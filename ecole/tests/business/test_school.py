from unittest.mock import MagicMock

import pytest

from ecole.business.school import School
from ecole.models.course import Course
from ecole.models.student import Student
from ecole.models.teacher import Teacher


#---------------les fixtures----------------
@pytest.fixture
def school():
    return School()

@pytest.fixture
def course():
    mock = MagicMock(spec=Course)
    mock.students_taking_it = []
    return mock

@pytest.fixture
def teacher():
    return MagicMock(spec=Teacher)

@pytest.fixture
def student():
    return MagicMock(spec=Student)

#------------------test de add course--------------------------
def test_add_course_should_add_course_to_list(school, course):
    school.add_course(course)
    assert course in school.courses

def test_add_multiple_courses_should_all_be_in_list(school):
    courses = [MagicMock(spec=Course), MagicMock(spec=Course), MagicMock(spec=Course)]
    for c in courses:
        school.add_course(c)
    assert len(school.courses) == 3

#-----------test de add teacher --------------------------
def test_add_teacher_should_add_teacher_to_list(school,teacher):
    school.add_teacher(teacher)
    assert teacher in school.teachers

def test_add_multiple_teachers_should_all_be_in_list(school):
    teachers = [MagicMock(spec=Teacher), MagicMock(spec=Teacher), MagicMock(spec=Teacher)]
    for t in teachers:
        school.add_teacher(t)
    assert len(school.teachers) == 3

#-------tests de add student------------------------
def test_add_student_should_add_student_to_list(school,student):
    school.add_student(student)
    assert student in school.students

def test_add_multiple_students_should_all_be_in_list(school):
    students = [MagicMock(spec=Student), MagicMock(spec=Student), MagicMock(spec=Student)]
    for s in students:
        school.add_student(s)
    assert len(school.students) == 3