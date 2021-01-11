post_schema = {
        "required": ["from", "to", "value"],
        "properties": {
            "from": {"type": "string", "minLength": 3, "maxLength": 3},
            "to": {"type": "string", "minLength": 3, "maxLength": 3},
            "value": {}
        }
    }
