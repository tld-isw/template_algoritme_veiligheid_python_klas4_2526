# src/utils.py
from urllib.parse import urlparse

def domain_from_email(addr: str) -> str:
    """Haal domein uit e-mailadres."""
    if "@" not in addr:
        return ""
    return addr.split("@", 1)[1].strip().lower()

def domain_from_url(url: str) -> str:
    """Haal domein uit URL."""
    try:
        netloc = urlparse(url).netloc.lower()
        return netloc.split(":")[0]
    except Exception:
        return ""

def has_executable_attachment(attachments: list[str]) -> bool:
    """
    Checked of een bestand uit de attatchements een executable is. 
    """
    for a in attachments:
        if str(a).lower().endswith(".exe"):
            return True
    return False

def contains_any(text: str, words: list[str]) -> bool:
    """
    Checked of de text een van de wooorden uit words bevat. 
    """
    text = text.lower()
    return any(w in text for w in words)