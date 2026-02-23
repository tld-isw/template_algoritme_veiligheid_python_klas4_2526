from utils import krijg_tijd, bereken_seconden, wacht
from authenticator import (
    genereer_2fa_code,
    random_gok,
    bruteforce_gok,
    verifieer_code
)

DIGITS = 6 # Aantal cijfers in de 2FA-code
VENSTER = 30 # Aantal seconden voordat de code verloopt
RUNS = 100 # Aantal runs van het experiment

DELAY = 0 # Aantal seconden om te wachten tussen pogingen
STRATEGIE = "bruteforce"

SUCCESS = "SUCCESS"
FAIL = "FAIL"


def maak_log(run_nr: int, status: str, attempts: int, tijd: float) -> str:
    """Maak een logregel met de volgende info:
    - run_nr (1 t/m RUNS)
    - status (SUCCESS of FAIL)
    - attempts (aantal pogingen)
    - tijd (aantal seconden, afgerond op 2 decimalen)
    Formaat: "Run 1: SUCCESS na 123 pogingen in 12.34 seconden"
    """
    # TODO
    pass


def update_tellers(status: str, success: int, fail: int) -> tuple[int, int]:
    """
    Update de success- en fail-tellers op basis van de status.
    - Als status SUCCESS is, verhoog success met 1
    - Als status FAIL is, verhoog fail met 1
    Geef de nieuwe waarden van success en fail terug als tuple (success, fail)
    """
    # TODO
    return success, fail


def doe_run(run_nr: int):
    """Voer één run uit van het 2FA-kraken."""
    echte_code = genereer_2fa_code(DIGITS)
    start = krijg_tijd()
    attempts = 0

    while True:
        if bereken_seconden(start, krijg_tijd()) > VENSTER:
            return FAIL, attempts, bereken_seconden(start, krijg_tijd())
       
        gok = maak_gok(attempts)
        attempts += 1

        if verifieer_code(echte_code, gok):
            return SUCCESS, attempts, bereken_seconden(start, krijg_tijd())

def maak_gok(poging: int) -> str:
    """
    Maak een gok op basis van de gekozen strategie.
    """
    if STRATEGIE == "random":
        return random_gok(DIGITS)
    if STRATEGIE == "bruteforce":
        return bruteforce_gok(DIGITS, poging)
    raise ValueError("Onbekende strategie")


def main():
    """Voer RUNS aantal runs uit en houd bij hoeveel succesvol waren."""
    success = 0
    fail = 0
    logs = []

    for run in range(1, RUNS + 1):
        print("running run", run)
        status, attempts, tijd = doe_run(run)
        success, fail = update_tellers(status, success, fail)

    # TODO: Toon de logs en de stats

if __name__ == "__main__":
    main()