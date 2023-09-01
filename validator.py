import re
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "update"

user_database = [{"email": "lito@gmail.com", "password": "what123"}]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    email_format = r"^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$"

    if not re.match(email_format, email):
        return "Invalid email format"

    for user in user_database:
        if user["email"] == email and user["password"] == password:
            return redirect(url_for("success"))

    return "Login Failed"


@app.route("/success")
def success():
    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=True)
