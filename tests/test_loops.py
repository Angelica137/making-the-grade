from scripts.loops import *


def test_round_scores():
    student_scores = [90.33, 40.5, 55.44, 70.05,
                      30.55, 25.45, 80.45, 95.3, 38.7, 40.3]
    assert round_scores(student_scores) == [
        90, 40, 55, 70, 31, 25, 80, 95, 39, 40]


def test_count_failed_students():
    student_scores = [90, 40, 55, 70, 30, 25, 80, 95, 38, 40]
    assert count_failed_students(student_scores) == 5


def test_above_threshold():
    student_scores = [90, 40, 55, 70, 30, 68, 70, 75, 83, 96]
    threshold = 75
    assert above_threshold(student_scores, threshold) == [90, 75, 83, 96]


def test_letter_grades_100():
    assert letter_grades(100) == [41, 56, 71, 86]


def test_letter_grades_88():
    assert letter_grades(88) == [41, 53, 65, 77]
