# ransomware.py (leerling)
# DIT BESTAND MOET JE INLEVEREN
# NAAM: ......
from utils import is_truthy, training_level

LAAG = "LAAG"
MIDDEL = "MIDDEL"
HOOG = "HOOG"

def calculate_risk(features: dict) -> int:
    """
    TODO (leerling):
    - Bereken een risicoscore op basis van jullie regels uit fase 2.
    - Gebruik alleen objectieve checks (velden uit `features`).
    """
    score = 0

    # Voorbeeld hoe je een feature uitleest:
    # if not is_truthy(features.get("offline_backups")):
    #     score += 3  # geen offline back-ups -> hogere impact

    # TODO: voeg jouw regels toe

    return score

def classify(score: int) -> str:
    """
    TODO (leerling):
    - Zet score om naar LAAG / MIDDEL / HOOG
    - Gebruik drempels die passen bij jouw fase 2 ranges.
    """
    return LAAG
