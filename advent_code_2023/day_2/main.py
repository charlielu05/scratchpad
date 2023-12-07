from functools import reduce

test_data = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
]

marbles_limit = {"red": 12, "blue": 14, "green": 13}


def transform_input_string(input_string: str):
    data = input_string[input_string.find(":") + 1 :].split(";")

    return list(game_set.split(",") for game_set in data)


def possible_game(game_sets: str):
    possible = True

    for game in game_sets:
        for marble_counts in game:
            count, color = tuple(marble_counts.strip().split(" "))
            if int(count) > marbles_limit.get(color):
                possible = False
                break

    return possible


def possible_color(game_sets: str):
    max_marbles = {"red": 0, "blue": 0, "green": 0}

    for game in game_sets:
        for marble_counts in game:
            count, color = tuple(marble_counts.strip().split(" "))
            if int(count) > max_marbles.get(color):
                max_marbles[color] = int(count)

    return max_marbles


def return_possible(raw_data: str):
    return [
        {"id": i + 1, "possible": possible_game(games)}
        for i, games in enumerate(transform_input_string(data) for data in raw_data)
    ]


def return_possible_colors(raw_data: str):
    return [
        {"id": i + 1, "marble_counts": possible_color(games)}
        for i, games in enumerate(transform_input_string(data) for data in raw_data)
    ]


if __name__ == "__main__":
    with open("./puzzle_input.txt", encoding="utf-8") as file:
        full_data = file.read().splitlines()

    possible_full = return_possible(full_data)

    possible_sums = list(x.get("id") for x in possible_full if x.get("possible"))

    # part two
    possible_colors_full = return_possible_colors(full_data)
    marble_counts = list(
        list(game.get("marble_counts").values()) for game in possible_colors_full
    )
    multiplication_reduce = lambda x, y: x * y
    possible_colors_sums = [
        reduce(multiplication_reduce, marble_count) for marble_count in marble_counts
    ]
