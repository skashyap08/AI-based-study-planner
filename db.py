import mysql.connector

conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root123",
    database="study_planner"
)

cursor = conn.cursor()

subjects = [

    # Basic Subjects
    ("Math", 5, 3),
    ("Physics", 4, 2),
    ("English", 2, 1),
    ("Computer", 3, 2),

    # Medical
    ("Biology", 5, 3),
    ("Human Anatomy", 5, 2),
    ("Physiology", 4, 2),
    ("Biochemistry", 5, 3),
    ("Pathology", 4, 2),
    ("Pharmacology", 5, 3),

    # Non-Medical (PCM)
    ("Advanced Mathematics", 5, 3),
    ("Organic Chemistry", 5, 3),
    ("Inorganic Chemistry", 4, 2),
    ("Physical Chemistry", 4, 2),
    ("Electromagnetism", 5, 3),
    ("Modern Physics", 4, 2),

    # BTech CSE
    ("Data Structures", 5, 3),
    ("Algorithms", 5, 3),
    ("Operating Systems", 4, 2),
    ("Database Management Systems", 4, 2),
    ("Computer Networks", 4, 2),
    ("Software Engineering", 3, 2),
    ("Machine Learning", 5, 3),
    ("Artificial Intelligence", 5, 3),

    # Mechanical Engineering
    ("Thermodynamics", 5, 3),
    ("Fluid Mechanics", 5, 3),
    ("Strength of Materials", 4, 2),
    ("Engineering Mechanics", 4, 2),
    ("Machine Design", 5, 3),
    ("Heat Transfer", 4, 2),

    # Electrical Engineering
    ("Circuit Analysis", 5, 3),
    ("Electrical Machines", 5, 3),
    ("Power Systems", 4, 2),
    ("Control Systems", 4, 2),
    ("Signals and Systems", 5, 3),
    ("Power Electronics", 4, 2),
]

query = "INSERT INTO subjects (name, difficulty, hours) VALUES (%s, %s, %s)"

cursor.executemany(query, subjects)
conn.commit()

print("✅ Multiple subjects added!")