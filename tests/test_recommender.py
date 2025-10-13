from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from traveltips.recommender import TravelTipsRecommender, UnknownDestinationError


def test_list_destinations_sorted():
    recommender = TravelTipsRecommender()
    assert recommender.destinations() == sorted(recommender.destinations())


def test_get_tips_known_destination():
    recommender = TravelTipsRecommender()
    tips = recommender.get_tips("Tokyo")
    assert "cherry blossoms" in tips.best_time.lower()
    assert len(tips.top_experiences) == 3


def test_get_tips_unknown_destination():
    recommender = TravelTipsRecommender()
    try:
        recommender.get_tips("Atlantis")
    except UnknownDestinationError as exc:
        assert "Atlantis" in str(exc)
    else:
        raise AssertionError("Expected an UnknownDestinationError to be raised")


def test_search_matches_partial_name():
    recommender = TravelTipsRecommender()
    results = list(recommender.search("yo"))
    assert "tokyo" in results
    assert all("yo" in name for name in results)
