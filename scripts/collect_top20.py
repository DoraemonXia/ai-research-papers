#!/usr/bin/env python3
"""Collect and rank high-scoring ICLR 2027 submissions from public review data.

The public Paper Copilot review table exposes the raw rating values from
OpenReview. This script reads its default rating-ordered pages, independently
computes arithmetic mean ratings, and fetches abstracts for the selected papers.
It excludes papers with fewer than three posted ratings from the main ranking.
"""

from __future__ import annotations

import html
import json
import re
import time
from dataclasses import asdict, dataclass
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.parse import urlencode
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
STATS_URL = "https://papercopilot.com/statistics/iclr-statistics/iclr-2027-statistics/"
PAPERLIST_URL = "https://papercopilot.com/paper-list/iclr-paper-list/iclr-2027-paper-list/"
AJAX_URL = "https://papercopilot.com/wp-admin/admin-ajax.php"
USER_AGENT = "Mozilla/5.0 (compatible; ICLR2027ScoreResearch/1.0)"
PAGE_SIZE = 100
TOP_N = 20


class TableParser(HTMLParser):
    """Small HTML table parser retaining cell attributes and anchor URLs."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.rows: list[list[dict[str, Any]]] = []
        self.row: list[dict[str, Any]] | None = None
        self.cell: dict[str, Any] | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = dict(attrs)
        if tag == "tr":
            self.row = []
        elif tag == "td" and self.row is not None:
            self.cell = {"attrs": attrs_dict, "text": "", "href": None}
            self.row.append(self.cell)
        elif tag == "a" and self.cell is not None:
            self.cell["href"] = attrs_dict.get("href")
        elif tag == "br" and self.cell is not None:
            self.cell["text"] += "\n"

    def handle_data(self, data: str) -> None:
        if self.cell is not None:
            self.cell["text"] += data

    def handle_endtag(self, tag: str) -> None:
        if tag == "td":
            self.cell = None
        elif tag == "tr" and self.row is not None:
            self.rows.append(self.row)
            self.row = None


def get_text(url: str) -> str:
    req = Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/json, */*",
            "Referer": STATS_URL,
        },
    )
    with urlopen(req, timeout=60) as response:
        return response.read().decode("utf-8", "replace")


def get_json(url: str, referer: str) -> dict[str, Any]:
    req = Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "application/json, text/plain, */*",
            "Referer": referer,
        },
    )
    with urlopen(req, timeout=90) as response:
        return json.loads(response.read().decode("utf-8", "replace"))


def request_page(mode: str, batch: int, **extras: str) -> dict[str, Any]:
    params = {
        "action": "load_paperlist",
        "batch": str(batch),
        "conf": "iclr",
        "year": "2027",
        "mode": mode,
        "track": "main",
        "surface": "papers",
        "filters": "[]",
        **extras,
    }
    return get_json(f"{AJAX_URL}?{urlencode(params)}", STATS_URL if mode == "rating" else PAPERLIST_URL)


def raw_numbers(cell: dict[str, Any]) -> list[float]:
    raw = cell["attrs"].get("data-search-raw", "")
    return [float(value.strip()) for value in raw.split(",") if value.strip()]


@dataclass
class Paper:
    title: str
    forum_id: str
    track: str
    status: str
    ratings: list[float]
    confidence: list[float]
    mean_rating: float
    mean_confidence: float | None
    abstract: str = ""

    @property
    def n_reviews(self) -> int:
        return len(self.ratings)


def parse_rating_rows(markup: str) -> list[Paper]:
    parser = TableParser()
    parser.feed(markup)
    papers: list[Paper] = []
    for row in parser.rows:
        if len(row) < 6:
            continue
        href = row[1].get("href") or ""
        match = re.search(r"[?&]id=([^&]+)", href)
        if not match:
            continue
        ratings = raw_numbers(row[4])
        if not ratings:
            continue
        confidence = raw_numbers(row[5])
        papers.append(
            Paper(
                title=html.unescape(row[1]["text"]).strip(),
                forum_id=match.group(1),
                track=row[2]["text"].strip(),
                status=row[3]["text"].strip(),
                ratings=ratings,
                confidence=confidence,
                mean_rating=sum(ratings) / len(ratings),
                mean_confidence=sum(confidence) / len(confidence) if confidence else None,
            )
        )
    return papers


def fetch_abstract(paper: Paper) -> str:
    # The table's title search uses a quoted phrase, allowing a narrow public
    # query without downloading the full 42k-paper abstract collection.
    filters = [{"colIndex": 1, "terms": [paper.title.lower()]}]
    payload = request_page(
        "detail",
        0,
        filters=json.dumps(filters, ensure_ascii=False, separators=(",", ":")),
        paper_dims='["abstract"]',
    )
    parser = TableParser()
    parser.feed(payload.get("html", ""))
    target = re.sub(r"\s+", " ", paper.title).strip().casefold()
    for row in parser.rows:
        if len(row) < 5:
            continue
        title = row[1]["text"].split("\n", 1)[0].strip()
        if re.sub(r"\s+", " ", title).strip().casefold() != target:
            continue
        abstract = row[4]["attrs"].get("data-search", "")
        return html.unescape(abstract).strip()
    return ""


def main() -> None:
    # The page announces the current data source and its data collection mode.
    # Retrieve the first ranked page, then continue until the next page's best
    # arithmetic mean is below the current top-20 cutoff.
    all_papers: list[Paper] = []
    batches: list[dict[str, Any]] = []
    batch = 0
    cutoff: float | None = None

    while True:
        payload = request_page(
            "rating",
            batch,
            review_dims='["rating","confidence"]',
            review_metric_search="raw",
            review_metric_search_map="{}",
        )
        current = parse_rating_rows(payload.get("html", ""))
        if not current:
            raise RuntimeError(f"No rating rows returned for batch {batch}")
        batches.append(
            {
                "batch": batch,
                "offset": payload.get("offset"),
                "count": payload.get("count"),
                "max_mean": max(p.mean_rating for p in current),
                "min_mean": min(p.mean_rating for p in current),
            }
        )
        all_papers.extend(current)

        eligible = [p for p in all_papers if p.n_reviews >= 3]
        eligible.sort(
            key=lambda p: (
                -p.mean_rating,
                -p.n_reviews,
                -(p.mean_confidence if p.mean_confidence is not None else -1),
                p.title.casefold(),
            )
        )
        if len(eligible) >= TOP_N:
            cutoff = eligible[TOP_N - 1].mean_rating
            # Pages are returned in the site's default descending rating order.
            # If the just-fetched page is entirely below the cutoff, the top 20
            # is complete. Otherwise fetch the next page and compare again.
            if batch > 0 and max(p.mean_rating for p in current) < cutoff:
                break
        if not payload.get("has_more", False):
            break
        batch += 1
        time.sleep(0.15)

    eligible = [p for p in all_papers if p.n_reviews >= 3]
    eligible.sort(
        key=lambda p: (
            -p.mean_rating,
            -p.n_reviews,
            -(p.mean_confidence if p.mean_confidence is not None else -1),
            p.title.casefold(),
        )
    )
    selected = eligible[:TOP_N]
    if len(selected) < TOP_N:
        raise RuntimeError(f"Only {len(selected)} papers had at least three posted ratings")

    for index, paper in enumerate(selected):
        paper.abstract = fetch_abstract(paper)
        if not paper.abstract:
            raise RuntimeError(f"Could not find the abstract for {paper.title}")
        if index < len(selected) - 1:
            time.sleep(0.15)

    selected_payload = []
    for paper in selected:
        item = asdict(paper)
        item.pop("abstract", None)
        sentences = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9])", paper.abstract)
        snippet = sentences[0].strip() if sentences else paper.abstract.strip()
        item["abstract_snippet"] = snippet[:277].rsplit(" ", 1)[0] + "..." if len(snippet) > 280 else snippet
        item["n_reviews"] = paper.n_reviews
        item["openreview_url"] = f"https://openreview.net/forum?id={paper.forum_id}"
        selected_payload.append(item)

    result = {
        "venue": "ICLR 2027",
        "retrieved_at_local": time.strftime("%Y-%m-%d %H:%M:%S %z"),
        "source_rating_table": "https://papercopilot.com/statistics/iclr-statistics/iclr-2027-statistics/",
        "source_paperlist": PAPERLIST_URL,
        "review_scale": "1-4",
        "ranking_rule": "Arithmetic mean of raw ratings; require >=3 posted ratings; tie break by review count, mean confidence, then title.",
        "pages_checked": batches,
        "selected": selected_payload,
    }
    output = ROOT / "data" / "top20_raw.json"
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {output}")
    print(f"Saved the current review snapshot for {len(selected)} papers.")


if __name__ == "__main__":
    main()
