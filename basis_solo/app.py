# app.py (gegeven)
import json
from pathlib import Path
from ransomware import calculate_risk, classify

BASE_DIR = Path(__file__).parent
CASES_PATH = BASE_DIR / "cases.json"

def main() -> None:
    cases = json.loads(CASES_PATH.read_text(encoding="utf-8-sig"))

    correct = 0
    for c in cases:
        # Pak alle velden van de casus (organisatiesituatie)
        features = c.get("features", {}) or {}

        score = calculate_risk(features)
        label = classify(score)

        exp = c.get("expected")
        ok = (label == exp)
        correct += int(ok)
        print(f"{c['id']}: score={score:>2} label={label:<7} expected={exp:<7} -> {'OK' if ok else 'WRONG'}")

    print(f"\nResultaat: {correct}/{len(cases)} correct")

if __name__ == "__main__":
    main()
