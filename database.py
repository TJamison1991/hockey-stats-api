import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "data", "practice.db")

def create_tables():
    connection = sqlite3.connect(DB_PATH)

    ## connect to db
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS players(
                   player_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   team TEXT NOT NULL,
                   position TEXT NOT NULL
        )"""
    )

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS games(
                   game_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   home_team TEXT NOT NULL,
                   away_team TEXT NOT NULL,
                   date_played TEXT NOT NULL,
                   home_score INTEGER NOT NULL,
                   away_score INTEGER NOT NULL
        )"""
    )

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS player_stats(
                   stat_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   player_id INTEGER NOT NULL,
                   game_id INTEGER NOT NULL,
                   goals INTEGER,
                   assists INTEGER,
                   points INTEGER,
                   plus_minus INTEGER,
                   penalty_minutes INTEGER,
                   sog INTEGER,
        FOREIGN KEY (player_id) REFERENCES players(player_id),
        FOREIGN KEY (game_id) REFERENCES games(game_id)
        )"""
    )

    connection.commit()
    connection.close()
    print("Tables created successfully!")


if __name__ == "__main__":
    create_tables()