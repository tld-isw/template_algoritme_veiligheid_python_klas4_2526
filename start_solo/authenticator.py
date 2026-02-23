import random

def genereer_2fa_code(digits: int = 6) -> str:
    """
    Genereert een random 2FA-code met het opgegeven aantal cijfers.
     - digits=6 -> 000000 t/m 999999
     - digits=4 -> 0000 t/m 9999
     - etc.
    """
    return str(random.randrange(0, 10**digits)).zfill(digits)

def random_gok(digits: int = 6) -> str:
    """
    Doe een random gok voor een 2FA-code met het opgegeven aantal cijfers.
    """
    return str(random.randrange(0, 10**digits)).zfill(digits)

def bruteforce_gok(digits: int, poging: int) -> str:
    """
    Doe een bruteforce-gok voor een 2FA-code met het opgegeven aantal cijfers.
    Poging 0 -> 000000
    Poging 1 -> 000001
    enz.
    """
    return str(poging).zfill(digits)

def verifieer_code(echte_code: str, gok_code: str) -> bool:
    """
    Vergelijk de echte code met de gok-code en geef True terug als ze overeenkomen.
    """
    return gok_code == echte_code