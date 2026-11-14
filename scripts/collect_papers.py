#!/usr/bin/env python3
"""Refresh the English AI-paper catalogue from public conference records.

Numeric ratings and score-stage metadata stay in data/papers.json and the
review history file. The README generator deliberately omits them.
"""

from __future__ import annotations

import json
import math
import re
import time
from collections import defaultdict
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
CATALOG_PATH = DATA_DIR / "papers.json"
SOURCE_STATE_PATH = DATA_DIR / "source_state.json"
REVIEW_HISTORY_PATH = DATA_DIR / "review_score_history.json"
TOP20_PATH = DATA_DIR / "top20_raw.json"

PAPERLISTS_RAW = "https://raw.githubusercontent.com/papercopilot/paperlists/main"
PAPERLISTS_MEDIA = "https://media.githubusercontent.com/media/papercopilot/paperlists/main"
USER_AGENT = "AIResearchPaperCatalogue/1.0 (+https://github.com)"
YEARS = (2024, 2025, 2026)
SCORE_TOP_N = 15
PRESENTATION_TOP_N = 12
CITATION_TOP_N = 10
NORMALIZER_VERSION = 2

CONFERENCES = {
    "ICLR": "iclr",
    "ICML": "icml",
    "NeurIPS": "nips",
    "CVPR": "cvpr",
    "ICCV": "iccv",
    "ECCV": "eccv",
    "ACL": "acl",
    "EMNLP": "emnlp",
    "NAACL": "naacl",
    "AAAI": "aaai",
    "IJCAI": "ijcai",
    "AISTATS": "aistats",
    "KDD": "kdd",
    "COLM": "colm",
    "CoRL": "corl",
    "ICRA": "icra",
    "IROS": "iros",
}

CURRENT_ICLR_TOPICS = {
    "U1ObEVC4A7": ("Language Models and NLP", "Context management and agent memory"),
    "m5TLPK0U7O": ("Language Models and NLP", "Category induction in language models"),
    "XsOXBiKamY": ("Theory and Optimization", "Asynchronous distributed optimization"),
    "3WJt45k8b3": ("Computer Vision and Graphics", "Cross-spectral person re-identification"),
    "5PWu6Ds1fO": ("Representation Learning and Clustering", "Multi-view clustering"),
    "n9zG3wmMK9": ("Representation Learning and Clustering", "Uncertainty-aware multimodal clustering"),
    "RWcRiQ45vV": ("Computer Vision and Graphics", "Gaussian Splatting and light transport"),
    "V84yBc0EgP": ("Trustworthy AI and Safety", "Fair clustering"),
    "q1jd5DsPfx": ("AI Agents and Tools", "Agent red-teaming and safety"),
    "cRvwvthrBO": ("Theory and Optimization", "Generalization theory for contrastive learning"),
    "2dhoYgHiC2": ("Language Models and NLP", "Long-context inference and KV-cache compression"),
    "Lkq8S9i7Qm": ("Representation Learning and Clustering", "Incomplete multi-view clustering"),
    "Jn7WiQ9LtS": ("AI for Science and Biology", "Protein and biomolecular structure prediction"),
    "X4lPQWX5Ds": ("Theory and Optimization", "Gradient dynamics in recurrent networks"),
    "ZZ2jyq4qFC": ("Reinforcement Learning and Decision-Making", "Contextual bandits and job scheduling"),
    "IgVNSa3MMg": ("Language Models and NLP", "Efficient language-model training and inference"),
    "ddJW429f5j": ("AI Agents and Tools", "Long-horizon computer-use agents"),
    "gpt1K3Ia4D": ("Trustworthy AI and Safety", "Deception detection in language models"),
    "PQdqz0vaG5": ("Generative Models and World Models", "Interactive world-model evaluation"),
    "NpBFkL2BTm": ("Language Models and NLP", "Pretraining data and copyright"),
}

