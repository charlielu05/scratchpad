import re
from pathlib import Path
from dataclasses import dataclass
from typing import List

TEST_INPUT = """
    seeds: 79 14 55 13

    seed-to-soil map:
    50 98 2
    52 50 48

    soil-to-fertilizer map:
    0 15 37
    37 52 2
    39 0 15

    fertilizer-to-water map:
    49 53 8
    0 11 42
    42 0 7
    57 7 4

    water-to-light map:
    88 18 7
    18 25 70

    light-to-temperature map:
    45 77 23
    81 45 19
    68 64 13

    temperature-to-humidity map:
    0 69 1
    1 0 69

    humidity-to-location map:
    60 56 37
    56 93 4
    """


@dataclass
class Mapping:
    name: str
    mapping: List[List[int]]


@dataclass
class MapRange:
    destination_start: int
    source_start: int
    range_len: int

    @property
    def source_range(self):
        return range(self.source_start, self.source_start + self.range_len)

    @property
    def destination_range(self):
        return range(self.destination_start, self.destination_start + self.range_len)


@dataclass
class SeedRange:
    start: int
    length: int
    mapping_name: str = None

    @property
    def range(self):
        return range(self.start, self.start + self.length)


if __name__ == "__main__":
    # read the input file
    input_file = "full_input.txt"
    with open(Path(__file__).parent / input_file) as f:
        lines = f.read()

    # separate the TEST_INPUT into sections
    sections = lines.split("\n\n")

    # seeds are a list of seed values
    # use regex to get only the integer values of seeds string
    seeds = list(map(int, re.findall(r"\d+", sections[0])))

    # process the rest of the data, these are all mappings
    # mappings are dictionaries with the name of the mapping as key
    mappings = {}
    for section in sections[1:]:
        # split the section into lines
        lines = section.split("\n")
        # remove the first line, it is the title of the map
        mapping_name = lines.pop(0)
        # convert each line into a list of integers
        list_map = [MapRange(*map(int, line.split())) for line in lines]
        # add the map to the list of maps
        mappings[mapping_name] = list_map

    # iterate through the seeds and map them to the soil, then to the fertilizer, etc.
    # the last mapping is the location
    def seed_to_location(seed: int) -> int:
        CURRENT_IDX = seed

        for map_name, map_values in mappings.items():
            for mapping in map_values:
                if CURRENT_IDX in mapping.source_range:
                    CURRENT_IDX = mapping.destination_range[
                        mapping.source_range.index(CURRENT_IDX)
                    ]
                    break

        return CURRENT_IDX

    # print(min(seed_to_location(seed_idx) for seed_idx in seeds))

    # part two
    # seeds corresponds to a pair of values, first being the start of the range
    # and second value is the length of the range

    # iterating through each possible seed value is too slow
    # instead, we compare the seed ranges to the mapping ranges
    def seed_to_seedranges(
        seedObj: SeedRange, mappings: List[MapRange], map_name: str
    ) -> List[SeedRange]:
        SEED_RANGES = []

        for mapping in mappings:
            # three cases in the mapping interval
            # first case is that the seed range is completely contained in the mapping range
            # the second case is that the seed range is partially contained in the left side of the mapping range
            # the third case is that the seed range is partially contained in the right side of the mapping range
            # the fourth case is that the seed range is completely outside of the mapping range
            # the first case is the easiest to handle

            if (
                seedObj.start >= mapping.source_start
                and seedObj.start + seedObj.length
                <= mapping.source_start + mapping.range_len
            ):
                # print("first case")
                SEED_RANGES.append(
                    SeedRange(
                        mapping.destination_start
                        + (seedObj.start - mapping.source_start),
                        seedObj.length,
                        map_name,
                    )
                )
            # the second case is more complicated
            # if the seed range is partially contained in the left side of the mapping range
            # then we need to split the seed range into two parts

            elif (
                seedObj.start <= mapping.source_start
                and seedObj.start + seedObj.length
                <= mapping.source_start + mapping.range_len
                and seedObj.start + seedObj.length >= mapping.source_start
            ):
                # print("second case")
                SEED_RANGES.append(
                    SeedRange(
                        mapping.destination_start,
                        seedObj.start + seedObj.length - mapping.source_start + 1,
                        map_name,
                    )
                )
                SEED_RANGES.append(
                    SeedRange(
                        seedObj.start,
                        mapping.source_start - seedObj.start,
                        map_name,
                    )
                )

            # the third case is similar to the second case
            # if the seed range is partially contained in the right side of the mapping range
            # then we need to split the seed range into two parts
            elif (
                seedObj.start > mapping.source_start
                and seedObj.start + seedObj.length
                > mapping.source_start + mapping.range_len
                and seedObj.start < mapping.source_start + mapping.range_len
            ):
                # print("third case")
                SEED_RANGES.append(
                    SeedRange(
                        mapping.destination_start
                        + (seedObj.start - mapping.source_start),
                        mapping.source_start + mapping.range_len - seedObj.start,
                        map_name,
                    )
                )
                SEED_RANGES.append(
                    SeedRange(
                        mapping.source_start + mapping.range_len,
                        (seedObj.start + seedObj.length)
                        - (mapping.source_start + mapping.range_len),
                        map_name,
                    ),
                )

        # the fourth case is simple, if the seed range is completely outside of the mapping range
        # then the new seed range is just the old seed range
        # we can check length of SEED_RANGES
        if len(SEED_RANGES) == 0:
            SEED_RANGES.append(SeedRange(seedObj.start, seedObj.length, map_name))
            # print("fourth case")

        return SEED_RANGES

    # TEST_SEEDS = "seeds: 1 10 40 10 99 10"
    # # break up the TEST_SEEDS string into a list of pairs of values
    # seeds = list(map(int, re.findall(r"\d+", TEST_SEEDS)))
    # print(seeds)
    seeds = [
        [SeedRange(seed, seeds[idx * 2 + 1])] for idx, seed in enumerate(seeds[::2])
    ]
    # a = seed_to_seedranges(seeds[2][0], mappings.get("seed-to-soil map:"), "soil")

    def process_seed_to_location_p2(test_seed: List[SeedRange]):
        # process all seeds to soil
        soils = [
            seed_to_seedranges(seed_range, mappings["seed-to-soil map:"], "soil")
            for seed_range in test_seed
        ]

        # process all soils to fertilizer
        fertilizers = [
            seed_to_seedranges(soil, mappings["soil-to-fertilizer map:"], "fertilizer")
            # flatten the soils list of lists
            for soil in [item for sublist in soils for item in sublist]
        ]

        # process all fertilizers to water
        waters = [
            seed_to_seedranges(
                fertilizer, mappings["fertilizer-to-water map:"], "water"
            )
            # flatten the fertilizers list of lists
            for fertilizer in [item for sublist in fertilizers for item in sublist]
        ]

        # process all water to light
        lights = [
            seed_to_seedranges(water, mappings["water-to-light map:"], "light")
            # flatten the waters list of lists
            for water in [item for sublist in waters for item in sublist]
        ]

        # process all light to temperature
        temperatures = [
            seed_to_seedranges(
                light, mappings["light-to-temperature map:"], "temperature"
            )
            # flatten the lights list of lists
            for light in [item for sublist in lights for item in sublist]
        ]

        # process all temperature to humidity
        humidities = [
            seed_to_seedranges(
                temperature, mappings["temperature-to-humidity map:"], "humidity"
            )
            # flatten the temperatures list of lists
            for temperature in [item for sublist in temperatures for item in sublist]
        ]

        # process all humidity to location
        locations = [
            seed_to_seedranges(
                humidity, mappings["humidity-to-location map:"], "location"
            )
            # flatten the humidities list of lists
            for humidity in [item for sublist in humidities for item in sublist]
        ]

        return locations

    result = [
        min(x.start for sublist in process_seed_to_location_p2(seed) for x in sublist)
        for seed in seeds
    ]
