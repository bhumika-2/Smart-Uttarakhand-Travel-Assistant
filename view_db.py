import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Show all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tables:", cursor.fetchall())

# Show all destinations
cursor.execute("SELECT * FROM destinations")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()