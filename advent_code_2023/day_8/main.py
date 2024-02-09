from pathlib import Path
from ast import literal_eval
from dataclasses import dataclass
import re


@dataclass
class Node:
    name: str
    left_child: str
    right_child: str

    def __eq__(self, other):
        return self.name == other.name


if __name__ == "__main__":
    with open(Path(__file__).parent / "full_input.txt") as f:
        data = f.read().splitlines()

    # store the nodes as dict
    nodes = {}
    for line in data[2:]:
        node_key, node_value = line.split("=")
        nodes[node_key.strip()] = Node(
            name=node_key.strip(),
            left_child=re.findall("[a-zA-Z]+", node_value.strip())[0],
            right_child=re.findall("[a-zA-Z]+", node_value.strip())[1],
        )

    # the instructions
    instructions = data[0]

    CURRENT_NODE = "AAA"
    DESTINATION_NODE = "ZZZ"
    STEP_COUNT = 0

    while CURRENT_NODE != DESTINATION_NODE:
        for instruction in instructions:
            if instruction == "L":
                CURRENT_NODE = nodes[CURRENT_NODE].left_child
            elif instruction == "R":
                CURRENT_NODE = nodes[CURRENT_NODE].right_child
            else:
                raise ValueError(f"Unknown instruction: {instruction}")
            STEP_COUNT += 1
            if CURRENT_NODE == DESTINATION_NODE:
                break

    print(f"Number of steps: {STEP_COUNT}")

    # part two
    # simultaneously start on every node that ends with A
    # how many steps does it take before you're only on nodes that end with Z
