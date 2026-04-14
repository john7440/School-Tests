import pytest

from unittest.mock import MagicMock
from ecole.models.course import Course

#----------------------------les fixtures-------------------
@pytest.fixture
def course():
    return Course(
        name="Test course",
        start_date="2026-04-14",
        end_date="2026-04-15",
    )

@pytest.fixture
def teacher():
    mock = MagicMock()
    mock.courses_teached = []
    return  mock

@pytest.fixture
def student():
    mock = MagicMock()
    mock.courses_taken=[]
    return mock

#----------------test set teacher-------------------------
def test_set_teacher_should_assign_teacher_to_course(course,teacher):
    course.set_teacher(teacher)
    assert course.teacher == teacher

def test_set_teacher_should_add_course_to_teacher_courses(course,teacher):
    course.set_teacher(teacher)
    assert course in teacher.courses_teached

#--------------test de add student------------------
def test_add_student_should_add_student_to_courses(course, student):
    course.add_student(student)
    assert student in course.students_taking_it

def test_add_student_should_add_course_to_student(course, student):
    course.add_student(student)
    assert course in student.courses_taken

def test_add_multiple_students_should_all_be_in_course(course):
    students = [MagicMock(), MagicMock(), MagicMock()]
    for s in students:
        s.courses_taken = []
        course.add_student(s)
    assert len(course.students_taking_it) == 3

#---------------test str-----------------
def test_str_should_contain_course_name(course):
    assert "Test course" in str(course)

def test_str_should_contains_dates(course):
    result = str(course)
    assert "2026-04-14" in result
    assert "2026-04-15" in result