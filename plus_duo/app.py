"""
Bestand voor de duo-opdracht. Hierin moeten functies komen die in de solo-opdracht ook al gemaakt zijn, maar nu moeten ze samenwerken.

Namen: ....

"""


from __future__ import annotations
from util import huidige_tijd, bereken_seconden, normaliseer_tekst, naar_getal, naar_teken, modulo_alfabet


def _check_sleutel(sleutel: str) -> str:
    """
    Controleer dat sleutel:
    - een string is
    - niet leeg is
    - alleen letters bevat
    Retourneer sleutel in originele vorm.
    """
    raise NotImplementedError


def _herhaal_sleutel(tekst: str, sleutel: str) -> str:
    """
    Herhaal de sleutel zodat hij even lang wordt als de tekst,
    maar alleen voor letters (niet-letters tellen niet mee).
    """
    raise NotImplementedError


def encrypt_vigenere(tekst: str, sleutel: str) -> str:
    """
    Versleutel de tekst met de Vigenère-cijfer.
    - gebruik de herhaalde sleutel
    - gebruik de hulp functies uit util.py

    Niet-letters blijven gelijk.
    """
    raise NotImplementedError


def decrypt_vigenere(tekst: str, sleutel: str) -> str:
    """
    Ontsleutel de tekst met de Vigenère-cijfer.
    - gebruik de herhaalde sleutel
    - gebruik de hulp functies uit util.py
    """
    raise NotImplementedError


# Demo
if __name__ == "__main__":

    msg = "Hallo wereld!"
    key = "KEY"
    print("sleutel:", key, _check_sleutel(key))
    print("tekst  :", msg, "de sleutel wordt herhaald tot", _herhaal_sleutel(msg, key))

    huidige_tijd = huidige_tijd()
    c = encrypt_vigenere(msg, key)
    enc_tijd = bereken_seconden(huidige_tijd, huidige_tijd())
    
    huidige_tijd = huidige_tijd()
    p = decrypt_vigenere(c, key)
    dec_tijd = bereken_seconden(huidige_tijd, huidige_tijd())

    print("Origineel:", msg)
    print("Cipher   :", c)
    print("Terug    :", p)
    print(f"Encryptie duurde {enc_tijd} seconden")
    print(f"Decryptie duurde {dec_tijd} seconden")


