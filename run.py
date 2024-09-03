import argparse
from pathlib import Path
from modules.fileutils import get_next_file

def write_categories(f: Path): pass

def write_foods(f: Path): pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Write food categories and/or foods into DB.')
    parser.add_argument("-c", action="store_true", help="Write only food categories.")
    parser.add_argument("-f", action="store_true", help="Write only foods.")
    
    args = parser.parse_args()

    for file in get_next_file():
        if not args.f:
            write_categories(file)
        if not args.c:
            write_foods(file)