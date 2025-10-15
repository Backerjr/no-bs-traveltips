import sys
from pathlib import Path
import pytest

# Add the project root to the Python path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.concierge_logic import get_concierge_response, KNOWLEDGE_BASE

# --- English Tests ---

def test_initial_greeting_en():
    response, tip, tip_title, booking_info = get_concierge_response("", language="en")
    assert response == KNOWLEDGE_BASE["greeting"]["en"]["response"]
    assert tip == KNOWLEDGE_BASE["greeting"]["en"]["tip"]
    assert tip_title == "Ahmed's Tip™"
    assert booking_info is None # No booking info on initial greeting

def test_burj_khalifa_query_en():
    response, tip, tip_title, booking_info = get_concierge_response("tell me about burj khalifa", language="en")
    assert response == KNOWLEDGE_BASE["burj khalifa"]["en"]["response"]
    assert tip == KNOWLEDGE_BASE["burj khalifa"]["en"]["tip"]
    assert booking_info == KNOWLEDGE_BASE["booking_prompt"]["en"]

def test_desert_safari_query_en():
    response, tip, tip_title, booking_info = get_concierge_response("what is a desert safari like?", language="en")
    assert response == KNOWLEDGE_BASE["desert safari"]["en"]["response"]
    assert tip == KNOWLEDGE_BASE["desert safari"]["en"]["tip"]
    assert booking_info is not None

def test_default_response_en():
    response, tip, tip_title, booking_info = get_concierge_response("tell me about the food", language="en")
    assert response == KNOWLEDGE_BASE["default"]["en"]["response"]
    assert tip == KNOWLEDGE_BASE["default"]["en"]["tip"]
    assert booking_info is None # No booking info for default response

# --- Arabic Tests ---

def test_initial_greeting_ar():
    response, tip, tip_title, booking_info = get_concierge_response("", language="ar")
    assert response == KNOWLEDGE_BASE["greeting"]["ar"]["response"]
    assert tip == KNOWLEDGE_BASE["greeting"]["ar"]["tip"]
    assert tip_title == "نصيحة أحمد™"
    assert booking_info is None

def test_burj_khalifa_query_ar_from_en_keyword():
    response, tip, tip_title, booking_info = get_concierge_response("tell me about burj khalifa", language="ar")
    assert response == KNOWLEDGE_BASE["burj khalifa"]["ar"]["response"]
    assert tip == KNOWLEDGE_BASE["burj khalifa"]["ar"]["tip"]
    assert booking_info == KNOWLEDGE_BASE["booking_prompt"]["ar"]

def test_desert_safari_query_ar_from_en_keyword():
    response, tip, tip_title, booking_info = get_concierge_response("what is a desert safari like?", language="ar")
    assert response == KNOWLEDGE_BASE["desert safari"]["ar"]["response"]
    assert tip == KNOWLEDGE_BASE["desert safari"]["ar"]["tip"]
    assert booking_info is not None

def test_default_response_ar():
    response, tip, tip_title, booking_info = get_concierge_response("tell me about the food", language="ar")
    assert response == KNOWLEDGE_BASE["default"]["ar"]["response"]
    assert tip == KNOWLEDGE_BASE["default"]["ar"]["tip"]
    assert booking_info is None