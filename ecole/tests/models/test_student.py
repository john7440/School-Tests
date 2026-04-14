from unittest.mock import MagicMock

import pytest

from ecole.models.student import Student

#-----------------------les fixtrues--------------------
@pytest.fixture(autouse=True)
def reset_student_nbr():
    Student.students_nb = 0

@pytest.fixture
def student():
    return Student(first_name="Paul", last_name="Dubois", age=12)

@pytest.fixture
def course():
    mock = MagicMock()
    mock.students_taking_it =[]
    return mock

#---------------test add course-------------------
def test_add_course_should_add_course_to_student(student, course):
    student.add_course(course)
    assert course in student.courses_taken

def test_add_course_should_add_student_to_course(student, course):
     student.add_course(course)
     assert student in course.students_taking_it

def test_add_multiple_courses_should_all_be_in_student(student):
    courses = [MagicMock(), MagicMock(), MagicMock()]
    for c in courses:
        c.students_taking_it =[]
        student.add_course(c)
    assert len(student.courses_taken) == 3

#------------------test str----------------------
def test_should_contains_first_name_and_last_name_and_age(student):
    assert "Paul" in str(student)
    assert "Dubois" in str(student)
    assert "12" in str(student)

def test_str_should_match_expected_format_without_address(student):
    assert str(student) == "Paul Dubois (12 ans), n° étudiant : 1"


