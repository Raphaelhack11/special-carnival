from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    # dummy balance + plans
    plans = [
        {"id": 1, "name": "Basic", "stake": 50, "roi": 20, "duration": "1 month"},
        {"id": 2, "name": "Gold", "stake": 100, "roi": 35, "duration": "1 month"},
        {"id": 3, "name": "Master", "stake": 200, "roi": 50, "duration": "1 month"},
        {"id": 4, "name": "Premium", "stake": 300, "roi": 75, "duration": "1 month"},
    ]
    return render_template("dashboard.html", balance=120, plans=plans)

@app.route("/deposit")
def deposit():
    return render_template("deposit.html")

@app.route("/withdraw")
def withdraw():
    return render_template("withdraw.html")

if __name__ == "__main__":
    app.run(debug=True)
