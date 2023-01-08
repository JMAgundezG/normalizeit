"""Loaders for the project"""

import json
from typing import Optional


def load_scheme_file(scheme_path: str, error_message: Optional[str] = "") -> dict:
    """Load an scheme file using the path"""
    try:
        with open(scheme_path, "r", encoding="utf-8") as scheme_file:
            return json.loads(scheme_file.read())
    except Exception as exc:
        raise Exception(f"[ERROR] {error_message} not found") from exc
