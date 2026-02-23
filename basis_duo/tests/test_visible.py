import sys
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from phishing import calculate_risk, classify, SAFE, SUSPICIOUS, PHISHING

EMAILS_PATH = ROOT / "tests/test-emails.json"

def _load():
    return json.loads(EMAILS_PATH.read_text(encoding="utf-8-sig"))

def test_classification_matches_expected():
    emails = _load()
    for e in emails:
        score = calculate_risk(
            e.get("from",""),
            e.get("subject",""),
            e.get("body",""),
            e.get("links",[]) or [],
            e.get("attachments",[]) or [],
        )
        label = classify(score)
        assert label == e["expected"], f"{e['id']} expected {e['expected']} but got {label} (score={score})"