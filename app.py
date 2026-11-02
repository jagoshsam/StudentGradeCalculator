
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        name = request.form["name"]
        roll_number = request.form["roll_number"]

        subjects = [
            "English",
            "Mathematics",
            "Science",
            "Computer Science",
            "Social Studies"
        ]

        marks = []

        for subject in subjects:
            mark = float(request.form[subject])
            marks.append(mark)

        total = sum(marks)
        percentage = total / len(subjects)

        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 50:
            grade = "D"
        else:
            grade = "F"

        if all(mark >= 35 for mark in marks):
            status = "PASS"
        else:
            status = "FAIL"

        result = {
            "name": name,
            "roll_number": roll_number,
            "total": total,
            "percentage": round(percentage, 2),
            "grade": grade,
            "status": status
        }

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
