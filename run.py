import argparse
from modules import fileutils, excel, db

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Write food categories and/or foods into DB.')
    parser.add_argument("-c", action="store_true", help="Write only food categories.")
    parser.add_argument("-f", action="store_true", help="Write only foods.")

    args = parser.parse_args()
    if not args.f and not args.c:
        ans = input("Type Y if you are ready to run without flags. Possiblity of overwriting existing stuff.")
        if ans!="Y":
            print("Terminating...")
            exit()

    conn = db.init()

    for file in fileutils.get_next_file():
        if not args.f:
            category_names = excel.parse_category_names(file)
            db.write_categories(conn, category_names)
        if not args.c:
            categories = db.read_categories(conn)
            foods = excel.parse_food_data(file, categories)
            db.write_foods(conn, foods)

    conn.close()
    print("OK!")