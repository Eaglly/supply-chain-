from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("signup.html")


@app.route("/exec1")
def signup():
    return render_template("home.html")


@app.route("/exec2")
def exec2():
    return render_template("analysis.html")


@app.route("/exec3")
def exec3():
    return render_template("order.html")


if __name__ == "__main__":
    app.run(port=5000, debug=True)
