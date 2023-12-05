from collections import defaultdict
from pathlib import Path
import re


LINE_PATTERN = re.compile(r"Card\s+([0-9]+):([^:|]+)\|([^:|]+)")
NUMBER_PATTERN = re.compile(r"[0-9]+")

def _parse_line(line):
    parts = LINE_PATTERN.search(line).groups()
    return (
        int(parts[0]),
        set(NUMBER_PATTERN.findall(parts[1])),
        set(NUMBER_PATTERN.findall(parts[2])),
    )



def challenge_part1(input_data):
    card_points = []

    for line in input_data:
        game_id, winning_numbers, game_numbers = _parse_line(line)
        matching_numbers = game_numbers & winning_numbers
        if matching_numbers:
            card_points.append(2 ** (len(matching_numbers) - 1))

    return sum(card_points)


def challenge_part2(input_data):
    scratch_cards_gains = {}

    for line in input_data:
        card_id, winning_numbers, game_numbers = _parse_line(line)
        scratch_cards_gains[int(card_id)] = len(winning_numbers & game_numbers)

    pile = {card_id: 1 for card_id in scratch_cards_gains.keys()}
    for card_id, gains in scratch_cards_gains.items():
        card_count = pile[card_id]
        for won_card_id in range(card_id + 1, card_id + gains + 1):
            pile[won_card_id] += card_count
    
    return sum(pile.values())


if __name__ == "__main__":
    input_file = Path(__file__).parent / "input.txt"
    with open(input_file) as f:
        input_data = list(map(lambda s: s.strip(), f.readlines()))

    print("Part 1:", challenge_part1(input_data))
    print("Part 2:", challenge_part2(input_data))
