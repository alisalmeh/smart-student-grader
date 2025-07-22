from grader.utils import normalize_scores, apply_grade_modifier, calculate_average

def compute_final_grades(students, bonus=0, curve=0):
    normalized = {}
    for name, scores in students.items():
        normalized_scores = normalize_scores(scores)
        normalized[name] = normalized_scores

    final_grades = {}    
    for name, scores in normalized.items():
        average = calculate_average(*scores)
        final_grade = apply_grade_modifier(average, Bonus=bonus, curve=curve)
        final_grades[name] = final_grade


    return final_grades 