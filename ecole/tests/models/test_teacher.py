from unittest.mock import MagicMock

import pytest

from datetime import date
from ecole.models.teacher import Teacher


#----------les fixtures--------------------
@pytest.fixture
def teacher():
    return Teacher(
        first_name="Victor",
        last_name="Hugo",
        age=23,
        hiring_date= date(2023,9,4)
    )

@pytest.fixture
def course():
    mock = MagicMock()
    mock.teacher = None
    return mock

#---------------------text add course------------------------
def test_add_course_should_set_teacher_on_course(teacher,course):
    teacher.add_course(course)
    assert course.teacher == teacher

def test_add_multiple_courses_should_all_have_teacher_set(teacher,course):
    courses = [MagicMock(),MagicMock(),MagicMock()]
    for c in courses:
        c.teacher = None
        teacher.add_course(c)
    for c in courses:
        assert c.teacher == teacher


#-----------------------test str---------------------------
def test_str_should_match_expected_format_without_address(teacher):
    assert str(teacher) == "Victor Hugo (23 ans), arrivé(e) le 2023-09-04"