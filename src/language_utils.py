"""Utility helpers for language handling."""

LANGUAGE_LABEL_TO_CODE = {
    "English": "en",
    "en": "en",
    "Arabic": "ar",
    "العربية": "ar",
    "ar": "ar",
}


def normalize_language_selection(language: str) -> str:
    """Return the two-letter language code for a UI selection."""
    return LANGUAGE_LABEL_TO_CODE.get(language, "en")
