import time
from typing import Union

def huidige_tijd() -> float:
    return time.perf_counter()

def bereken_seconden(start: Union[int, float], eind: Union[int, float]) -> float:
    if not (isinstance(start, (int, float)) and isinstance(eind, (int, float))):
        raise TypeError("start en eind moeten getallen zijn")
    return round(float(eind) - float(start), 3)

ALFABET_START = ord('A')
ALFABET_LENGTE = 26

def normaliseer_tekst(tekst: str) -> str:
    """
    Zet tekst om naar alleen hoofdletters A-Z.
    Verwijdert spaties en andere tekens.
    """
    resultaat = ""
    for teken in tekst.upper():
        if 'A' <= teken <= 'Z':
            resultaat += teken
    return resultaat


def naar_getal(teken: str) -> int:
    """
    Zet een hoofdletter om naar een getal.
    A -> 0
    B -> 1
    ...
    Z -> 25
    """
    return ord(teken) - ALFABET_START


def naar_teken(getal: int) -> str:
    """
    Zet een getal om naar een hoofdletter.
    0 -> A
    1 -> B
    ...
    25 -> Z
    """
    return chr(getal + ALFABET_START)


def modulo_alfabet(getal: int) -> int:
    """
    Zorgt dat een getal binnen 0-25 blijft.
    Ondersteunt ook negatieve getallen.
    """
    return getal % ALFABET_LENGTE
