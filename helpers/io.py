from pathlib import Path
from typing import Iterable


def yield_lines(path: Path) -> Iterable:
    with path.open("r") as fh:
        for line in fh:
            yield line.strip()
