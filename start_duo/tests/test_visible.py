import sys
from pathlib import Path
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app import crack_bruteforce, crack_dictionary, crack_slim, laad_wordlist

def test_bruteforce_vindt_pin():
    r = crack_bruteforce("0003", 4)
    assert r["gevonden"] is True
    assert r["pin"] == "0003"
    assert r["pogingen"] == 4  # 0000,0001,0002,0003

def test_dictionary_vindt_pin_met_wordlist():
    wl = ["9999", "1234", "0000"]
    r = crack_dictionary("1234", wl)
    assert r["gevonden"] is True
    assert r["pin"] == "1234"
    assert r["methode"] == "dictionary"
    assert r["pogingen"] == 2

def test_dictionary_slaat_foute_lengtes_over():
    wl = ["123", "12", "12345", "0000"]
    r = crack_dictionary("0000", wl)
    assert r["gevonden"] is True
    assert r["pogingen"] == 1  # alleen 0000 telt mee

def test_dictionary_niet_gevonden():
    wl = ["1111", "2222"]
    r = crack_dictionary("0000", wl)
    assert r["gevonden"] is False
    assert r["pin"] is None
    assert r["pogingen"] == 2

def test_slim_is_correct_en_vindt_pin():
    r = crack_slim("1234", 4)
    assert r["gevonden"] is True
    assert r["pin"] == "1234"
    assert r["methode"] == "slim"
    assert isinstance(r["pogingen"], int) and r["pogingen"] >= 1

@pytest.mark.parametrize("secret", ["0000", "9999", "0420", "6969", "6767", "1234"])
def test_slim_altijd_correct_met_fallback(secret):
    # Ook als secret niet 'menselijk' is, moet hij hem uiteindelijk vinden.
    r = crack_slim(secret, 4)
    assert r["gevonden"] is True
    assert r["pin"] == secret
    assert r["methode"] == "slim"
    assert isinstance(r["pogingen"], int) and r["pogingen"] >= 1 # geen pogingen mag ook niet, dat zou gek zijn
