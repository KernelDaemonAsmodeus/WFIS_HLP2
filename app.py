from flask import Flask, render_template, request, jsonify
import sqlite3
from models import Game
import random

app = Flask(__name__)
game = Game()

def init_db():
    with sqlite3.connect("roulette.db") as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS ranking (
                nickname TEXT PRIMARY KEY,
                max_balance INTEGER,
                spins INTEGER
            )
        """)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/start", methods=["POST"])
def start():
    nickname = request.json["nickname"]
    player = game.add_player(nickname)
    return jsonify({"balance": player.balance})

@app.route("/spin", methods=["POST"])
def spin():
    nickname = request.json["nickname"]
    player = game.get_player(nickname)
    result = player.spin()
    if result is None:
        return jsonify({"error": "Not enough balance"})

    # 20 losowych wartości od 1 do 20
    values = [random.randint(1, 20) for _ in range(20)]
    # losowanie faktycznej liczby
    values.append(result)
    # kilka dodatkowych wartości po wyniku dla wyglądu
    tail = [random.randint(1, 20) for _ in range(5)]
    values.extend(tail)

    return jsonify({
        "result": result,
        "balance": player.balance,
        "values": values,
        "result_index": len(values) - len(tail) - 1  # pozycja prawdziwego wyniku
    })

@app.route("/end", methods=["POST"])
def end():
    nickname = request.json["nickname"]
    player = game.get_player(nickname)
    with sqlite3.connect("roulette.db") as conn:
        conn.execute("""INSERT INTO ranking (nickname, max_balance, spins) 
                        VALUES (?, ?, ?)
                        ON CONFLICT(nickname) 
                        DO UPDATE SET 
                            max_balance = MAX(max_balance, excluded.max_balance),
                            spins = excluded.spins""",
                     (player.nickname, player.max_balance, player.spins))
    return jsonify({"message": "Game saved!"})

@app.route("/ranking")
def ranking():
    with sqlite3.connect("roulette.db") as conn:
        rows = conn.execute("""SELECT nickname, max_balance, spins 
                               FROM ranking 
                               ORDER BY max_balance DESC 
                               LIMIT 10""").fetchall()
    data = [{"nickname": r[0], "max_balance": r[1], "spins": r[2]} for r in rows]
    return jsonify(data)

if __name__ == "__main__":
    init_db()
    app.run(debug=False)
