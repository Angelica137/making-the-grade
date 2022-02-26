def round_scores(student_scores: list) -> list:
    """
    Returns a list of student scores rounded to nearest integer
    """
    rounded_scores = student_scores
    for i in range(len(rounded_scores)):
        rounded_scores[i] = round(rounded_scores[i])
    return rounded_scores
