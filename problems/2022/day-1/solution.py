from helpers.io import Path, yield_lines


def solution(input_file: Path, top_n: int = 1):
    current_elf = 0
    elves = []

    for line in yield_lines(input_file):
        if not line:
            elves.append(current_elf)
            current_elf = 0
            continue

        current_elf += int(line)

    if current_elf != 0:
        elves.append(current_elf)

    return sum(sorted(elves)[-top_n:])


if __name__ == "__main__":
    data_dir = Path(__file__).parent / "data"
    path_test_input = data_dir / "test.txt"
    path_input = data_dir / "input.txt"

    assert solution(path_test_input) == 24000
    print("Solution Part 1:", solution(path_input))

    assert solution(path_test_input, 3) == 45000
    print("Solution Part 2:", solution(path_input, 3))
