from flask import Flask, request  #

app = Flask(__name__)


@app.route("/")  # route decorator
def home():
    return "Hello user! This is my first flask app"


@app.route("/about")
def about():
    return "this is about us page"


def connect():
    return "this is contact us page"


# @app.route("/submit", methods=["GET", "POST"])
# def submit():
#     if request.method == "POST":
#         return "you send data"
#     else:
#         return "you are only view the form"


# routes has to be unique, readible,


# Form page (to send data)
@app.route("/form")
def form():
    return """
        <h2>Submit Form</h2>
        <form action="/submit" method="post">
            <input type="text" name="username" placeholder="Enter your name">
            <input type="submit" value="Submit">
        </form>
    """


# Submit route (handles GET and POST)
@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        username = request.form.get("username")  # get data from form
        return f"You sent data: {username}"
    else:
        return "You are only viewing the form"
