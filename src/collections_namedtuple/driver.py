from src.collections_namedtuple.util import calculate_average_marks

if __name__ == '__main__':

    n = int(input())

    student_data = []

    for _ in range(n):
        name, marks = input().split()
        student_data.append((name, int(marks)))

    average = calculate_average_marks(student_data)

    print(f"{average:.2f}")