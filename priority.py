def normalize_priority(value):
    if value not in ("low", "normal", "high"):
        raise ValueError("Invalid priority")
    return value
