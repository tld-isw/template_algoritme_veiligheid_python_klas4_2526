# utils.py
import time

def krijg_tijd() -> float:
    """Geeft een tijdstempel terug (hoog-resolutie) om tijd te meten."""
    return time.perf_counter()

def bereken_seconden(start: float, eind: float) -> float:
    """Aantal seconden tussen start en eind, afgerond op 3 decimalen."""
    return round(eind - start, 3)

def wacht(seconden: float):
    time.sleep(seconden)