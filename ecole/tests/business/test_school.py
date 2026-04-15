from unittest.mock import MagicMock, patch

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

#---------test de display courses list -----------------------------
def test_display_course_should_not_crash_with_empty_list(school):
    with patch("builtins.print"):
        school.display_courses_list()

def test_display_courses_list_should_print_each_course(school):
    """
    Note: display_courses_list() va lancer 2 print donc on mutliplie par2
    chaque cours ajoutés, ici 2 * 2 =4
    """
    course1 = MagicMock(spec=Course)
    course1.students_taking_it = []
    course1.__str__ = lambda self: "Mathématiques (2024-01-01 – 2024-06-30)"

    course2 = MagicMock(spec=Course)
    course2.students_taking_it = []
    course2.__str__ = lambda self: "Histoire (2024-01-01 – 2024-06-30)"

    school.add_course(course1)
    school.add_course(course2)

    with patch("builtins.print") as mock_print:
        school.display_courses_list()
        assert mock_print.call_count == 4