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

def read_categories(conn: pyodbc.Connection) -> dict:
    c = conn.cursor()
    q = "SELECT name, id FROM food_categories"
    c.execute(q)
    d = {}
    for row in c.fetchall():
        d[row[0]] = row[1]
    return d

def write_foods(conn: pyodbc.Connection, foods: List[tuple]):
    c = conn.cursor()
    q = """INSERT INTO foods 
    (food_id, name, category, calories, fat, fat_saturated, carbs, fiber, protein, salt, calories_ri, fat_ri, fat_saturated_ri, carbs_ri, protein_ri) 
    VALUES 
    (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
    for food in foods:
        c.execute(q, food)
    c.commit()