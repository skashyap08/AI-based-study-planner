def generate_schedule(subjects):
    # AI logic (priority-based)
    sorted_subjects = sorted(
        subjects,
        key=lambda x: x['difficulty'] * x['hours'],
        reverse=True
    )

    schedule = []
    day = 1

    for sub in sorted_subjects:
        schedule.append({
            "day": f"Day {day}",
            "subject": sub['name'],
            "time": sub['hours']
        })
        day += 1

    return schedule