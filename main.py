from grader.generator import get_student_data
from grader.grading import compute_final_grades
from grader.utils import filter_failing_students, save_results

def main():
    print("\n#### Welcome to Smart Student Grader ####")
    
    students = get_student_data()

    print("\nCalculating final grades... ")
    final_grades = compute_final_grades(students, bonus=3, curve=2)

    passing_students = filter_failing_students(final_grades, passing_score=60)

    print("\nFinal Grades:")
    for name, grade in passing_students.items():
        print(f"{name}: {grade:.2f}")

    save_results("final_grades.txt", passing_students)


if __name__  == "__main__":
    main()