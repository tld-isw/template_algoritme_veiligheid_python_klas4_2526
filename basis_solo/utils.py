# utils.py
def is_truthy(value) -> bool:
    """Robuuste check voor boolean-ish waarden uit JSON (true/false/0/1/'yes' etc)."""
    if isinstance(value, bool):
        return value
    if value is None:
        return False
    if isinstance(value, (int, float)):
        return value != 0
    if isinstance(value, str):
        return value.strip().lower() in {"1","true","yes","ja","y","on"}
    return bool(value)


def training_level(value) -> int:
    """
    Zet security_training om naar een niveau:
    - false / ontbreekt -> 0
    - "yearly" -> 1
    - "twice_yearly" -> 2
    """
    if value is False or value is None:
        return 0
    if isinstance(value, str):
        v = value.strip().lower()
        if v == "yearly":
            return 1
        if v == "twice_yearly":
            return 2
    return 0
