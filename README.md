# 📚 AI-Based Study Planner

An intelligent web application that helps students **automatically generate optimized study schedules** based on subject difficulty, available time, and priorities.

---

## 📌 Project Overview

Managing study time effectively is a challenge for many students. This project solves that problem by using **AI-based logic** to create a **personalized study plan**.

👉 Just enter your subjects, difficulty level, and study hours — the system will generate a smart timetable instantly.
The project uses:
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python Flask
- **Database:** MySQL

---

## ✨ Features

- Smart timetable generation  
- Priority-based scheduling (AI logic)  
- Simple and clean user interface  
- MySQL database integration  
- Dynamic schedule display  
- Add study tasks easily  
- Priority-based task sorting  
- Responsive modern UI  
- Glassmorphism dashboard design  
- Real-time task updates  

---

## 🧠 How It Works

1. User enters:
   - Subject name  
   - Difficulty level  
   - Study hours  

2. System calculates priority: 
3. Subjects are sorted based on priority

4. A structured study plan is generated

---

## 🏗️ Tech Stack

| Layer        | Technology Used          |
|--------------|------------------------|
| Frontend     | HTML, CSS              |
| Backend      | Python (Flask)         |
| Database     | MySQL                  |
| AI Logic     | Rule-based algorithm   |
| Version Ctrl | Git & GitHub           |

---

## 📂 Project Structure

<pre>
AI-study-planner/
│
├── app.py
├── db.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── backend/
│   └── scheduler.py
│
├── database/
│   └── db.sql
│
├── templates/
│   ├── index.html
│   └── dashboard.html
│
├── static/
│   └── style.css
</pre>
## 📸 Sample Output
- Day 1 - Math (2 hrs)
- Day 2 - Physics (1 hr)
- Day 3 - Chemistry (2 hrs)

## 💡 Learning Outcomes
1. Understanding of AI-based scheduling
2. Full-stack web development
3. Database integration
4. Version control using Git

--- 
## 🧠 How Priority Works

The system calculates a **priority score** using:
- Task difficulty
- Deadline urgency

Higher priority tasks appear first in the generated study plan.

Example:
```text
DBMS - Transactions | Priority: 4.75
OS - Deadlocks | Priority: 2.10
```

---

## 🛠️ Technologies Used

- HTML5
- CSS3
- JavaScript
- Python
- Flask
- MySQL

---

## ⚙️ How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/skashyap08/AI-based-study-planner.git
```

---

### 2️⃣ Open Project Folder

```bash
cd AI-based-study-planner
```

---

### 3️⃣ Install Dependencies

```bash
pip install flask mysql-connector-python
```

---

### 4️⃣ Setup MySQL Database

Create a database named:

```sql
CREATE DATABASE study_planner;
```

Import your SQL file if available.

---

### 5️⃣ Configure Database Connection

Update your MySQL credentials inside `app.py`:

```python
host="localhost"
user="root"
password="root123"
database="study_planner"
```

---

### 6️⃣ Run Flask Server

```bash
python app.py
```

---

### 7️⃣ Open in Browser

```text
http://127.0.0.1:5000
```
## live demo: 
 ```text
ai-based-study-planner-production.up.railway.app
``` 
## 🔮 Future Improvements

- AI recommendation engine
- Calendar integration
- Progress tracking
- Login system
- Study analytics dashboard
- Mobile responsive optimization

---

## 👩‍💻 Author

Sakshi Kashyap

---

## ⭐ If you like this project

Give it a star on GitHub ⭐

