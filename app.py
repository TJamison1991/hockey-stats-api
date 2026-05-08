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

@app.route("/api/player/<player_id>", methods=["GET"])
def get_player_id(player_id):
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM players WHERE player_id = ?", (player_id,))
    row = cursor.fetchone()
    if row is None:
        return jsonify({"error": "Player not found"}), 404
    player = dict(row)
    connection.close()
    return jsonify(player)

@app.route("/api/players", methods=["POST"])
def add_player():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    data = request.get_json()
    player_name = data["name"]
    team = data["team"]
    position = data["position"]
    cursor.execute("""
        INSERT INTO players (name, team, position)
        VALUES (?, ?, ?)
    """, (player_name, team, position))
    connection.commit()
    connection.close()
    return jsonify({"message": "Player added successfully."}), 201


if __name__ == "__main__":
    app.run(debug=True)