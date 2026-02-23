# util.py
import hashlib

def hash_sha256(tekst: str) -> str:
    """
    Geeft de SHA-256 hash terug van een tekst als hex-string.
    (Deze functie is 'vast' in het project.)
    """
    if not isinstance(tekst, str):
        raise TypeError("tekst moet een str zijn")
    return hashlib.sha256(tekst.encode("utf-8")).hexdigest()


def bereken_seconden(start: float, eind: float) -> float:
    """
    Hulpfunctie om tijdsduur te berekenen (afgerond op 3 decimalen).
    Handig als je later timing/efficiëntie wilt laten meten.
    """
    if not (isinstance(start, (int, float)) and isinstance(eind, (int, float))):
        raise TypeError("start en eind moeten getallen zijn")
    return round(eind - start, 3)