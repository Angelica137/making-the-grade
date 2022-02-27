from scripts.loops import *


def test_round_scores():
    student_scores = [90.33, 40.5, 55.44, 70.05,
                      30.55, 25.45, 80.45, 95.3, 38.7, 40.3]
    assert round_scores(student_scores) == [
        90, 40, 55, 70, 31, 25, 80, 95, 39, 40]


def test_count_failed_students():
    student_scores = [90, 40, 55, 70, 30, 25, 80, 95, 38, 40]
    assert count_failed_students(student_scores) == 5
