import csv
import sqlite3
import json
from db_insert_values import insert_query

conn = sqlite3.connect("netflix.sqlite")
cur = conn.cursor()


file_path = "netflix_titles.csv"

def read_file(file_path):
    with open(file_path, "r") as f:
        reader = csv.DictReader(f, delimiter=",")
        i = 0
        for row in reader:
            print("Row number", i + 1)
            try:
                show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, desc = row['show_id'], row['type'], row['title'], row['director'], row['cast'], row['country'], row['date_added'], row['release_year'], row['rating'], row['duration'], row['listed_in'], row[' ']
            except Exception as e:
                print("There was an error",e,"in line", i)

            try:
                cur.execute(insert_query, [show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, desc])
            except Exception as e:
                print(e)
            i += 1
        conn.commit()
def db_create_table(columns):
    conn = sqlite3.connect("netflix.sqlite")
    print("Connected to database")
    cur = conn.cursor()
    print("cursor reached")
    values = ""
    print("values = ", values)
    
    for i,c in enumerate(columns):
        if i == 0:
            values += " ("
        if c:
            if c.isspace():
                values += "desc TEXT"
            else:
                values += f"{c} TEXT,"
            print("values =", values)
    values += ")"
    query = "CREATE TABLE IF NOT EXISTS movies"
    query += values
    print("resulting query",query)
    cur.execute(query)
    print("finished db_create_table")

def main():
    read_file(file_path)


if __name__ == "__main__":
    main()
