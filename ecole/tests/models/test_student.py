from unittest.mock import MagicMock

import pytest

from ecole.models.student import Student

#-----------------------les fixtrues--------------------
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

#------------------test str----------------------
def test_should_contains_first_name_and_last_name_and_age(student):
    assert "Paul" in str(student)
    assert "Dubois" in str(student)
    assert "12" in str(student)


