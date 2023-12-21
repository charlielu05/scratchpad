import os
from dataclasses import dataclass
from typing import List, Set
import re
from pathlib import Path
from collections import defaultdict


@dataclass
class Card:
    card_id: str
    winning_numbers: Set[int]
    numbers: Set[int]


def calculate_score(wins: int) -> int:
    score = 1 if wins > 0 else 0
    for _ in range(wins - 1):
        score *= 2
    return score


if __name__ == "__main__":
    # two lists of numbers separated by vertical bar (|) character
    # a list of winning numbers and a list of numbers you have
    # find the number of winning numbers you have
    # one point for the first winning number, double the value for each subsequent winning number
    INPUT_FILENAME = Path(__file__).parent / "full_input.txt"

    # open text file
    with open(INPUT_FILENAME, encoding="utf-8") as file:
        test_input = file.read().splitlines()

    # create a list of cards
    cards: List[Card] = []
    for line in test_input:
        card_id, winning_numbers, numbers = re.split(r":\s|\s\|\s", line)
        winning_numbers = set(map(int, winning_numbers.split()))
        numbers = set(map(int, numbers.split()))
        # create a card
        card = Card(card_id=card_id, winning_numbers=winning_numbers, numbers=numbers)
        # add the card to the list
        cards.append(card)

    # find the number of winning numbers for each card
    wins = [(card.numbers.intersection(card.winning_numbers)) for card in cards]

    # calculate the score for each card
    scores = [calculate_score(len(win)) for win in wins]
    # print(f"total score: {sum(scores)}")

    # part two
    # calculate how many scratch cards you end up with
    N = defaultdict(int)
    for i, win in enumerate(wins):
        N[i] += 1
        for j in range(len(win)):
            N[i + 1 + j] += N[i]
