from flask import Flask, session
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

@app.route("/")
def index():
    return "ok"

@app.route("/set/")
def set():
    session["key"] = "value"
    return "ok"

@app.route("/get/")
def get():
    return session.get("key", "not set")

Session(app)
