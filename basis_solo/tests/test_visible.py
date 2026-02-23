import sys
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from ransomware import calculate_risk, classify, LAAG, MIDDEL, HOOG

CASES_PATH = ROOT / "tests/test-cases.json"

def _load():
    return json.loads(CASES_PATH.read_text(encoding="utf-8-sig"))

def test_classification_matches_expected():
    cases = _load()
    for c in cases:
        score = calculate_risk(c.get("features", {}) or {})
        label = classify(score)
        assert label == c["expected"], f"{c['id']} expected {c['expected']} but got {label} (score={score})"
