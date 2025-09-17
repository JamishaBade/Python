from flask import Flask, render_template, request

app = Flask(__name__)


# Home page
@app.route("/")
def home():
    return render_template("index.html", title="Home")


# About page
@app.route("/about")
def about():
    return render_template("about.html", title="About")


# Dynamic route with variables
@app.route("/hello/<name>")
def hello(name):
    return render_template("index.html", title="Hello", name=name)


# Passing lists/dictionaries
@app.route("/users")
def users():
    names = ["Jamisha", "Sambhav", "Sam"]
    return render_template("users.html", title="Users", users=names)


# Form handling
@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        username = request.form.get("username")
        return render_template("index.html", title="Form Result", name=username)
    return render_template("form.html", title="Form")


if __name__ == "__main__":
    app.run(debug=True)
