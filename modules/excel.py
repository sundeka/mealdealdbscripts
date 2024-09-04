from pathlib import Path
from typing import List
import pandas as pd

def parse_category_names(f: Path) -> List[str]:
    df = pd.read_excel(f)
    next_row_is_title = False
    names = set()
    for i, data in df.iterrows():
        locator = data.keys()[0] # Always the value at cell 0,0. Used for indexing
        if (i==0):
            # The first row is a special case 
            # given how pandas treats the data 
            # in the form it happens to be in.
            # e.g.
            # Fruits    name
            # Unnamed: 1    kcal
            # Unnamed: 2    fat
            # etc.
            names.add(locator)
            continue
        value = data.get(locator)
        if next_row_is_title:
            names.add(value)
            next_row_is_title = False
        if type(value) == float:
            # When a NaN (float) value is reached, based on the way the
            # data is structured, the next value is always the category name
            # (apart from the first row edge case)
            next_row_is_title = True
    return sorted(names)