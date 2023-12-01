import csv
import sqlite3
import json


file_path = "netflix_titles.csv"

def read_file(file_path):
    with open(file_path, "r") as f:
        reader = csv.DictReader(f, delimiter=",")
        i = 0
        for row in reader:
            columns = []
            if i == 0:
                columns = row.keys()
                print(columns)
                db_create_table(columns)
            if i == 3:
                
                print("finished")
                return
            i+=1
            print(row)


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
