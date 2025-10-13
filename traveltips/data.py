"""Static travel data used by the recommender."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass(frozen=True)
class DestinationTips:
    """Container for travel guidance about a destination."""

    best_time: str
    top_experiences: List[str]
    local_tips: List[str]


DESTINATIONS: Dict[str, DestinationTips] = {
    "barcelona": DestinationTips(
        best_time="April to June or September to October for great weather without peak crowds.",
        top_experiences=[
            "Stroll down the Passeig de Gràcia to see Gaudí's Casa Batlló and La Pedrera.",
            "Buy skip-the-line tickets for the Sagrada Família at least a day in advance.",
            "Reserve sunset tapas at a neighborhood bar in Gràcia or Poble Sec.",
        ],
        local_tips=[
            "Lunch is eaten late—many restaurants don't open for dinner until 8pm.",
            "Use the T-casual metro card for 10 discounted rides around the city.",
            "Visit popular beaches on weekday mornings to avoid cruise ship crowds.",
        ],
    ),
    "lisbon": DestinationTips(
        best_time="March to May for mild temperatures or September to October after the summer rush.",
        top_experiences=[
            "Ride the historic Tram 28 early in the morning to avoid long lines.",
            "Book a day trip to Sintra and arrive when the palaces open.",
            "Catch sunset at Miradouro da Senhora do Monte with a takeaway pastel de nata.",
        ],
        local_tips=[
            "Lisbon's hills are steep—pack comfortable shoes and use elevators where available.",
            "Buy a Viva Viagem card for buses, trams, ferries, and the metro.",
            "Seafood restaurants often close on Mondays, so plan accordingly.",
        ],
    ),
    "new york": DestinationTips(
        best_time="Late April to early June or September to early November for pleasant weather.",
        top_experiences=[
            "Reserve free timed tickets to the High Line or Summit One Vanderbilt ahead of time.",
            "Catch a Broadway show by entering the daily digital lottery the morning of the performance.",
            "Explore the food scene in Queens—Jackson Heights and Flushing are musts for adventurous eaters.",
        ],
        local_tips=[
            "Load a MetroCard or use OMNY contactless payments for subway rides.",
            "Museums often have free or pay-what-you-wish evenings—check their calendars before you go.",
            "Always check alternate-side parking if you're renting a car.",
        ],
    ),
    "tokyo": DestinationTips(
        best_time="Late March to April for cherry blossoms or October to November for autumn colors.",
        top_experiences=[
            "Buy a Suica or Pasmo card on arrival to breeze through public transit.",
            "Reserve a spot at teamLab Planets weeks in advance—it sells out quickly.",
            "Take a day trip to Nikko or Hakone for hot springs and mountain scenery.",
        ],
        local_tips=[
            "Most restaurants prefer cash or IC cards—ATMs at 7-Eleven accept international cards.",
            "Stay quiet on trains; phone calls are considered impolite inside carriages.",
            "Convenience stores are your friend for quick, tasty meals on the go.",
        ],
    ),
    "vancouver": DestinationTips(
        best_time="June to September for outdoor adventures or December to February for skiing at nearby mountains.",
        top_experiences=[
            "Rent a bike to explore the Stanley Park Seawall early in the morning.",
            "Take the SeaBus to Lonsdale Quay for a less touristy food market experience.",
            "Plan a day trip to Whistler via shuttle to skip parking hassles.",
        ],
        local_tips=[
            "Pack a light rain jacket—weather shifts quickly even in summer.",
            "Tap your contactless credit card on SkyTrain and buses; fares cap daily.",
            "Check the aurora forecast in winter—Northern Lights occasionally appear.",
        ],
    ),
}


def normalized_key(query: str) -> str:
    """Return a normalized lookup key for the provided query string."""

    return query.strip().lower()
