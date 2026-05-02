import mysql.connector

conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root123",
    database="study_planner"
)

cursor = conn.cursor()

subjects = [
    ("Math", 5, 3),
    ("Physics", 4, 2),
    ("English", 2, 1),
    ("Computer", 3, 2)
]

query = "INSERT INTO subjects (name, difficulty, hours) VALUES (%s, %s, %s)"

cursor.executemany(query, subjects)
conn.commit()

print("✅ Multiple subjects added!")