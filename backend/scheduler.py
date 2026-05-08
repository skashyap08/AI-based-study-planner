from datetime import datetime


def generate_schedule(tasks):

    today = datetime.today().date()

    # Calculate priority safely
    for task in tasks:

        days_left = (task['deadline'] - today).days

        # Prevent negative or zero issue
        if days_left < 0:
            days_left = 0

        task['priority'] = round(
            task['difficulty'] * (1 / (days_left + 1)),
            2
        )

    # Sort by priority
    sorted_tasks = sorted(
        tasks,
        key=lambda x: x['priority'],
        reverse=True
    )

    schedule = []
    day = 1

    for task in sorted_tasks:

        days_left = (task['deadline'] - today).days

        if days_left < 0:
            days_left = 0

        schedule.append({
            "day": f"Day {day}",
            "subject": task['subject'],
            "topic": task['topic'],
            "deadline": str(task['deadline']),
            "days_left": days_left,
            "priority": task['priority']
        })

        day += 1

    return schedule