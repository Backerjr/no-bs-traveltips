"""Simple travel tip recommendation logic."""

from __future__ import annotations

from typing import Iterable, List, Optional

from .data import DESTINATIONS, DestinationTips, normalized_key


class UnknownDestinationError(ValueError):
    """Raised when the user asks for a destination that we do not know."""


class TravelTipsRecommender:
    """Return concise, actionable travel advice for supported destinations."""

    def __init__(self, destinations: Optional[dict[str, DestinationTips]] = None) -> None:
        self._destinations = destinations or DESTINATIONS

    def destinations(self) -> List[str]:
        """Return the list of supported destination names sorted alphabetically."""

        return sorted(self._destinations)

    def get_tips(self, query: str) -> DestinationTips:
        """Look up a destination and return its associated travel tips.

        Raises
        ------
        UnknownDestinationError
            If the destination does not exist in our dataset.
        """

        key = normalized_key(query)
        try:
            return self._destinations[key]
        except KeyError as exc:  # pragma: no cover - defensive branch
            raise UnknownDestinationError(f"No travel tips are available for '{query}'.") from exc

    def format_tips(self, tips: DestinationTips) -> str:
        """Return a human-readable string containing the travel tips."""

        lines: List[str] = ["Best time to visit: " + tips.best_time, "", "Top experiences:"]
        lines.extend(f"  • {experience}" for experience in tips.top_experiences)
        lines.extend(["", "Local tips:"])
        lines.extend(f"  • {tip}" for tip in tips.local_tips)
        return "\n".join(lines)

    def describe_destination(self, query: str) -> str:
        """Shortcut that combines :meth:`get_tips` and :meth:`format_tips`."""

        return self.format_tips(self.get_tips(query))

    def search(self, keyword: str) -> Iterable[str]:
        """Return destinations whose name contains the provided keyword."""

        norm = normalized_key(keyword)
        for name in self.destinations():
            if norm in name:
                yield name
