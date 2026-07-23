import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

# Enable Foreign Key
cursor.execute("PRAGMA foreign_keys = ON;")

# ---------------- DESTINATIONS ----------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS destinations (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE,
    category TEXT,
    district TEXT,
    state TEXT,
    best_season TEXT,
    approx_budget TEXT,
    difficulty_level TEXT,
    risk_level TEXT,
    ideal_duration INTEGER,
    popular_activities TEXT,
    short_description TEXT
);
""")

# ---------------- TREKS ----------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS treks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    trek_name TEXT UNIQUE,
    region TEXT,
    district TEXT,
    difficulty TEXT,
    max_altitude TEXT,
    duration TEXT,
    best_season TEXT,
    budget TEXT,
    permits TEXT,
    physical_requirement TEXT,
    essential_gear TEXT,
    nearest_hospital TEXT,
    safety_note TEXT
);
""")

# ---------------- DISTRICT EMERGENCY ----------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS district_emergency (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    district TEXT UNIQUE,
    police TEXT,
    ambulance TEXT,
    disaster_management TEXT,
    nearest_major_hospital TEXT
);
""")

connection.commit()
connection.close()

print("Database structure created successfully!")