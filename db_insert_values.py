# import sqlite3


# conn = sqlite3.connect("netflix.sqlite")

# cur = conn.cursor()

insert_query = """
    INSERT INTO movies (show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, desc)
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
"""

