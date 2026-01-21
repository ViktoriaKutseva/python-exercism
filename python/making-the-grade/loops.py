"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores: list) -> list:
    return [round(score) for score in student_scores]

def count_failed_students(student_scores: list) -> int:
    return sum(score <= 40 for score in student_scores)

def above_threshold(student_scores: list, threshold: int) -> list:
    return [result for result in student_scores if result >= threshold]

def letter_grades(highest: int) -> list:
    score_gap = round((highest - 40) / 4)
    return list(range(41, highest, score_gap))

def student_ranking(student_scores: list, student_names: list) -> list:
    return [f'{index+1}. {student_names[index]}: {score}' for index, score in enumerate(student_scores)]

def perfect_score(student_info: list) -> list:
    return next((student for student in student_info if student[1] == 100), [])