from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Sixth version deployed to EC2, Cutie 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
