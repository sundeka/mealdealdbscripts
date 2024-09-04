from typing import List
import pyodbc
import os
from dotenv import load_dotenv

def init() -> pyodbc.Connection:
    load_dotenv()
    cnxn_str = f'DRIVER={os.environ['driver']};SERVER={os.environ['server']};PORT={os.environ['port']};UID={os.environ['user']};PWD={os.environ['password']};DATABASE={os.environ['db']}'
    return pyodbc.connect(cnxn_str)

def write_categories(conn: pyodbc.Connection, names: List[str]):
    c = conn.cursor()
    q = "INSERT INTO food_categories (name) VALUES (?)"
    for name in names:
        c.execute(q, (name))
    c.commit()