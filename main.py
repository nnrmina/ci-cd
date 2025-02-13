from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, World!"

@app.route("/narmina")
def narmina():
    return "l m so perfect"

if __name__ == "__main__":
    app.run(debug=True)
