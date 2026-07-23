import sqlite3


DATABASE_NAME = "database.db"


def get_db_connection():
    """
    Creates and returns a SQLite database connection.
    """

    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def execute_query(query, params=()):
    """
    Executes INSERT, UPDATE or DELETE queries.
    """

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(query, params)

    conn.commit()
    conn.close()


def fetch_one(query, params=()):
    """
    Returns a single row.
    """

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(query, params)

    row = cursor.fetchone()

    conn.close()

    return row


def fetch_all(query, params=()):
    """
    Returns multiple rows.
    """

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(query, params)

    rows = cursor.fetchall()

    conn.close()

    return rows


def get_all_destinations():
    """
    Returns all destinations.
    """

    return fetch_all(
        """
        SELECT *
        FROM destinations
        ORDER BY name
        """
    )


def get_all_treks():
    """
    Returns all treks.
    """

    return fetch_all(
        """
        SELECT *
        FROM treks
        ORDER BY trek_name
        """
    )


def get_all_categories():
    """
    Returns all unique destination categories.
    """

    return fetch_all(
        """
        SELECT DISTINCT category
        FROM destinations
        ORDER BY category
        """
    )


def get_all_districts():
    """
    Returns all unique districts.
    """

    return fetch_all(
        """
        SELECT DISTINCT district
        FROM destinations
        ORDER BY district
        """
    )


def database_status():
    """
    Checks whether the database is working.
    """

    try:

        conn = get_db_connection()

        conn.execute("SELECT 1")

        conn.close()

        return True

    except:

        return False