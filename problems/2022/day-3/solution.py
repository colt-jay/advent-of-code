import string
from pathlib import Path

item_priorities = {char: i + 1 for i, char in enumerate(string.ascii_letters)}


def get_compartments(bag: list) -> tuple:
    n_half = len(bag) // 2
    return bag[:n_half], bag[n_half:]


def part_1(input_path: Path) -> int:
    with input_path.open("r") as fh:
        bags = fh.read().split("\n")

    return sum(
        [
            item_priorities[set.intersection(*map(set, get_compartments(bag))).pop()]
            for bag in bags
        ]
    )


def part_2(input_path: Path, group_size: int = 3) -> int:
    with input_path.open("r") as fh:
        bags = fh.read().split("\n")

    bag_groups = [
        bags[(i * group_size) : (i + 1) * group_size]
        for i in range(len(bags) // group_size)
    ]

    return sum(
        [
            item_priorities[set.intersection(*map(set, bag_group)).pop()]
            for bag_group in bag_groups
        ]
    )


if __name__ == "__main__":
    data_dir = Path(__file__).parent / "data"
    path_test = data_dir / "test.txt"
    path_input = data_dir / "input.txt"

    # Part 1
    assert part_1(path_test) == 157
    print("Solution Part 1:", part_1(path_input))
    # assert part_1(path_input) == 8240

    # Part 2
    assert part_2(path_test) == 70
    print("Solution Part 2:", part_2(path_input))
    # assert part_2(path_input) == 2587
