import sys
from pathlib import Path
import pytest

# Add the project root to the Python path to allow for module imports
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.concierge_logic import get_concierge_response, KNOWLEDGE_BASE

def test_initial_greeting_response():
    """
    Tests that an empty query returns the initial welcome message and tip.
    """
    response, tip = get_concierge_response("")
    assert "Welcome to Ahmed’s AI Concierge™" in response
    assert isinstance(tip, str) and len(tip) > 0

def test_burj_khalifa_query():
    """
    Tests the response for a query about the Burj Khalifa.
    """
    response, tip = get_concierge_response("tell me about burj khalifa")
    assert response == KNOWLEDGE_BASE["burj khalifa"]["response"]
    assert tip == KNOWLEDGE_BASE["burj khalifa"]["tip"]

def test_desert_safari_query():
    """
    Tests the response for a query about the desert safari.
    """
    response, tip = get_concierge_response("what is a desert safari like?")
    assert response == KNOWLEDGE_BASE["desert safari"]["response"]
    assert tip == KNOWLEDGE_BASE["desert safari"]["tip"]

def test_default_response_for_unknown_query():
    """
    Tests that an unknown query returns the default response and tip.
    """
    response, tip = get_concierge_response("tell me about the food")
    assert response == KNOWLEDGE_BASE["default"]["response"]
    assert tip == KNOWLEDGE_BASE["default"]["tip"]