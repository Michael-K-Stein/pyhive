from typing import Any


def get_client_params() -> dict[str, Any]:
    return {
        "username": "michaelks",
        "password": "Password1",
        "hive_url": "https://hive.org",
        "verify": False,
        "timeout": 20,  # Very long timeout so tests do not fail just because the Hive endpoint is slow
    }
