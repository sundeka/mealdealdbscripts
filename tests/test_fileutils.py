from modules.fileutils import get_next_file
from pathlib import WindowsPath

def test_yield():
    for file in get_next_file():
        assert type(file) == WindowsPath
        assert file.suffix == ".xlsx"