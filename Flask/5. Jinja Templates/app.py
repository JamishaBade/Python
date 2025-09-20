from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    students = [
        {
            "name": "Marc",
            "hasGoodGrade": True,
            "subjects": ["Math", "Science", "French"],
        },
        {
            "name": "Clara",
            "hasGoodGrade": False,
            "subjects": ["History", "English", "Biology"],
        },
        {
            "name": "Jamisha",
            "hasGoodGrade": True,
            "subjects": ["Physics", "Chemistry", "Calculus"],
        },
        {
            "name": "Sambhav",
            "subjects": ["Nepali", "Chemistry", "Music"],
        },
    ]
    return render_template("profile.html", students=students)


if __name__ == "__main__":
    app.run(debug=True)
