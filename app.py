from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from github Action 🚀 App is running on port 8080 on EC2 Instance"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
