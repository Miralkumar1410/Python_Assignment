def calculate_average_marks(student_data):
    total_marks = sum(
        marks
        for name, marks in student_data
    )

    average = total_marks / len(student_data)

    return round(average, 2)