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


def test_above_threshold_2():
    student_scores = [40, 39, 95, 80, 25, 31, 70, 55, 40, 90]
    threshold = 98
    assert above_threshold(student_scores, threshold) == []


def test_above_threshold_3():
    student_scores = [88, 29, 91, 64, 78, 43, 41, 77, 36, 50]
    threshold = 80
    assert above_threshold(student_scores, threshold) == [88, 91]


def test_above_threshold_4():
    student_scores = [100, 89]
    threshold = 100
    assert above_threshold(student_scores, threshold) == [100]


def test_above_threshold_5():
    student_scores = [88, 29, 91, 64, 78, 43, 41, 77, 36, 50]
    threshold = 78
    assert above_threshold(student_scores, threshold) == [88, 91, 78]


def test_above_threshold_5():
    student_scores = []
    threshold = 80
    assert above_threshold(student_scores, threshold) == []


def test_letter_grades_100():
    assert letter_grades(100) == [41, 56, 71, 86]


def test_letter_grades_88():
    assert letter_grades(88) == [41, 53, 65, 77]


def test_student_ranking():
    student_scores = [100, 99, 90, 84, 66, 53, 47]
    student_names = ['Joci', 'Sara', 'Kora', 'Jan', 'John', 'Bern', 'Fred']
    assert student_ranking(student_scores, student_names) == [
        '1. Joci: 100', '2. Sara: 99', '3. Kora: 90', '4. Jan: 84', '5. John: 66', '6. Bern: 53', '7. Fred: 47']


def test_perfect_score():
    student_info = [["Charles", 90], ["Tony", 80], ["Alex", 100]]
    assert perfect_score(student_info) == ["Alex", 100]


def test_perfect_score_empty():
    student_info = [["Charles", 90], ["Tony", 80]]
    assert perfect_score(student_info) == []
