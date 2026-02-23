# app.py (gegeven)
import json
from pathlib import Path
from phishing import calculate_risk, classify

# Pak de email.json bestand
BASE_DIR = Path(__file__).parent
EMAILS_PATH = BASE_DIR / "emails.json"

def main() -> None:
    emails = json.loads(EMAILS_PATH.read_text(encoding="utf-8-sig"))

    correct = 0
    for e in emails:
        # Pak alle velden van de email
        sender = e.get("from", "")
        subject = e.get("subject", "")
        body = e.get("body", "")
        links = e.get("links", []) or []
        attachments = e.get("attachments", []) or []

        # Dit zijn de functies die jij implementeerd in phishing.py
        score = calculate_risk(sender, subject, body, links, attachments)
        label = classify(score)

        # Check of het antwoord overeen komt
        exp = e.get("expected")
        ok = (label == exp)
        correct += int(ok)
        print(f"{e['id']}: score={score:>2} label={label:<11} expected={exp:<11} -> {'OK' if ok else 'WRONG'}")

    print(f"\nResultaat: {correct}/{len(emails)} correct")

if __name__ == "__main__":
    main()