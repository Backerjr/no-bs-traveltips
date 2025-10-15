import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.language_utils import normalize_language_selection


def test_normalize_language_selection_defaults_to_english():
    assert normalize_language_selection("English") == "en"
    assert normalize_language_selection("en") == "en"
    assert normalize_language_selection("unknown") == "en"


def test_normalize_language_selection_accepts_arabic_labels():
    assert normalize_language_selection("Arabic") == "ar"
    assert normalize_language_selection("العربية") == "ar"
    assert normalize_language_selection("ar") == "ar"
