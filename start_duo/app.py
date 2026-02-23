from __future__ import annotations
from pathlib import Path
import random
from typing import Any

from util import huidige_tijd, bereken_seconden, format_pin, lees_pins_wordlist, filter_op_lengte, sorteerde_pins_op_frequentie, laad_leak_sample, laad_wordlist, wacht

DELAY = 0.00001  # vertraging tussen pogingen, in seconden (simuleert tijd voor een poging)

def crack_random(secret: str, lengte: int) -> dict[str, Any]:
    """
    Probeer willekeurige PINs totdat je de secret vindt.
    Retourneert een Result-dict.
    """
    if not isinstance(secret, str):
        raise TypeError("secret moet een string zijn")
    if not isinstance(lengte, int) or lengte <= 0:
        raise ValueError("lengte moet een positief geheel getal zijn")

    start = huidige_tijd()
    pogingen = 0

    while True:
        gok = format_pin(random.randint(0, 10**lengte - 1), lengte)
        pogingen += 1
        wacht(DELAY)
        if gok == secret:
            eind = huidige_tijd()
            return {
                "gevonden": True,
                "pin": gok,
                "pogingen": pogingen,
                "seconden": bereken_seconden(start, eind),
                "methode": "random",
            }

def crack_bruteforce(secret: str, lengte: int) -> dict[str, Any]:
    """
    Probeer alle combinaties van 0..(10**lengte - 1) in oplopende volgorde.
    Retourneert een Result-dict.
    """
    raise NotImplementedError

def crack_dictionary(secret: str, wordlist: list[str]) -> dict[str, Any]:
    """
    Probeer de PINs uit de gegeven wordlist (in volgorde).
    - Stop als je de secret vindt.
    - Als secret niet in de lijst zit, geef gevonden=False terug.

    Let op:
    - wordlist kan ook PINs bevatten met andere lengtes; filter die eruit of sla ze over.
    - Je woordenlijst is nog erg klein, maak hem langer. Zie data/pins.txt
    - tel alleen echte pogingen mee.

    Retourneer een Result-dict met methode="dictionary".
    """
    raise NotImplementedError

def crack_slim(secret: str, lengte: int) -> dict[str, Any]:
    """
    Ontwerp jullie eigen slimme strategie, je kunt bijvoorbeeld gebruik maken van leak_sample.

    Richtlijnen:
    1) Je bedenkt je eigen algoritme, en werkt deze zelf uit. Je mag ook hulpfuncties maken en gebruiken.
    2) Zorg dat je ALTIJD eindigt met een correct antwoord.

    Retourneer een Result-dict met methode="slim".
    """
    raise NotImplementedError

def run_demo() -> None:
    """Kleine demo om te zien wat er gebeurt."""
    lengte = 4
    secret = "1234"
    wl = laad_wordlist(lengte)

    print("=== DEMO ===")
    print("Secret:", secret)

    r0 = crack_random(secret, lengte)
    print("Random:", r0)

    try:
        r1 = crack_bruteforce(secret, lengte)
        print("Bruteforce:", r1)
    except NotImplementedError:
        print("Bruteforce: nog niet gemaakt")

    try:
        r2 = crack_dictionary(secret, wl)
        print("Dictionary:", r2)
    except NotImplementedError:
        print("Dictionary: nog niet gemaakt")

    try:
        r3 = crack_slim(secret, lengte)
        print("Slim:", r3)
    except NotImplementedError:
        print("Slim: nog niet gemaakt")

def test(n: int = 10, length: int = 4) -> None:
    """Voer n tests uit met willekeurige secrets van gegeven lengte."""
    results = []
    for i in range(n):
        secret = format_pin(random.randint(0, 10**length - 1), length)
        results.append((secret, crack_random(secret, len(secret))))
        try:
            results.append((secret, crack_slim(secret, length)))
        except NotImplementedError:
            pass
        try:
            results.append((secret, crack_bruteforce(secret, length)))
        except NotImplementedError:
            pass
        try:
            results.append((secret, crack_dictionary(secret, laad_wordlist(length))))
        except NotImplementedError:
            pass

    calc(results)

def test_gegeven_lijst(test: list[str]) -> None:
    """
    Voer een test uit met de gegeven lijst van secrets.
    Elke secret in de lijst wordt getest met alle methodes (random, bruteforce, dictionary, slim).
    Print de resultaten in een leesbaar formaat, bijvoorbeeld:
     - status (SUCCESS of FAIL)
     - attempts (aantal pogingen)
     - tijd (aantal seconden, afgerond op 2 decimalen)
    Formaat: "Run 1: SUCCESS na 123 pogingen in 12.34 seconden"
    """
    results = []
    for i, secret in enumerate(test):
        results.append((secret, crack_random(secret, len(secret))))
        length = len(secret)
        try:
            results.append((secret, crack_slim(secret, length)))
        except NotImplementedError:
            pass
        try:
            results.append((secret, crack_bruteforce(secret, length)))
        except NotImplementedError:
            pass
        try:
            results.append((secret, crack_dictionary(secret, laad_wordlist(length))))
        except NotImplementedError:
            pass

    calc(results)

def calc(results: list[tuple[str, dict[str, Any]]]) -> None:
    """
    Bereken en print de stats van de testresultaten.
    """
    slim = [r for s, r in results if r["methode"] == "slim"]
    random = [r for s, r in results if r["methode"] == "random"]
    bruteforce = [r for s, r in results if r["methode"] == "bruteforce"]
    dictionary = [r for s, r in results if r["methode"] == "dictionary"]    

    print("=== STATS ===")
    show_results("Random\t", random)
    show_results("Bruteforce\t", bruteforce)
    show_results("Dictionary\t", dictionary)
    show_results("Slim\t", slim)

def show_results(alg: str, resultaten: list[dict[str, Any]]) -> None:
    """Print de resultaten van een test in een leesbaar formaat."""
    print(f"{alg}: \t {len(resultaten)} tests, gemiddeld {sum(r['pogingen'] for r in resultaten) / len(resultaten) if resultaten else 0:.1f} pogingen\t gemiddeld {sum(r['seconden'] for r in resultaten) / len(resultaten) if resultaten else 0:.2f} seconden\t successrate van {sum(1 for r in resultaten if r['gevonden']) / len(resultaten) * 100 if resultaten else 0:.1f}%")


if __name__ == "__main__":
    run_demo()
    # Andere opties voor testen:
    # test_gegeven_lijst(["0000", "9999", "1234"])
    test(n=100, length=4)
