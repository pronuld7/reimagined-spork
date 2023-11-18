import sqlite3
import datetime
connection = sqlite3.connect("tempdate.DB.sl3", 5)
cur = connection.cursor()
cur.execute(f"INSERT INTO first_table (name) VALUES ('{datetime.datetime.now()}');")
connection.commit()
connection.close()