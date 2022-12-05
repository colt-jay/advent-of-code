import re
from pathlib import Path
from typing import List, MutableMapping, Tuple

CrateStack = MutableMapping[int, List[str]]
InstructionSet = List[Tuple[int, int, int]]


def parse_input(input_file: Path) -> Tuple[CrateStack, InstructionSet]:
    with input_file.open("r") as fh:
        # First Line And Init Stacks
        currline = next(fh)
        n_stacks = len(currline) // 4
        stacks = {i + 1: list() for i in range(n_stacks)}

        # Process Stacks
        while len(currline) > 1:
            for i in range(n_stacks):
                crate: str = currline[1 + i * 4]
                if crate.isalpha():
                    stacks[i + 1].append(crate)

            currline = next(fh)

        # Invert stacks
        for stack in stacks.values():
            stack.reverse()

        # Process Instructions
        instructions = []
        RE_INSTRUCTIONS = re.compile(r"move (\d+) from (\d+) to (\d+)")
        while True:
            try:
                currline = next(fh)
                match_result = RE_INSTRUCTIONS.match(currline)
                instruction_str = [match_result[1], match_result[2], match_result[3]]
                instructions.append(list(map(int, instruction_str)))
            except:
                break

    return stacks, instructions


def part_1(input_file: Path) -> str:
    stacks, instructions = parse_input(input_file)
    for I in instructions:
        for _ in range(I[0]):
            crane = stacks[I[1]].pop()
            stacks[I[2]].append(crane)
    return "".join([crates[-1] for crates in stacks.values()])


def part_2(input_file: Path) -> None:
    stacks, instructions = parse_input(input_file)
    for I in instructions:
        stack = stacks[I[1]]
        stacks[I[2]].extend(stack[len(stack) - I[0] :])
        stacks[I[1]] = stack[: -I[0]]

    return "".join([crates[-1] for crates in stacks.values()])


if __name__ == "__main__":
    data_dir = Path(__file__).parent / "data"
    path_test = data_dir / "test.txt"
    path_input = data_dir / "input.txt"

    # Part 1
    assert part_1(path_test) == "CMZ"
    print("Solution Part 1:", part_1(path_input))

    # Part 2
    assert part_2(path_test) == "MCD"
    print("Solution Part 2:", part_2(path_input))
