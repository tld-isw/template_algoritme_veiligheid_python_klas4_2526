import pytest
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app import encrypt_vigenere, decrypt_vigenere, _check_sleutel

def test_check_sleutel_valid():
    assert _check_sleutel("KEY") == "KEY"

@pytest.mark.parametrize("sleutel", ["", "123", "K3Y", None])
def test_check_sleutel_invalid(sleutel):
    with pytest.raises((TypeError, ValueError)):
        _check_sleutel(sleutel)  # type: ignore

def test_encrypt_decrypt_roundtrip():
    tekst = "Hallo wereld!"
    sleutel = "KEY"
    c = encrypt_vigenere(tekst, sleutel)
    p = decrypt_vigenere(c, sleutel)
    assert p == tekst

def test_encrypt_hoofdletters():
    assert encrypt_vigenere("ABC", "B") == "BCD"

def test_encrypt_kleine_letters():
    assert encrypt_vigenere("abc", "b") == "bcd"

def test_niet_letters_blijven():
    tekst = "a-b c!"
    c = encrypt_vigenere(tekst, "KEY")
    for i, ch in enumerate(tekst):
        if not ch.isalpha():
            assert c[i] == ch

def test_sleutel_langer_dan_tekst():
    tekst = "HI"
    sleutel = "LONGKEY"
    c = encrypt_vigenere(tekst, sleutel)
    p = decrypt_vigenere(c, sleutel)
    assert p == tekst
