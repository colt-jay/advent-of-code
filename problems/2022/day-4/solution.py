from pathlib import Path
from typing import List, Tuple


def solution(input_file: Path) -> Tuple[int, int]:
    with input_file.open("r") as fh:
        clean = lambda x: list(map(int, x.split("-")))
        assignment_ids: List[List[int]] = [
            clean(r1) + clean(r2)
            for r1, r2 in [line.split(",") for line in fh.read().split()]
        ]

    num_full_overlap = 0
    num_partial_overlap = 0
    for x1, x2, y1, y2 in assignment_ids:
        r1, r2 = set(range(x1, x2 + 1)), set(range(y1, y2 + 1))

        if r1.issubset(r2) or r1.issuperset(r2):
            num_full_overlap += 1

        if r1.intersection(r2):
            num_partial_overlap += 1

    return num_full_overlap, num_partial_overlap


if __name__ == "__main__":
    data_dir = Path(__file__).parent / "data"
    path_test = data_dir / "test.txt"
    path_input = data_dir / "input.txt"

    # Part 1
    p1_test, p2_test = solution(path_test)
    p1_final, p2_final = solution(path_input)

    assert p1_test == 2
    print("Solution Part 1:", p1_final)
    # Part 2
    assert p2_test == 4
    print("Solution Part 2:", p2_final)
