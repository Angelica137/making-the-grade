import math


def round_scores(student_scores: list) -> list:
    """
    Returns a list of student scores rounded to nearest integer
    """
    return [round(score) for score in student_scores]


def count_failed_students(student_scores: list) -> list:
    """
    Takes a list of student scores and 
    returns the count of failed students
    """
    return len([score for score in student_scores if score <= 40])


def above_threshold(student_scores: list, threshold: int) -> list:
    """
    Takes a list of student socres and the current top score threshold
    and returns a list of scores at or above that threshold
    """
    return [round(score)
            for score in student_scores if score >= threshold]


def letter_grades(highest: int) -> list:
    """"
    Takes the highest score in the exam and 
    returns a list of lower band thresholds for for letter grading
    """
    threshold = 41
    return list(range(threshold, highest, round((highest - threshold) / 4)))


def student_ranking(student_scores: list, student_names: list) -> list:
    """
    Returns the list of ranked students and their grades
    Assumes the parameters are sorted from highest ranked to lowest
    """
    return [f"{i + 1}. {student_names}: {student_scores}" for i, (student_names, student_scores)
            in enumerate(zip(student_names, student_scores))]


def perfect_score(student_info: list) -> list:
    """
    Returns a list containing the name and score 
    of the first student in the list to score 100
    else will return an empty list
    """
    for student in student_info:
        if 100 in student:
            return student
    return []
