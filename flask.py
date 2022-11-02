from flask import Flask

app = Flask(__name__)

@app.route("/")
def server():
    return "<h1>the app<h1/>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
