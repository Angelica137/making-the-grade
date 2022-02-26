from scripts.loops import *


def test_round_scores():
    student_scores = [90.33, 40.5, 55.44, 70.05,
                      30.55, 25.45, 80.45, 95.3, 38.7, 40.3]
    assert round_scores(student_scores) == [
        40, 39, 95, 80, 25, 31, 70, 55, 40, 90]
