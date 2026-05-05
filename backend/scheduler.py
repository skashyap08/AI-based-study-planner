from datetime import datetime

def generate_schedule(tasks):
    today = datetime.today().date()

    # ✅ Sort tasks by priority (difficulty + urgency)
    sorted_tasks = sorted(
        tasks,
        key=lambda x: x['difficulty'] * (1 / ((x['deadline'] - today).days + 1)),
        reverse=True
    )

    schedule = []
    day = 1

    for task in sorted_tasks:
        days_left = (task['deadline'] - today).days

        schedule.append({
            "day": f"Day {day}",
            "subject": task['subject'],
            "topic": task['topic'],
            "deadline": str(task['deadline']),
            "days_left": days_left,
            "priority": round(task['difficulty'] * (1 / (days_left + 1)), 2)
        })

        day += 1

    return schedule
    return schedule