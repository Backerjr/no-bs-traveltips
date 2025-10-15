import sys
from pathlib import Path
import pytest

# Add the project root to the Python path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.concierge_logic import greet

def test_greet_with_name():
    """
    Tests the greet function with a name provided.
    """
    assert greet("Jules") == "Welcome to Dubai, Jules! How may I assist you today?"

def test_greet_without_name():
    """
    Tests the greet function without a name.
    """
    assert greet("") == "Welcome to Dubai! How may I assist you today?"

def test_greet_with_none():
    """
    Tests the greet function with None as the input.
    """
    assert greet(None) == "Welcome to Dubai! How may I assist you today?"