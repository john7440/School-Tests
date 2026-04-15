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