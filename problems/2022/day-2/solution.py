from enum import Enum

from helpers.io import Path, yield_lines


class Choice(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    @property
    def beats(self):
        if self == Choice.ROCK:
            return Choice.SCISSORS
        elif self == Choice.PAPER:
            return Choice.ROCK
        elif self == Choice.SCISSORS:
            return Choice.PAPER


class Outcome(Enum):
    LOSS = 0
    TIE = 3
    WIN = 6


encoding_part_1 = {
    "A": Choice.ROCK,
    "B": Choice.PAPER,
    "C": Choice.SCISSORS,
    "X": Choice.ROCK,
    "Y": Choice.PAPER,
    "Z": Choice.SCISSORS,
}

encoding_part_2 = {
    "A": Choice.ROCK,
    "B": Choice.PAPER,
    "C": Choice.SCISSORS,
    "X": Outcome.LOSS,
    "Y": Outcome.TIE,
    "Z": Outcome.WIN,
}


def score_round(your_choice: Choice, their_choice: Choice) -> int:
    if your_choice == their_choice:
        outcome = Outcome.TIE
    elif your_choice.beats == their_choice:
        outcome = Outcome.WIN
    else:
        outcome = Outcome.LOSS

    return your_choice.value + outcome.value


def pick_choice(their_choice: Choice, outcome: Outcome) -> Choice:
    if outcome == Outcome.TIE:
        return their_choice
    elif outcome == Outcome.LOSS:
        return their_choice.beats
    elif outcome == Outcome.WIN:
        return their_choice.beats.beats


def part_1(input_file: Path):
    total_score = 0
    for i, round in enumerate(yield_lines(input_file)):
        if not round:
            continue

        choices = round.split()
        your_choice = encoding_part_1[choices[1]]
        their_choice = encoding_part_1[choices[0]]
        score = score_round(your_choice, their_choice)
        total_score += score

    return total_score


def part_2(input_file: Path):
    total_score = 0
    for i, round in enumerate(yield_lines(input_file)):
        if not round:
            continue

        choices = round.split()
        their_choice = encoding_part_2[choices[0]]
        outcome = encoding_part_2[choices[1]]
        your_choice = pick_choice(their_choice, outcome)
        score = score_round(your_choice, their_choice)
        total_score += score

    return total_score


if __name__ == "__main__":
    data_dir = Path(__file__).parent / "data"
    path_test = data_dir / "test.txt"
    path_input = data_dir / "input.txt"

    # Part 1
    assert part_1(path_test) == 15
    print("Solution Part 1:", part_1(path_input))
    # Part 2
    assert part_2(path_test) == 12
    print("Solution Part 2:", part_2(path_input))
