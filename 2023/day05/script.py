from collections import defaultdict
import logging
from pathlib import Path
import re


NUMBER_PATTERN = re.compile(r"[0-9]+")
MAP_ORDER = [
    "seed-to-soil",
    "soil-to-fertilizer",
    "fertilizer-to-water",
    "water-to-light",
    "light-to-temperature",
    "temperature-to-humidity",
    "humidity-to-location",
]
MAP_REVERSED_ORDER = reversed(MAP_ORDER)


def _parse_input_to_seeds_and_map(input_data):
    seeds = None
    maps = defaultdict(list)

    current_map = None
    for line in input_data:
        if line.startswith("seeds: "):
            seeds = list(map(int, NUMBER_PATTERN.findall(line)))
            continue

        if line == '':
            current_map = None
            continue

        if not current_map and line.endswith("map:"):
            current_map = line[0:-5]
            continue
        
        if current_map:
            map_numbers = list(map(int, NUMBER_PATTERN.findall(line)))
            maps[current_map].append(map_numbers)
            continue
    return seeds, maps


def _get_destination_from_source(map_to_use, source_value):
    for dest_start, source_start, size in map_to_use:
        if source_start <= source_value < source_start + size:
            return dest_start + (source_value - source_start)


def _range_from_start_and_size(start, size):
    return (start, start + size)


def _get_destination_ranges_from_source_range(map_to_use, source_range):
    destination_ranges = []
    for dest_start, source_start, size in map_to_use:
        new_source_start = max(source_start, source_range[0])
        new_source_end = min(source_start + size, source_range[1])

        if new_source_end >= new_source_start:
            new_dest_start = dest_start + (new_source_start - source_start)
            new_dest_end = new_dest_start + (new_source_end - new_source_start)

            destination_ranges.append((new_dest_start, new_dest_end))
    return destination_ranges


def challenge_part1(input_data):
    seeds, raw_maps = _parse_input_to_seeds_and_map(input_data)

    final_destinations = []
    for seed in seeds:
        source = seed
        for map_name in MAP_ORDER:
            destination = _get_destination_from_source(raw_maps[map_name], source)
            if destination is None:
                break
            source = destination
        else:
            final_destinations.append(destination)

    return min(final_destinations)


def challenge_part2(input_data):
    seed_ranges, raw_maps = _parse_input_to_seeds_and_map(input_data)

    min_locations = []
    for seed, size in [seed_ranges[i:i+2] for i in range(0, len(seed_ranges), 2)]:
        seed_range = _range_from_start_and_size(seed, size)

        current_ranges = [seed_range]
        for map_name in MAP_ORDER:
            next_ranges = []
            for current_range in current_ranges:
                new_next_ranges = _get_destination_ranges_from_source_range(raw_maps[map_name], current_range)
                next_ranges.extend(new_next_ranges)
            current_ranges = next_ranges

        min_locations.append(min([r[0] for r in next_ranges]))

    return min(min_locations)


if __name__ == "__main__":
    input_file = Path(__file__).parent / "input.txt"
    with open(input_file) as f:
        input_data = list(map(lambda s: s.strip(), f.readlines()))

    print("Part 1:", challenge_part1(input_data))
    print("Part 2:", challenge_part2(input_data))