CURRENT_ICLR_SUMMARIES = {
    "U1ObEVC4A7": "Treats context as an editable file managed by the language model, extending the approach to multi-agent contexts. The authors report better accuracy with lower compute on long-context and long-horizon tasks.",
    "m5TLPK0U7O": "Continues pretraining models of different sizes on synthetic hierarchical facts. Properties transfer more readily within latent categories, and corresponding hierarchical structures emerge in model representations.",
    "XsOXBiKamY": "Analyzes the gap between homogeneous and heterogeneous data in asynchronous distributed optimization. It shows that common similarity assumptions do not remove the complexity barrier in heterogeneous settings and studies improvements under interpolation conditions.",
    "3WJt45k8b3": "Addresses cross-spectral and aerial-ground person re-identification by aligning spectral features and learning hierarchical cross-view features in one model.",
    "5PWu6Ds1fO": "Recasts multi-view clustering as symmetric incremental reasoning across views. Complementary view interaction, feature modulation, and semantic consistency are used to improve clustering.",
    "n9zG3wmMK9": "Addresses uncertainty and modality conflicts in multimodal clustering by adapting information compression to uncertainty, then combining uncertainty-aware fusion with evidence-theoretic opinion aggregation.",
    "RWcRiQ45vV": "Applies differentiable volumetric light transport to Gaussian Splatting to model subsurface scattering. The method reconstructs relightable objects from captures under a single light source.",
    "V84yBc0EgP": "Studies how fair clustering ensembles should account for the allocation of protected groups across clusters. It introduces an allocation-dependent distortion objective and analyzes its relationship to group disparities.",
    "q1jd5DsPfx": "Introduces a red-teaming platform and automated attack agents for evaluating tool use, prompt injection, and other safety risks across reproducible agent environments.",
    "cRvwvthrBO": "Studies the VC dimension and sample complexity of margin-based contrastive learning, deriving tighter upper and lower bounds for a previously unresolved margin setting.",
    "2dhoYgHiC2": "Finds that retrieval under chunked KV-cache compression depends on a token's position relative to compression boundaries. Different phases can produce substantial accuracy differences.",
    "Lkq8S9i7Qm": "Learns reliable correspondences for incomplete, unaligned multi-view data using a shared coordinate system and local sparse transport, reducing the effect of incorrect matches on clustering.",
    "Jn7WiQ9LtS": "Combines pair representations from multiple co-folding models to predict protein and other biomolecular complex structures without retraining the underlying models.",
    "X4lPQWX5Ds": "Shows that zero asymptotic drift in recurrent-network gradients does not guarantee finite-horizon stability, and characterizes diffusion-driven vanishing and exploding gradients.",
    "ZZ2jyq4qFC": "Studies online learning and job scheduling when service rates are unknown. It proposes WISE, an anytime algorithm with queue-regret guarantees that does not require a known time horizon.",
    "IgVNSa3MMg": "Nests language models of different sizes in one jointly trained architecture to reduce training costs and uses the embedded smaller model to improve speculative-decoding throughput.",
    "ddJW429f5j": "Introduces 108 long-horizon computer-use workflows covering cross-source reasoning, dynamic interfaces, and hidden-state inference for evaluating real-world computer-use agents.",
    "gpt1K3Ia4D": "Trains LoRA honesty adapters on on-policy dialogue to detect deception, reporting improved detection of unseen models over several probing baselines.",
    "PQdqz0vaG5": "Introduces a benchmark with 289 cases and 1,058 interaction turns for evaluating video quality, instruction following, consistency, and physical plausibility in interactive world models.",
    "NpBFkL2BTm": "Trains controlled 1B-parameter models to compare web text, public-domain books, and contemporary fiction as pretraining data, including their effects on creative-writing performance.",
}

