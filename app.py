from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Hero-Vired CI/CD Year-2026"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
