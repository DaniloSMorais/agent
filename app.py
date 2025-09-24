from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "chave_super_secreta"

def init_db():
    conn = sqlite3.connect("usuarios.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    c.execute("INSERT OR IGNORE INTO usuarios (username, password) VALUES (?, ?)", ("admin", "1234"))
    c.execute("INSERT OR IGNORE INTO usuarios (username, password) VALUES (?, ?)", ("pmpr", "rotam2bpm"))
    conn.commit()
    conn.close()

@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("usuarios.db")
        c = conn.cursor()
        c.execute("SELECT * FROM usuarios WHERE username=? AND password=?", (username, password))
        user = c.fetchone()
        conn.close()

        if user:
            return redirect("https://rotam-chat-force.lovable.app/")
        else:
            flash("Usuário ou senha inválidos")
            return redirect(url_for("login"))

    return render_template("login.html")

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