TOPIC_RULES = [
    ("AI for Science and Biology", "Protein, molecule, and biological modeling", r"\bprotein\b|\bpeptide\b|\bantibod(?:y|ies)\b|\bbiomolecular\b|\bmolecules?\b|\bmolecular\b|\bdrug discovery\b|\bgenomics?\b|\bcell(?:s|ular)?\b|\bbiology\b|\bbiological\b|\bmedical\b|\bclinical\b|\bhealthcare\b|\bchemistry\b|\benzymes?\b|\bgenomes?\b|\bRNA\b|\bDNA\b|\bdrugs?\b"),
    ("Robotics and Embodied AI", "Robotics, control, and embodied learning", r"\brobot(?:ics|ic)?\b|\bembodied\b|\bmanipulation\b|\bautonomous driving\b|\bnavigation\b|\blocomo(?:tion|tive)\b|\bmotor control\b|\bsim-to-real\b"),
    ("AI Agents and Tools", "Agents, tool use, and planning", r"\bagents?\b|\btool[- ]use\b|\bcomputer use\b|\bbrowser use\b|\bweb agents?\b|\bautonomous workflows?\b|\bplanning agents?\b|\bmulti-agents?\b"),
    ("Language Models and NLP", "Language modeling, reasoning, and NLP", r"\blarge language models?\b|\bLLMs?\b|\blanguage models?\b|\bnatural language\b|\bNLP\b|\btext generation\b|\bpre[- ]training\b|\btokenizers?\b|\btransformers?\b|\binstruction tuning\b|\breasoning\b|\bretrieval[- ]augmented\b|\bRAG\b"),
    ("Speech and Audio", "Speech, audio, and music", r"\bspeech\b|\baudio\b|\bmusic\b|\bvoice\b|\bacoustic\b|\bsound events?\b|\btext-to-speech\b|\bspeech recognition\b"),
    ("Computer Vision and Graphics", "Vision, video, and 3D graphics", r"\bcomputer vision\b|\bimages?\b|\bvideos?\b|\bvisual\b|\b3D\b|\bGaussian Splatting\b|\brendering\b|\bsegmentation\b|\bobject detection\b|\bimage recognition\b|\bre-identification\b|\bpoint clouds?\b|\bNeRFs?\b|\bdiffusion for images?\b"),
    ("Multimodal Learning", "Multimodal learning and fusion", r"\bmultimodal\b|\bmulti-modal\b|\bvision-language\b|\bvision language\b|\bimage-text\b|\baudio-visual\b|\bcross-modal\b|\bcross modal\b"),
    ("Reinforcement Learning and Decision-Making", "Reinforcement learning, bandits, and decisions", r"\breinforcement learning\b|\bRL\b|\bcontextual bandits?\b|\bbandits?\b|\bpolicy optimization\b|\bdecision[- ]making\b|\bqueueing\b|\bscheduling\b|\bMarkov decision\b|\bMDPs?\b"),
    ("Generative Models and World Models", "Generative modeling and world models", r"\bdiffusion\b|\bgenerative models?\b|\bgeneration\b|\bflow matching\b|\bworld models?\b|\bscore-based\b|\bautoregressive generation\b|\bnormalizing flows?\b"),
    ("Trustworthy AI and Safety", "Safety, privacy, fairness, and robustness", r"\bprivacy\b|\bfairness\b|\bfair clustering\b|\bred[- ]team(?:ing)?\b|\bdeception\b|\bhonesty\b|\btrustworthy\b|\bsecurity\b|\bsafety\b|\battacks?\b|\badversarial\b|\balignment\b|\brobustness\b|\binterpretability\b|\bexplainability\b"),
    ("Theory and Optimization", "Learning theory and optimization", r"\btheor(?:em|etical|y)\b|\bVC dimension\b|\bsample complexity\b|\bgeneralization bound\b|\boptimization\b|\bgradient descent\b|\bconvergence\b|\basynchronous optimization\b|\bLyapunov\b|\bregret\b|\bcomplexity bound\b"),
    ("Representation Learning and Clustering", "Representation learning and clustering", r"\bclustering\b|\bcontrastive learning\b|\brepresentation learning\b|\bmulti-view\b|\bmultiview\b|\bself-supervised\b|\bunsupervised\b|\bembeddings?\b|\bmetric learning\b|\bmanifold learning\b"),
    ("AI Systems and Efficiency", "Inference, training, and infrastructure", r"\binference\b|\bquantization\b|\bserving\b|\bhardware\b|\baccelerators?\b|\bmemory-efficient\b|\bcompute-efficient\b|\bsystems\b|\binfrastructure\b|\bcaches?\b|\bdistributed training\b|\bparallel training\b|\bcompilers?\b"),
    ("Datasets and Evaluation", "Datasets, benchmarks, and evaluation", r"\bbenchmarks?\b|\bdatasets?\b|\bevaluation\b|\bleaderboards?\b|\bassessments?\b|\btest suites?\b|\bcorpora\b|\bdata collection\b"),
    ("Graph Learning", "Graph learning and network analysis", r"\bgraph neural\b|\bgraph learning\b|\bknowledge graphs?\b|\bnetwork analysis\b|\bgraph representations?\b|\bGNNs?\b"),
]

