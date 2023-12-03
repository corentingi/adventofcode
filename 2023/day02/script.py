from pathlib import Path
from collections import defaultdict

BAG_CONTENT = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def _parse_line(line: str):
    raw_game, raw_draws = line.split(": ", maxsplit=1)
    sets = raw_draws.split("; ")
    draws = []
    for s in sets:
        cubes = s.split(", ")
        draws.append({
            color: int(count)
            for count, color in [cube.split(" ", maxsplit=1) for cube in cubes]
        })
    return int(raw_game.split(" ", maxsplit=1)[1]), draws


def challenge_part1(input_data):
    games_ok = []
    for line in input_data:
        game_id, draws = _parse_line(line)
        for draw in draws:
            for color, count in draw.items():
                if BAG_CONTENT.get(color, 0) < count:
                    break
            else:
                continue
            break
        else:
            games_ok.append(game_id)
            continue
    return sum(games_ok)


def challenge_part2(input_data):
    games_power = []
    for line in input_data:
        _, draws = _parse_line(line)

        min_bag_content = defaultdict(lambda: 0)
        for draw in draws:
            for color, count in draw.items():
                min_bag_content[color] = max(min_bag_content[color], count)

        power = 1
        for _, count in min_bag_content.items():
            power *= count

        games_power.append(power)
    return sum(games_power)


if __name__ == "__main__":
    input_file = Path(__file__).parent / "input.txt"
    with open(input_file) as f:
        input_data = list(map(lambda s: s.strip(), f.readlines()))

    print("Part 1:", challenge_part1(input_data))
    print("Part 2:", challenge_part2(input_data))
