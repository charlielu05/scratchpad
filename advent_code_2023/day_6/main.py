from pathlib import Path
import re

if __name__ == "__main__":
    input_file = Path(__file__).parent / "full_input.txt"
    with open(input_file, "r", encoding="utf-8") as f:
        data = f.read().splitlines()

    # use regex to capture only the numbers from time string
    number_regex = r"\d+"
    time = [int(i) for i in re.findall(number_regex, data[0])]

    distances = [int(i) for i in re.findall(number_regex, data[1])]

    # time is measured in milliseconds, for each millisecond used, speed is increased by 1 millisecond per second
    # function to calculate how much distance travelled given time spend accelerating and total time

    def total_distance(acceleration_time: int, total_time: int) -> int:
        time_to_travel = total_time - acceleration_time
        speed = acceleration_time * 1
        return time_to_travel * speed

    assert total_distance(0, 7) == 0
    assert total_distance(2, 7) == 10
    assert total_distance(6, 7) == 6
    assert total_distance(7, 7) == 0

    # the distance is the current record for the given time allowed
    # how many different ways are there to spend the time to get more distance than current record

    def winning_times(total_time: int, distance_record: int) -> int:
        winning_times = 0
        for i in range(total_time + 1):
            if total_distance(i, total_time) > distance_record:
                winning_times += 1
        return winning_times

    wins = []
    for total_time, distance_record in zip(time, distances):
        wins.append(winning_times(total_time, distance_record))

    from functools import reduce

    print(reduce(lambda x, y: x * y, wins))

    # part 2
    # actually a single race
    # combine the time string together into one string
    # combine the distances together into one string

    total_time_str = int("".join(map(str, time)))
    total_distance_str = int("".join(map(str, distances)))

    wins_p2 = []

    wins_p2.append(winning_times(total_time_str, total_distance_str))
