#!/usr/bin/env python3
"""Render the English, topic-first GitHub README from the paper database."""

from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "data" / "papers.json"
README_PATH = ROOT / "README.md"

TOPIC_ORDER = [
    "Language Models and NLP",
    "AI Agents and Tools",
    "AI for Science and Biology",
    "Computer Vision and Graphics",
    "Speech and Audio",
    "Multimodal Learning",
    "Robotics and Embodied AI",
    "Reinforcement Learning and Decision-Making",
    "Generative Models and World Models",
    "Representation Learning and Clustering",
    "Theory and Optimization",
    "Trustworthy AI and Safety",
    "AI Systems and Efficiency",
    "Datasets and Evaluation",
    "Graph Learning",
    "Other AI Research",
]


def clean(value: object) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip()


def md_link_label(value: str) -> str:
    return value.replace("\\", "\\\\").replace("[", "\\[").replace("]", "\\]")


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.casefold()).strip("-")


def display_status(paper: dict) -> str:
    if paper.get("year") == 2027 and paper.get("venue") == "ICLR":
        return "Under review"
    status = clean(paper.get("status"))
    if re.search(r"best paper|outstanding paper|honorable mention|award", status, re.I):
        return status
    if re.fullmatch(r"oral|spotlight|highlight|poster|findings|long|short|journal", status, re.I):
        return status.title()
    if "award" in paper.get("selection_reasons", []):
        return "Award recipient"
    return ""


def main() -> None:
    catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    papers = catalog.get("papers", [])
    grouped: dict[str, list[dict]] = defaultdict(list)
    for paper in papers:
        grouped[clean(paper.get("topic")) or "Other AI Research"].append(paper)

    topics = [topic for topic in TOPIC_ORDER if topic in grouped]
    topics.extend(sorted(set(grouped) - set(topics)))

    lines = [
        "# AI Research Papers by Topic",
        "",
        "## Contents",
        "",
    ]
    for topic in topics:
        lines.append(f"- [{topic}](#{slug(topic)})")
    lines += ["", "---", ""]

    for topic in topics:
        entries = grouped[topic]
        entries.sort(key=lambda p: (
            -int(p.get("year") or 0),
            clean(p.get("venue")).casefold(),
            clean(p.get("title")).casefold(),
        ))
        lines += [f"## {topic}", ""]
        for paper in entries:
            title = clean(paper.get("title")) or "Untitled paper"
            url = clean(paper.get("url"))
            title_text = f"[{md_link_label(title)}]({url})" if url else title
            venue_year = f"{clean(paper.get('venue'))} {int(paper.get('year') or 0)}".strip()
            status = display_status(paper)
            meta = f"{venue_year} · {status}" if status else venue_year
            direction = clean(paper.get("direction")) or "AI research"
            summary = clean(paper.get("summary")) or "Summary unavailable in the public source record."
            lines.append(f"- **{title_text}** — *{meta}*")
            lines.append(f"  - **Topic:** {direction}")
            lines.append(f"  - **Summary:** {summary}")
            lines.append("")

    lines += [
        "## Sources and updates",
        "",
        "- Data sources, selection rules, known gaps, and direct-source maintenance notes: [SOURCES.md](SOURCES.md).",
        "- The scheduled GitHub Actions workflow refreshes source records and regenerates this README daily. Review-score changes are stored with observation time and review phase so the internal ranking follows rebuttal updates.",
        "",
    ]
    README_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(f"Updated {README_PATH}")


if __name__ == "__main__":
    main()
