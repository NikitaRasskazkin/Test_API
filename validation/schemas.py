CURRENCY_POST = {
    "type": "object",
    "properties": {
        "from": {"type": "string"},
        "to": {"type": "string"},
        "value": {"type": "number"}
    },
    "required": ["from", "to", "value"]
}

CURRENCY_PUT = {
    "type": "object",
    "properties": {
        "currency": {"type": "string"},
        "base": {"type": "string"},
        "value": {"type": "number"}
    },
    "required": ["currency", "base", "value"]
}
