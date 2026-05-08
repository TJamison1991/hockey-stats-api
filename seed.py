import pandas as pd
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "data", "practice.db")

def seed_data():
    conn = sqlite3.connect(DB_PATH)

    games_df = pd.read_csv("sample_data/games.csv")
    players_df = pd.read_csv("sample_data/players.csv")
    player_stats_df = pd.read_csv("sample_data/player_stats.csv")

    games_df.to_sql("games", con=conn, if_exists="append", index=False)
    players_df.to_sql("players", con=conn, if_exists="append", index=False)
    player_stats_df.to_sql("player_stats", con=conn, if_exists="append", index=False)

    print("Games data successfully loaded.")
    print("Players data successfully loaded.")
    print("Player stats successfully loaded.")

if __name__ == "__main__":
    seed_data()