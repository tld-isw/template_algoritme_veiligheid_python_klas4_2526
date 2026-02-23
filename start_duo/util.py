import time
from pathlib import Path
from typing import Union, Iterable

def huidige_tijd() -> float:
    """Gebruik perf_counter voor nauwkeurige timings."""
    return time.perf_counter()

def bereken_seconden(start: Union[int, float], eind: Union[int, float]) -> float:
    """Rond af op milliseconden voor nette output."""
    if not (isinstance(start, (int, float)) and isinstance(eind, (int, float))):
        raise TypeError("start en eind moeten getallen zijn")
    return round(float(eind) - float(start), 3)

def format_pin(getal: int, lengte: int) -> str:
    """Zet een getal om naar een PIN met voorloopnullen."""
    if not isinstance(getal, int):
        raise TypeError("getal moet een int zijn")
    if not isinstance(lengte, int):
        raise TypeError("lengte moet een int zijn")
    if lengte <= 0:
        raise ValueError("lengte moet > 0 zijn")
    max_waarde = 10 ** lengte
    if not (0 <= getal < max_waarde):
        raise ValueError(f"getal moet tussen 0 en {max_waarde-1} liggen voor lengte {lengte}")
    return str(getal).zfill(lengte)

def is_pin(pin: str, lengte: int | None = None) -> bool:
    """Check of een string alleen cijfers bevat, en (optioneel) exacte lengte."""
    if not isinstance(pin, str):
        return False
    if not pin.isdigit():
        return False
    if lengte is not None and len(pin) != lengte:
        return False
    return True

def lees_pins_wordlist(pad: str | Path) -> list[str]:
    """
    Lees een wordlist met PINs.
    Verwacht: 1 PIN per regel, alleen cijfers.
    Lege regels en commentaar (# ...) worden genegeerd.
    """
    p = Path(pad)
    if not p.exists():
        raise FileNotFoundError(f"Bestand bestaat niet: {p}")
    regels = p.read_text(encoding="utf-8").splitlines()

    pins: list[str] = []
    for r in regels:
        r = r.strip()
        if not r or r.startswith("#"):
            continue
        if not r.isdigit():
            raise ValueError(f"Ongeldige regel in wordlist (geen cijfers): {r!r}")
        pins.append(r)
    return pins

def filter_op_lengte(pins: Iterable[str], lengte: int) -> list[str]:
    """Filter een lijst pins op exacte lengte."""
    if not isinstance(lengte, int) or lengte <= 0:
        raise ValueError("lengte moet een positief geheel getal zijn")
    uit: list[str] = []
    for p in pins:
        if is_pin(p, lengte):
            uit.append(p)
    return uit

def tel_frequenties(pins: Iterable[str]) -> dict[str, int]:
    """Tel hoe vaak elke PIN voorkomt."""
    freq: dict[str, int] = {}
    for p in pins:
        if not isinstance(p, str) or not p.isdigit():
            continue
        freq[p] = freq.get(p, 0) + 1
    return freq

def sorteerde_pins_op_frequentie(pins: Iterable[str]) -> list[str]:
    """
    Geeft unieke PINs terug, gesorteerd op:
    - hoogste frequentie eerst
    - daarna numeriek oplopend (voor determinisme)
    """
    freq = tel_frequenties(pins)
    return sorted(freq.keys(), key=lambda k: (-freq[k], int(k)))

def wacht(seconden: float) -> None:
    """Wacht een gegeven aantal seconden (kan ook 0 of negatief zijn)."""
    if not isinstance(seconden, (int, float)):
        raise TypeError("seconden moet een getal zijn")
    if seconden > 0:
        time.sleep(seconden)

DATA_DIR = Path(__file__).resolve().parent / "data"

def laad_wordlist(lengte: int) -> list[str]:
    """Laad pins.txt en filter op lengte."""
    pins = lees_pins_wordlist(DATA_DIR / "pins.txt")
    return filter_op_lengte(pins, lengte)

def laad_leak_sample(lengte: int) -> list[str]:
    """Laad leak_sample.txt en filter op lengte."""
    pins = lees_pins_wordlist(DATA_DIR / "leak_sample.txt")
    return filter_op_lengte(pins, lengte)