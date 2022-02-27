from sqlite3 import threadsafety


def round_scores(student_scores: list) -> list:
    """
    Returns a list of student scores rounded to nearest integer
    """
    rounded_scores = student_scores
    for i in range(len(rounded_scores)):
        rounded_scores[i] = round(rounded_scores[i])
    return rounded_scores


def count_failed_students(student_scores: list) -> list:
    """
    Takes a list of student scores and 
    returns the cound to failed students
    """
    count = 0
    for score in student_scores:
        if score <= 40:
            count += 1
    return count


def above_threshold(students_scores: list, threshold: int) -> list:
    """
    Takes a list ost student socres and the current tops score threshold
    and returns a list of scores at or above that threshold
    """
    top_scores = [score for score in students_scores if score >= threshold]
    return top_scores


def letter_grades(highest: int) -> list:
    """"
    Takes the highest score in the exam and 
    returns a list of lower band band thresholds for for letter grading
    """
    conversion_thresholds = []
    spread = (highest - 40) / 4
    thresholds = 4
    while thresholds:
        highest = highest - spread
        threshold = highest + 1
        conversion_thresholds.append(threshold)
        thresholds -= 1
    return sorted(conversion_thresholds)
