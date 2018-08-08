from databases import *
from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route('/')
def home_route():
    return render_template('hello.html')


@app.route("/hello/<int:student_id>")
def display_student(student_id):
	student=query_by_id(student_id)
	return render_template('student.html', student_id = student_id, student=student )

app.run(debug=True)
