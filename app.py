from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Detroit Pet Parks Map API running"

if __name__ == "__main__":
    app.run(debug=True)
