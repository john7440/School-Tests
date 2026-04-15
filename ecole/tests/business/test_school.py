from unittest.mock import MagicMock

import pytest

from ecole.business.school import School
from ecole.models.course import Course


#---------------les fixtures----------------
@pytest.fixture
def school():
    return School()

@pytest.fixture
def course():
    mock = MagicMock(spec=Course)
    mock.students_taking_it = []
    return mock

#------------------test de add course--------------------------
def test_add_course_should_add_course_to_list(school, course):
    school.add_course(course)
    assert course in school.courses

def test_add_multiple_courses_should_all_be_in_list(school):
    courses = [MagicMock(spec=Course), MagicMock(spec=Course), MagicMock(spec=Course)]
    for c in courses:
        school.add_course(c)
    assert len(school.courses) == 3
