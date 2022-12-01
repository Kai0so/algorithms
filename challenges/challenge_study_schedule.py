def study_schedule(permanence_period, target_time):
    connected_students = 0
    try:
        for student_schedule in permanence_period:
            if (
                student_schedule[0] <= target_time
                and student_schedule[1] >= target_time
            ):
                connected_students += 1
    except Exception:
        return None
    return connected_students
