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


def student_ranking(student_scores: list, student_names: list) -> list:
    """
    Returns the list of ranked students and their grades
    Assumes the parameters are sorted from highest ranked to lowest
    """
    ranks = []
    for i, (student_names, student_scores) in enumerate(zip(student_names, student_scores)):
        rank = f"{i + 1}. {student_names}: {student_scores}"
        ranks.append(rank)
    return ranks


student_scores = [100, 99, 90, 84, 66, 53, 47]
student_names = ['Joci', 'Sara', 'Kora', 'Jan', 'John', 'Bern', 'Fred']


print(student_ranking(student_scores, student_names))


def even_items(iterable):
    test = [v for i, v in enumerate(iterable, start=1) if not i % 2]
    print(test)


print(even_items([100, 99, 90, 84, 66, 53, 47]))
