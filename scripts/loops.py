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
