# app.py
"""
Salting the hashes (Plus - Solo)

Jij krijgt de hashfunctie (SHA-256) cadeau in util.py.
Jij maakt zelf de salting: hoe je salt maakt, hoe je combineert, en hoe je controleert.

De tests verwachten dat onderstaande functies bestaan.
"""

from util import hash_sha256

def genereer_salt(lengte: int = 16) -> str:
    """
    Maak en return een salt (string).
    Eisen (minimaal, voor tests):
    - resultaat is een str
    - lengte is >= 1
    - bij verschillende aanroepen kan hij verschillen (mag random zijn)
    """
    raise NotImplementedError


def combineer_salt_en_wachtwoord(salt: str, wachtwoord: str) -> str:
    """
    Combineer salt en wachtwoord tot 1 tekst die gehasht kan worden.
    Let op dat de salt niet leeg mag zijn.
    """
    raise NotImplementedError


def maak_salted_hash(wachtwoord: str, salt: str) -> str:
    """
    Maak een salted hash (hex string) op basis van wachtwoord en salt.
    Moet gebruik maken van util.hash_sha256(...)
    """
    raise NotImplementedError


def maak_gebruiker_record(gebruikersnaam: str, wachtwoord: str) -> dict:
    """
    Maak een 'record' dat je in een database zou kunnen opslaan.
    Voorbeeld van een record 
    {
        "gebruikersnaam": "Alice",
        "salt": "random_salt",
        "hash": "asf212...1231aa"
    }
    Verwachte keys:
      - 'gebruikersnaam'
      - 'salt'
      - 'hash'
    """
    raise NotImplementedError


def controleer_wachtwoord(record: dict, poging: str) -> bool:
    """
    Check of een poging klopt bij het record.
    Je kunt gegevens uit de record halen bijv met record["salt"]. 
    True als correct, anders False.
    """
    raise NotImplementedError



# kleine demo 
if __name__ == "__main__":
    salt1 = genereer_salt(12)
    salt2 = genereer_salt(12)
    print("Salt 1:", salt1)
    print("Salt 2:", salt2)

    print("Combineer voorbeeld:", combineer_salt_en_wachtwoord("SALT", "123456"))  

    print("Salted hash voorbeeld:", maak_salted_hash("123456", "SALT"))

    alice = maak_gebruiker_record("Alice", "123456")
    bob = maak_gebruiker_record("Bob", "123456")

    print("Alice record:", alice)
    print("Bob record:", bob)

    print("Alice login goed?", controleer_wachtwoord(alice, "123456"))
    print("Alice login fout?", controleer_wachtwoord(alice, "000000"))