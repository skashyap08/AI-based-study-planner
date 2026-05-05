from flask import Flask, jsonify, render_template, request
import mysql.connector
from backend.scheduler import generate_schedule
from datetime import datetime

app = Flask(__name__)

# Database connection function
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root123",
        database="study_planner"
    )


# Home route
@app.route('/')
def index():
    return render_template('index.html')


# Add Task
@app.route('/add_task', methods=['POST'])
def add_task():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "No data received"}), 400

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO tasks (subject, topic, difficulty, deadline, status)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            data.get('subject'),
            data.get('topic'),
            int(data.get('difficulty')),
            data.get('deadline'),
            "pending"
        ))

        conn.commit()
        conn.close()

        return jsonify({"message": "Task added successfully"})

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": str(e)}), 500


#  Schedule Route (THIS WAS MISSING)
@app.route('/schedule')
def schedule():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM tasks WHERE status='pending'")
        tasks = cursor.fetchall()

        conn.close()

        print("Tasks:", tasks)  # DEBUG

        if not tasks:
            return jsonify([])

        cleaned_tasks = []

        for t in tasks:
            # skip bad data
            if not t['deadline'] or not t['difficulty']:
                continue

            if isinstance(t['deadline'], str):
                t['deadline'] = datetime.strptime(t['deadline'], "%Y-%m-%d").date()

            cleaned_tasks.append(t)

        if not cleaned_tasks:
            return jsonify([])

        sorted_tasks = generate_schedule(cleaned_tasks)

        return jsonify(sorted_tasks)

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": str(e)}), 500


# Run app
if __name__ == '__main__':
    app.run(debug=True)