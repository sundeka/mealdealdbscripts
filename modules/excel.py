from pathlib import Path
from typing import List
import pandas as pd
import uuid

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
            #
            # e.g.
            # Fruits    name
            # Unnamed: 1    kcal
            # Unnamed: 2    fat
            # etc.
            #
            # Note to self: remember to change the axis so hack solutions like this can be avoided
            # This makes no sense!
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

def parse_food_data(f: Path, categories: dict) -> List[tuple]:
    df = pd.read_excel(f, header=None)
    current_category = None
    rows = []
    for i, data in df.iterrows():
        title = data[0]
        if not current_category:
            current_category=title
            continue
        if type(title) == float:
            current_category = None
            continue
        if title!="name":
            rows.append(
                (
                    str(uuid.uuid4()),
                    title,
                    categories.get(current_category),
                    data[1],
                    data[2],
                    data[3],
                    data[4],
                    data[5],
                    data[6],
                    data[7],
                    data[8],
                    data[9],
                    data[10],
                    data[11],
                    data[12]
                )
            )
    return rows