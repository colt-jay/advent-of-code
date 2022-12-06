from pathlib import Path


def find_distinct_str(buffer: str, n: int = 4) -> int:
    i_l, i_r = 0, n

    while i_r <= len(buffer):
        if len(set(buffer[i_l:i_r])) == n:
            return i_r

        i_l += 1
        i_r += 1


if __name__ == "__main__":
    data_dir = Path(__file__).parent / "data"
    path_test = data_dir / "test.txt"
    path_input = data_dir / "input.txt"

    with path_test.open("r") as fh:
        test_cases = fh.read().split("\n")

    for test_case in test_cases:
        buffer, solution_1, solution_2 = test_case.split(",")
        marker_1 = find_distinct_str(buffer)
        assert marker_1 == int(solution_1), f"Expected {solution_1} Got {marker_1}"
        marker_2 = find_distinct_str(buffer, n=14)
        assert marker_2 == int(solution_2), f"Expected {solution_2} Got {marker_2}"

    with path_input.open("r") as f:
        buffer = f.read().strip()
        print("Solution Part 1:", find_distinct_str(buffer))
        print("Solution Part 2:", find_distinct_str(buffer, n=14))
