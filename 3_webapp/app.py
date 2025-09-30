from flask import Flask, session, render_template, redirect, request
from flask_session import Session
from redis import Redis, RedisError
import socket

app = Flask(__name__)

app.secret_key = "3a5252fbcce94a63ae0bba73c1afd3d9"

app.config["SESSION_TYPE"] = "redis"
app.config["SESSION_PERMANENT"] = True
app.config["SESSION_USE_SIGNER"] = True
app.config["SESSION_KEY_PREFIX"] = "session:"
app.config["PERMANENT_SESSION_LIFETIME"] = 1800

app.config["SESSION_REDIS"] = Redis(host="redis", db=0, socket_timeout=2, socket_connect_timeout=2, port=6379)

Session(app)

# username: [password, message]
users = {
    "admin": ["admin", "You are the administrator."],
    "orson": ["rosebud", "Hello!"],
}

@app.route("/")
def index():
    username = session.get("uname", None)
    if username:
        return render_template("index.html", uname=username, msg=users[username][1])
    return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["uname"]
        if username in users and users[username][0] == request.form["pword"]:
            session["uname"] = username
            return redirect("/")
        else:
            return render_template("login.html", error="Invalid username or password.")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")
