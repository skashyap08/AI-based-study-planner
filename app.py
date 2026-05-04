from flask import Flask, render_template, request
import mysql.connector
from backend.scheduler import generate_schedule

app = Flask(__name__)

# Connect MySQL
db = mysql.connector.connect(
    host="127.0.0.1",
    user="study_user",
    password="root123",  # change this
    database="study_planner"
)

cursor = db.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    subjects = []

    names = request.form.getlist('name')
    difficulties = request.form.getlist('difficulty')
    hours = request.form.getlist('hours')

    for i in range(len(names)):
        subject = {
            "name": names[i],
            "difficulty": int(difficulties[i]),
            "hours": int(hours[i])
        }
        subjects.append(subject)

        cursor.execute(
            "INSERT INTO subjects (name, difficulty, hours) VALUES (%s, %s, %s)",
            (names[i], difficulties[i], hours[i])
        )
        db.commit()

    schedule = generate_schedule(subjects)

    return render_template('dashboard.html', schedule=schedule)

if __name__ == '__main__':
    app.run(debug=True)