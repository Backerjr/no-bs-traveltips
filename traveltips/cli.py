"""Command line entry point for the travel tips recommender."""

from __future__ import annotations

import argparse
from typing import Iterable

from .recommender import TravelTipsRecommender, UnknownDestinationError


def _format_list(title: str, values: Iterable[str]) -> str:
    items = "\n".join(f"  • {value.title()}" for value in values)
    return f"{title}\n{items}"


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Get no-nonsense travel recommendations.")
    parser.add_argument(
        "destination",
        nargs="?",
        help="Destination to look up. If omitted, prints the list of supported destinations.",
    )
    parser.add_argument(
        "--search",
        metavar="KEYWORD",
        help="Show destinations containing the provided keyword.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = create_parser()
    args = parser.parse_args(argv)

    recommender = TravelTipsRecommender()

    if args.search:
        matches = list(recommender.search(args.search))
        if matches:
            print(_format_list("Matching destinations:", matches))
            return 0
        print("No destinations matched your search.")
        return 1

    if args.destination:
        try:
            print(recommender.describe_destination(args.destination))
        except UnknownDestinationError as exc:
            parser.error(str(exc))
        return 0

    print(_format_list("Supported destinations:", recommender.destinations()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
