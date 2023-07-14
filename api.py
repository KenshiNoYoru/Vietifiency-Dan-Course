import flask
from flask import Flask, request, jsonify
from time import time

app = Flask(__name__)

@app.route('/')
def index():
    time_run_game = time()
    normal_data = {
        "name": "Vietifiency Dan Course",
        "status": "Online",
        "time_online": f"{time_run_game}",
    }
    return jsonify(normal_data)

@app.route('/student-code/<code>')
def student_code(code):
    info = {
        "code": code,
        "name": ""
    }
    
    name = request.args.get("student")

    if name:
        info["name"] = name
    
    
    return jsonify(info), 200

app.run("0.0.0.0", 25565)