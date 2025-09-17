from flask import Flask, render_template, request

app = Flask(__name__)


# Home route - login page
@app.route("/")
def login():
    return render_template("login.html")


# Submit route - handle login
@app.route("/submit", methods=["POST"])
def submit():
    # Get form data
    username = request.form.get("username", "").strip()
    password = request.form.get("password", "").strip()

    # DEBUG: check what Flask receives
    print(f"DEBUG: username='{username}', password='{password}'")

    # Adding Valid Users
    valid_users = {
        "admin": "123",
        "sager": "pass",
        "randy": "burger",
        "Jamisha": "2009",
        "Kark": "2010",
    }

    # Check credentials
    if username in valid_users and password == valid_users[username]:
        return render_template("welcome.html", name=username)
    else:
        return render_template("login.html", error="Invalid username or password")


# Run the app
if __name__ == "__main__":
    app.run(debug=True)
