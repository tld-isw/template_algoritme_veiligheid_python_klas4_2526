import pytest

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent))


from app import (
    genereer_salt,
    combineer_salt_en_wachtwoord,
    maak_salted_hash,
    maak_gebruiker_record,
    controleer_wachtwoord,
)

from util import hash_sha256


# -----------------------------
# Basiskwaliteit: salt
# -----------------------------

@pytest.mark.parametrize("lengte", [1, 2, 8, 16, 32])
def test_genereer_salt_lengte(lengte):
    s = genereer_salt(lengte)
    assert isinstance(s, str)
    assert len(s) == lengte


@pytest.mark.parametrize("lengte", [0, -1, -10])
def test_genereer_salt_ongeldig(lengte):
    with pytest.raises(ValueError):
        genereer_salt(lengte)


def test_genereer_salt_is_niet_constant():
    salts = [genereer_salt(16) for _ in range(20)]
    assert len(set(salts)) > 1


def test_genereer_salt_niet_whitespace_only():
    s = genereer_salt(16)
    assert s.strip() != ""


# -----------------------------
# Combineer: simpele regels
# -----------------------------

def test_combineer_deterministisch():
    a = combineer_salt_en_wachtwoord("SALT", "PW")
    b = combineer_salt_en_wachtwoord("SALT", "PW")
    assert a == b


def test_combineer_reageert_op_beide_inputs():
    base = combineer_salt_en_wachtwoord("SALT", "123456")
    assert base != combineer_salt_en_wachtwoord("SALT2", "123456")
    assert base != combineer_salt_en_wachtwoord("SALT", "654321")


def test_combineer_lege_salt_valueerror():
    with pytest.raises(ValueError):
        combineer_salt_en_wachtwoord("", "pw")


# -----------------------------
# Salted hash: klopt met util en combineer
# -----------------------------

def test_maak_salted_hash_is_sha256_van_combineer():
    salt = "SALT"
    pw = "123456"
    expected = hash_sha256(combineer_salt_en_wachtwoord(salt, pw))
    got = maak_salted_hash(pw, salt)
    assert got == expected


def test_maak_salted_hash_verschilt_bij_andere_salt():
    assert maak_salted_hash("123456", "SALT1") != maak_salted_hash("123456", "SALT2")


# -----------------------------
# Record: structuur en interne consistentie
# -----------------------------

def test_record_structuur():
    rec = maak_gebruiker_record("Alice", "123456")
    assert isinstance(rec, dict)
    assert set(rec.keys()) == {"gebruikersnaam", "salt", "hash"}
    assert rec["gebruikersnaam"] == "Alice"
    assert isinstance(rec["salt"], str) and len(rec["salt"]) >= 1
    assert isinstance(rec["hash"], str) and len(rec["hash"]) == 64


def test_record_hash_klopt_met_record_salt():
    rec = maak_gebruiker_record("Alice", "123456")
    assert rec["hash"] == maak_salted_hash("123456", rec["salt"])


def test_alice_en_bob_zelfde_wachtwoord_meestal_niet_dezelfde_hash():
    # Niet super-streng (random kan theoretisch botsen),
    # maar in de praktijk moet dit altijd slagen als salt niet constant is.
    alice = maak_gebruiker_record("Alice", "123456")
    bob = maak_gebruiker_record("Bob", "123456")
    assert alice["hash"] != bob["hash"] or alice["salt"] != bob["salt"]


# -----------------------------
# Login: functioneel gedrag
# -----------------------------

def test_controleer_wachtwoord_true_false():
    rec = maak_gebruiker_record("Alice", "123456")
    assert controleer_wachtwoord(rec, "123456") is True
    assert controleer_wachtwoord(rec, "000000") is False


def test_controleer_wachtwoord_exact_match_geen_strip():
    rec2 = maak_gebruiker_record("Space", " 123456 ")
    assert controleer_wachtwoord(rec2, " 123456 ") is True
    assert controleer_wachtwoord(rec2, "123456") is False