ACCEPTED_NEGATIVE = re.compile(r"reject|withdraw|desk\s*reject|declined|not accepted", re.I)
PRESENTATION_RE = re.compile(r"\b(oral|spotlight|highlight|best paper|distinguished paper)\b", re.I)
SUPPRESSED_RECORD_URLS = {"https://aclanthology.org/2024.acl-short.69/"}


def load_json(path: Path, fallback: Any) -> Any:
    if not path.exists():
        return fallback
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return fallback


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def clean(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip()


def values(value: Any) -> list[float]:
    if value is None or value == "":
        return []
    if isinstance(value, (int, float)):
        return [float(value)]
    if isinstance(value, list):
        result = []
        for item in value:
            result.extend(values(item))
        return result
    if isinstance(value, str):
        result = []
        for item in re.split(r"[;,|]", value):
            item = item.strip()
            if not item or item.casefold() in {"-", "none", "nan", "null", "n/a"}:
                continue
            try:
                number = float(item)
                if math.isfinite(number):
                    result.append(number)
            except ValueError:
                continue
        return result
    return []


def mean_and_sd(value: Any) -> tuple[float | None, float | None]:
    if isinstance(value, list) and value:
        try:
            return float(value[0]), float(value[1]) if len(value) > 1 else None
        except (TypeError, ValueError):
            pass
    numbers = values(value)
    if not numbers:
        return None, None
    avg = sum(numbers) / len(numbers)
    sd = math.sqrt(sum((x - avg) ** 2 for x in numbers) / len(numbers))
    return avg, sd


def is_trueish(value: Any) -> bool:
    if value is True:
        return True
    if isinstance(value, (int, float)):
        return value != 0
    if isinstance(value, list):
        return any(is_trueish(item) for item in value)
    return clean(value).casefold() in {"true", "yes", "1", "award", "best paper", "outstanding paper"}


def has_rebuttal_activity(paper: dict[str, Any], key: str) -> bool:
    value = paper.get(key)
    if value in (None, "", [], {}):
        return False
    if isinstance(value, str):
        return clean(value).casefold() not in {"-", "none", "nan", "no response", "[]"}
    return bool(value)


def classify(paper: dict[str, Any]) -> tuple[str, str]:
    title = clean(paper.get("title"))
    metadata = " ".join(clean(paper.get(k)) for k in ("tldr", "track", "primary_area", "keywords"))
    abstract = clean(paper.get("abstract"))
    best = (0, "Other AI Research", "Machine learning and artificial intelligence")
    for topic, subtopic, pattern in TOPIC_RULES:
        title_hits = len(re.findall(pattern, title, re.I))
        metadata_hits = len(re.findall(pattern, metadata, re.I))
        abstract_hits = len(re.findall(pattern, abstract, re.I))
        score = title_hits * 6 + min(metadata_hits, 3) * 3 + min(abstract_hits, 4)
        if score > best[0]:
            best = (score, topic, subtopic)
    if best[0]:
        return best[1], best[2]
    return "Other AI Research", "Machine learning and artificial intelligence"


def short_summary(paper: dict[str, Any], forum_id: str = "") -> str:
    if forum_id in CURRENT_ICLR_SUMMARIES:
        return CURRENT_ICLR_SUMMARIES[forum_id]
    tldr = clean(paper.get("tldr"))
    abstract = clean(paper.get("abstract"))
    source = tldr or abstract
    if not source:
        return "Summary unavailable in the public source record."
    sentences = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9])", source)
    summary = sentences[0] if sentences else source
    if len(summary) > 280:
        summary = summary[:277].rsplit(" ", 1)[0] + "..."
    return summary


def source_fingerprint(url: str) -> tuple[str | None, str | None, int | None]:
    req = Request(url, headers={"User-Agent": USER_AGENT}, method="HEAD")
    try:
        with urlopen(req, timeout=25) as response:
            size = response.headers.get("Content-Length")
            return response.headers.get("ETag"), response.headers.get("Last-Modified"), int(size) if size and size.isdigit() else None
    except HTTPError as error:
        if error.code == 404:
            return None, "404", None
        raise


