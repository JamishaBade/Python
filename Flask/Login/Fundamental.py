from flask import Flask, request, redirect, url_for, session, Response

"""
Flask : Creates the Flask application.
request : Used to access form data sent by the user.
redirect : Used to redirect the user to another route.
url_for : Generates the URL for a given function/route.
session: Stores information about the user across requests (like login status).

Response : Allows returning a custom response, e.g., plain text.

"""
app = Flask(__name__)
app.secret_key = (
    "supersecret"  # this is a secret value that is used to encrypt session data
)


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "123":
            session["user"] = username
            return redirect(url_for("welcome"))
        else:
            return Response("Invalid credentials. Try again", mimetype="text/plain")

    return """
    <h2>Login</h2>
    <form method="POST">
    Username: <input type="text" name="username"> <br>
    Password: <input type="text" name="password"> <br>
    <input type="submit" value="Login">
    </form>
    """


@app.route("/welcome")
def welcome():
    if "user" in session:
        return f"""
        <h2>Welcome, {session["user"]}!</h2>
        <a href="{url_for('logout')}">Logout</a>
        """
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))
