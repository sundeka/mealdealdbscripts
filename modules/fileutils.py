from typing import Generator
from pathlib import Path

def get_next_file() -> Generator[Path, None, None]:
    dir = Path("./excels")
    for file_path in dir.glob("*.xlsx"):
        yield dir / file_path.name