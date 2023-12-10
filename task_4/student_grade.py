def get_subjects():
    subjects = int(input("Enter the number of subjects: "))
    return subjects

def get_grades(subjects):
    grades = []
    for i in range(1, subjects + 1):
        grade = float(input(f"Enter grade for subject {i}: "))
        grades.append(grade)
    return grades

def calculate_average(grades):
    total_grades = sum(grades)
    average = total_grades / len(grades)
    return average

def main():
    subjects = get_subjects()
    student_grades = get_grades(subjects)
    
    print("\nStudent Grades:")
    for i, grade in enumerate(student_grades, start=1):
        print(f"Subject {i}: {grade}")

    average_grade = calculate_average(student_grades)
    print(f"\nAverage Grade: {average_grade:.2f}")

if __name__ == "__main__":
    main()
