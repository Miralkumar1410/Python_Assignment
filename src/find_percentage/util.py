def average_score(student_marks:dict , query_name:str):
    marks=student_marks[query_name]
    return round(sum(marks)/len(marks), 2)