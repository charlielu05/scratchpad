from pathlib import Path
from dataclasses import dataclass
from typing import List

DECK = "23456789TJQKA"
DECK_PART_TWO = "J23456789TQKA"


@dataclass
class Card:
    card: str
    card_value: int


@dataclass
class Hand:
    hand: List[Card]
    bid: int
    hand_counts = None
    hand_type = None

    def __post_init__(self):
        self.hand_counts = self.count_hand()
        self.hand_type = self.type_of_hand()

    def __lt__(self, other):
        if self.rank_hand() < other.rank_hand():
            return True
        elif self.rank_hand() == other.rank_hand():
            for i in range(len(self.hand)):
                if self.hand[i].card_value < other.hand[i].card_value:
                    return True
                elif self.hand[i].card_value > other.hand[i].card_value:
                    return False
        else:
            return False

    def rank_hand(self):
        if self.hand_type == "five of a kind":
            return 7

        elif self.hand_type == "four of a kind":
            return 6

        elif self.hand_type == "full house":
            return 5

        elif self.hand_type == "three of a kind":
            return 4

        elif self.hand_type == "two pairs":
            return 3

        elif self.hand_type == "one pair":
            return 2

        elif self.hand_type == "high card":
            return 1

    def count_hand(self):
        hand_counts = dict(zip(DECK, [0] * len(DECK)))
        for single_card in self.hand:
            hand_counts[single_card.card] += 1
        return hand_counts

    def type_of_hand(self):
        # if hand has five of the same type
        if max(self.hand_counts.values()) == 5:
            return "five of a kind"

        # if hand has four of the same type
        elif max(self.hand_counts.values()) == 4:
            return "four of a kind"

        # if hand has full house
        elif 3 in self.hand_counts.values() and 2 in self.hand_counts.values():
            return "full house"

        # if hand has three of the same type
        elif max(self.hand_counts.values()) == 3:
            return "three of a kind"

        # if hand has two pairs
        elif list(self.hand_counts.values()).count(2) == 2:
            return "two pairs"

        # if hand has one pair
        elif list(self.hand_counts.values()).count(2) == 1:
            return "one pair"

        # if hand has high card
        else:
            return "high card"


if __name__ == "__main__":
    file_path = Path(__file__).parent / "full_input.txt"
    # open test file
    with open(file_path, "r", encoding="utf-8") as f:
        # exclude the new line character
        lines = f.read().splitlines()

    # convert each line into a Hand object
    hands = []
    for line in lines:
        hand, bid = line.split(" ")
        cards = [Card(card, DECK.index(card)) for card in hand]
        hands.append(Hand(cards, int(bid)))

    for hand in hands:
        print(hand.hand_type)

    total_winnings = sum(hand.bid * (i + 1) for i, hand in enumerate(sorted(hands)))