def fetch_source(url: str, relpath: str) -> list[dict[str, Any]]:
    req = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    with urlopen(req, timeout=90) as response:
        payload = response.read()
    if b"version https://git-lfs.github.com/spec/v1" in payload[:300]:
        media_url = f"{PAPERLISTS_MEDIA}/{relpath}"
        req = Request(media_url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
        with urlopen(req, timeout=180) as response:
            payload = response.read()
    data = json.loads(payload.decode("utf-8", "replace"))
    if not isinstance(data, list):
        raise ValueError(f"Unexpected source format for {relpath}: expected a JSON array")
    return data


def paper_url(source: dict[str, Any]) -> str:
    for key in ("openreview", "oa", "proceeding", "site", "pdf", "url"):
        url = clean(source.get(key))
        if url.startswith("http://") or url.startswith("https://"):
            return url
    return ""


def score_record(source: dict[str, Any]) -> dict[str, Any]:
    ratings = values(source.get("rating"))
    mean, sd = mean_and_sd(source.get("rating_avg"))
    if mean is None and ratings:
        mean = sum(ratings) / len(ratings)
    confidence = values(source.get("confidence"))
    confidence_mean, confidence_sd = mean_and_sd(source.get("confidence_avg"))
    if confidence_mean is None and confidence:
        confidence_mean = sum(confidence) / len(confidence)
    return {
        "ratings": ratings,
        "score_mean": round(mean, 4) if mean is not None else None,
        "score_sd": round(sd, 4) if sd is not None else None,
        "confidence": confidence,
        "confidence_mean": round(confidence_mean, 4) if confidence_mean is not None else None,
    }


def award_signal(source: dict[str, Any]) -> list[str]:
    signals = []
    for key in ("award", "awards", "award_name", "best_paper", "honorable_mention"):
        value = source.get(key)
        if is_trueish(value):
            signals.append("award")
        elif isinstance(value, str) and re.search(r"award|best paper|outstanding|honorable|distinguished", value, re.I):
            signals.append("award")
    title = clean(source.get("title"))
    status = clean(source.get("status"))
    if re.search(r"best paper|outstanding paper|test of time|best student paper", title + " " + status, re.I):
        signals.append("award")
    return sorted(set(signals))


def normalize_record(source: dict[str, Any], venue: str, year: int, source_id: str, retrieved_at: str) -> dict[str, Any] | None:
    title = clean(source.get("title"))
    if not title:
        return None
    native_id = clean(source.get("id") or source.get("openreview_forum") or source.get("paper_id"))
    if not native_id:
        native_id = re.sub(r"[^a-z0-9]+", "-", title.casefold()).strip("-")[:80]
    rid = f"{venue}-{year}-{native_id}"
    topic, subtopic = classify(source)
    score = score_record(source)
    raw_status = clean(source.get("status"))
    presentation = raw_status if PRESENTATION_RE.search(raw_status) else ""
    reasons = award_signal(source)
    if presentation:
        reasons.append("presentation")
    author_reply = has_rebuttal_activity(source, "reply_authors")
    reviewer_reply = has_rebuttal_activity(source, "reply_reviewers")
    record = {
        "id": rid,
        "source_id": source_id,
        "native_id": native_id,
        "title": title,
        "venue": venue,
        "year": year,
        "url": paper_url(source),
        "topic": topic,
        "direction": subtopic,
        "summary": short_summary(source, native_id),
        "status": raw_status,
        "selection_reasons": reasons,
        "citation_count": values(source.get("gs_citation"))[0] if values(source.get("gs_citation")) else None,
        "score_mean": score["score_mean"],
        "score_sd": score["score_sd"],
        "score_scale_max": None,
        "ratings": score["ratings"],
        "review_count": len(score["ratings"]),
        "confidence": score["confidence"],
        "confidence_mean": score["confidence_mean"],
        "score_snapshot_at": retrieved_at,
        "score_phase": (
            "archive snapshot with rebuttal activity"
            if score["ratings"] and (author_reply or reviewer_reply)
            else "archive snapshot; exact rebuttal phase unknown" if score["ratings"] else None
        ),
        "author_response_present": author_reply,
        "reviewer_followup_present": reviewer_reply,
        "source_url": f"{PAPERLISTS_RAW}/{CONFERENCES[venue]}/{CONFERENCES[venue]}{year}.json",
    }
    return record


def select_records(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    records = [r for r in records if r.get("url") not in SUPPRESSED_RECORD_URLS]
    scored = [r for r in records if r["review_count"] >= 3 and r["score_mean"] is not None and not ACCEPTED_NEGATIVE.search(r["status"])]
    scored.sort(key=lambda r: (-r["score_mean"], -r["review_count"], -(r["confidence_mean"] or 0), r["title"].casefold()))
    selected: dict[str, dict[str, Any]] = {}
    for record in scored[:SCORE_TOP_N]:
        record["selection_reasons"] = sorted(set(record["selection_reasons"] + ["public_review_selection"]))
        selected[record["id"]] = record

    awards = [r for r in records if "award" in r["selection_reasons"]]
    for record in awards:
        selected[record["id"]] = record

    presentations = [r for r in records if "presentation" in r["selection_reasons"] and not ACCEPTED_NEGATIVE.search(r["status"])]
    presentations.sort(key=lambda r: (
        -(r["score_mean"] if r["score_mean"] is not None else -1),
        -(r["citation_count"] if r["citation_count"] is not None else -1),
        r["title"].casefold(),
    ))
    for record in presentations[:PRESENTATION_TOP_N]:
        record["selection_reasons"] = sorted(set(record["selection_reasons"] + ["notable_presentation"]))
        selected[record["id"]] = record

    if not selected:
        cited = [r for r in records if r["citation_count"] is not None and not ACCEPTED_NEGATIVE.search(r["status"])]
        cited.sort(key=lambda r: (-r["citation_count"], r["title"].casefold()))
        for record in cited[:CITATION_TOP_N]:
            record["selection_reasons"] = ["citation_signal"]
            selected[record["id"]] = record

    return list(selected.values())


def current_iclr_phase(today: date) -> str:
    reviews_release = date(2026, 11, 5)
    public_discussion_end = date(2026, 11, 18)
    decision_date = date(2026, 12, 16)
    if today < reviews_release:
        return "pre-rebuttal review period"
    if today <= public_discussion_end:
        return "author rebuttal and public discussion"
    if today < decision_date:
        return "post-rebuttal area-chair discussion"
    return "post-decision public record"


def merge_live_iclr(records: dict[str, dict[str, Any]], raw: dict[str, Any], retrieved_at: str, phase: str) -> None:
    for source in raw.get("selected", []):
        forum_id = clean(source.get("forum_id"))
        if not forum_id:
            continue
        topic, subtopic = CURRENT_ICLR_TOPICS.get(forum_id, ("Other AI Research", "Topic classification pending"))
        existing = records.get(f"ICLR-2027-{forum_id}", {})
        record = {
            "id": f"ICLR-2027-{forum_id}",
            "source_id": "ICLR-2027-live-reviews",
            "native_id": forum_id,
            "title": clean(source.get("title")),
            "venue": "ICLR",
            "year": 2027,
            "url": clean(source.get("openreview_url")) or f"https://openreview.net/forum?id={forum_id}",
            "topic": topic,
            "direction": subtopic,
            "summary": CURRENT_ICLR_SUMMARIES.get(forum_id, clean(source.get("abstract_snippet")) or "Short description unavailable; see the public submission."),
            "status": "Under review",
            "selection_reasons": ["current public-review selection"],
            "citation_count": None,
            "score_mean": round(float(source.get("mean_rating", 0)), 4),
            "score_sd": None,
            "score_scale_max": 4,
            "ratings": [float(x) for x in source.get("ratings", [])],
            "review_count": int(source.get("n_reviews", len(source.get("ratings", [])))),
            "confidence": [float(x) for x in source.get("confidence", [])],
            "confidence_mean": round(float(source["mean_confidence"]), 4) if source.get("mean_confidence") is not None else None,
            "score_snapshot_at": retrieved_at,
            "score_phase": phase,
            "author_response_present": bool(existing.get("author_response_present", False)),
            "reviewer_followup_present": bool(existing.get("reviewer_followup_present", False)),
            "source_url": clean(raw.get("source_rating_table")),
        }
        records[record["id"]] = record


def update_review_history(records: dict[str, dict[str, Any]], history: dict[str, Any], observed_at: str, phase: str) -> None:
    snapshots = history.setdefault("snapshots", [])
    live = [r for r in records.values() if r.get("source_id") == "ICLR-2027-live-reviews"]
    signature = {
        r["id"]: {"ratings": r.get("ratings", []), "score_mean": r.get("score_mean")}
        for r in sorted(live, key=lambda x: x["id"])
    }
    if not signature:
        return
    last = snapshots[-1] if snapshots else None
    if last and last.get("scores") == signature and last.get("phase") == phase:
        history["last_checked_at"] = observed_at
        return
    snapshots.append({"source": "ICLR 2027", "observed_at": observed_at, "phase": phase, "scores": signature})
    history["last_checked_at"] = observed_at


def main() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc)
    observed_at = now.isoformat(timespec="seconds").replace("+00:00", "Z")
    retrieved_at_local = now.astimezone(ZoneInfo("Asia/Shanghai")).isoformat(timespec="seconds")
    old_catalog = load_json(CATALOG_PATH, {"papers": []})
    old_records = {p["id"]: p for p in old_catalog.get("papers", []) if p.get("id")}
    state = load_json(SOURCE_STATE_PATH, {"sources": {}})
    source_state: dict[str, Any] = state.setdefault("sources", {})
    records_by_source: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in old_records.values():
        if record.get("source_id"):
            records_by_source[record["source_id"]].append(record)

    updated_sources = 0
    unchanged_sources = 0
    errors: list[str] = []
    sources = [(venue, slug, year, f"{slug}{year}.json") for venue, slug in CONFERENCES.items() for year in YEARS]

    for venue, slug, year, relpath in sources:
        source_id = f"{venue}-{year}"
        url = f"{PAPERLISTS_RAW}/{slug}/{relpath}"
        try:
            etag, modified, size = source_fingerprint(url)
            if modified == "404":
                unchanged_sources += 1
                continue
            previous = source_state.get(source_id, {})
            fingerprint = etag or modified or str(size)
            if previous.get("fingerprint") == fingerprint and previous.get("normalizer_version") == NORMALIZER_VERSION and records_by_source.get(source_id):
                unchanged_sources += 1
                continue

            source_papers = fetch_source(url, f"{slug}/{relpath}")
            normalized = [normalize_record(p, venue, year, source_id, retrieved_at_local) for p in source_papers]
            normalized = [p for p in normalized if p]
            selected = select_records(normalized)
            records_by_source[source_id] = selected
            source_state[source_id] = {
                "url": url,
                "etag": etag,
                "last_modified": modified,
                "content_length": size,
                "fingerprint": fingerprint,
                "updated_at": retrieved_at_local,
                "source_records": len(source_papers),
                "selected_records": len(selected),
                "normalizer_version": NORMALIZER_VERSION,
            }
            updated_sources += 1
            print(f"{source_id}: {len(source_papers)} source records -> {len(selected)} selected")
        except (HTTPError, URLError, TimeoutError, OSError, ValueError, json.JSONDecodeError) as error:
            errors.append(f"{source_id}: {error}")
            if not records_by_source.get(source_id):
                print(f"{source_id}: unavailable ({error})")
            time.sleep(0.1)

    flat_records = {record["id"]: record for records in records_by_source.values() for record in records}
    raw_live = load_json(TOP20_PATH, {})
    phase = current_iclr_phase(now.astimezone(ZoneInfo("America/Los_Angeles")).date())
    if raw_live.get("selected"):
        merge_live_iclr(flat_records, raw_live, retrieved_at_local, phase)
        history = load_json(REVIEW_HISTORY_PATH, {"snapshots": []})
        update_review_history(flat_records, history, observed_at, phase)
        write_json(REVIEW_HISTORY_PATH, history)

    papers = list(flat_records.values())
    papers.sort(key=lambda p: (p.get("topic", "").casefold(), -int(p.get("year", 0)), p.get("venue", ""), p.get("title", "").casefold()))
    catalog = {
        "updated_at": retrieved_at_local,
        "start_year": 2024,
        "venues": list(CONFERENCES),
        "paper_count": len(papers),
        "papers": papers,
        "selection_policy": {
            "public_review_records_per_venue_year": SCORE_TOP_N,
            "notable_presentations_per_venue_year": PRESENTATION_TOP_N,
            "highly_cited_fallback_per_venue_year": CITATION_TOP_N,
            "note": "Numeric review ratings are stored here and omitted from README.md.",
        },
    }
    write_json(CATALOG_PATH, catalog)
    write_json(SOURCE_STATE_PATH, {"updated_at": retrieved_at_local, "sources": source_state, "errors": errors})
    print(f"Catalogue: {len(papers)} papers; {updated_sources} source files refreshed; {unchanged_sources} unchanged or not yet available.")
    if errors:
        print(f"Source errors: {len(errors)} (retained prior data for unchanged failures)")


if __name__ == "__main__":
    main()
