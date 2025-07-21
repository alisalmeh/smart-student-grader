# Normalize scores between 0 and 100
def normalize_scores(scores):
    return list(map(lambda x: max(0, min(x, 100)), scores))


# Apply bonus and curve using **kwargs
def apply_grade_modifier(grade, **kwargs):
    bonus = kwargs.get('bonus', 0)
    curve = kwargs.get('curve', 0)

    final_score = min(grade + bonus + curve, 100)

    return final_score


# Calculate average using *args
def calculate_average(scores):
    return sum(scores) / len(scores)


# Filter passing students
def filter_failing_students(student_grades, passing_score=60):

    return dict(filter(lambda item: item[1] >= passing_score, student_grades.items()))


# Save to file
def save_results(file_name, student_grades):
    with  open(file_name, 'w') as f:
        f.write("Student Name, Grade\n")

        for name, grade in student_grades.items():
            f.write(f"{name}: {grade}\n")

    print(f"\nGrades saved to '{file_name}'")