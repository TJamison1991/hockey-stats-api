from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)

DB_PATH = os.path.join(os.path.dirname(__file__), "data", "practice.db")

@app.route("/api/players", methods=["GET"])
def get_players():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM players")
    players = [dict(row) for row in cursor.fetchall()]
    connection.close()
    return jsonify(players)

@app.route("/api/games", methods=["GET"])
def get_games():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM games")
    games = [dict(row) for row in cursor.fetchall()]
    connection.close()
    return jsonify(games)

@app.route("/api/player_stats", methods=["GET"])
def get_player_stats():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM player_stats")
    player_stats = [dict(row) for row in cursor.fetchall()]
    connection.close()
    return jsonify(player_stats)

if __name__ == "__main__":
    app.run(debug=True)