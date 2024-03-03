import pytest
from student import Student

@pytest.fixture
def student():
    return Student("Иванов Иван Иванович", "subjects.csv")

def test_average_grade(student):
    assert student.get_average_grade() == 0

def test_average_test_score(student):
    with pytest.raises(ValueError):
        student.get_average_test_score("Math")

def test_add_grade(student):
    student.add_grade("Math", 4)
    assert student.Math == {'grades': [4], 'test_scores': []}

def test_add_test_score(student):
    student.add_test_score("Math", 80)
    assert student.Math == {'grades': [], 'test_scores': [80]}
