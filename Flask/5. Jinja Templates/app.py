from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = (
    "supersecretkey"  # private password for flask sessions. This is used for protection
)

students = [
    {
        "name": "Marc",
        "hasGoodGrade": True,
        "subjects": ["Math", "Science", "French"],
        "username": "MarcK",
        "password": "Open123",
    },
    {
        "name": "Clara",
        "hasGoodGrade": False,
        "subjects": ["History", "English", "Biology"],
        "username": "ClaraH",
        "password": "Open123",
    },
    {
        "name": "Jamisha",
        "hasGoodGrade": True,
        "subjects": ["Physics", "Chemistry", "Calculus"],
        "username": "JamishaB",
        "password": "Hello123",
    },
    {
        "name": "Sambhav",
        "hasGoodGrade": False,
        "subjects": ["Nepali", "Chemistry", "Music"],
        "username": "SambhavC",
        "password": "Dumbass",
    },
    {
        "name": "Brandon",
        "hasGoodGrade": True,
        "subjects": ["English", "Business", "Music"],
        "username": "BrandonC",
        "password": "Hello",
    },
]


@app.route("/")
def base():
    return render_template("base.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        student = next(
            (
                s
                for s in students
                if s["username"] == username and s["password"] == password
            ),  # This checks if the username and password matches
            None,
        )
        if student:
            session["username"] = student["username"]  # store login
            return redirect(url_for("student_profile"))  # go to their profile
        error = "Invalid credentials"
    return render_template("login.html", error=error)


@app.route("/student")
def student_profile():
    if "username" not in session:
        return redirect(url_for("login"))  # not logged in → send to login

    # find logged-in student
    student = next((s for s in students if s["username"] == session["username"]), None)
    if student:
        return render_template("profile.html", student=student)
    return "Student not found", 404


@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
