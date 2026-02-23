# phishing.py (leerling)
# DIT BESTAND MOET JE INLEVEREN
# NAMEN: ......
from utils import domain_from_email, domain_from_url, has_executable_attachment, contains_any

SAFE = "SAFE"
SUSPICIOUS = "SUSPICOUS"
PHISHING = "PHISHING"

# Dit is een lijst met websites die we vertrouwen. 
# Vul hem aan met de verwachtte websites die je vertrouwd. 
TRUSTED = ["odido.nl", "postnl.nl"]

def calculate_risk(sender: str, subject: str, body: str, links: list[str], attachments: list[str]) -> int:
    """
    TODO (leerling):
    - Bereken een risicoscore op basis van jullie regels uit fase 2.
    - Gebruik alleen objectieve checks.
    """
    score = 0

    """
    TODO: voeg jullie regels toe
    Er zijn een aantal functies die je mag gebruiken om jezelf te helpen. 
    Je kunt deze vindein in utils.py. 
    Als je meer hulp functies nodig hebt, plaats deze dan in phishing.py en niet in utils.py

    VOORBEELD:
    Als je wilt controleren de zender een vertrouwde email uitgang heeft:
        if contains_any(sender, TRUSTED):
            score += 2

    Als je wilt controleren of er een .exe bijlage is:
        if has_executable(attachments):
            score += 3

    Je mag meerdere regels combineren.
    """


    return score

def classify(score: int) -> str:
    """
    TODO (leerling):
    - Zet score om naar SAFE / SUSPICIOUS / PHISHING
    - Gebruik drempels die passen bij jullie fase 2 ranges.
    """
    return SAFE