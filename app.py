from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Hero-Vired CI/CD Year-2026"

@app.route('/welcome')
def welcome():
    return "Hello! Let us learn CI/CD together and become experts in it. Welcome to the Hero-Vired CI/CD Year-2026 course!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True,port=5000)
