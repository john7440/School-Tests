from unittest.mock import MagicMock

import pytest

from datetime import date

from ecole.models.course import Course
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
def test_add_course_should_set_teacher_on_course(teacher):
    real_course = Course(
        name="Mathématiques",
        start_date=date(2024, 1, 1),
        end_date=date(2024, 6, 30)
    )
    teacher.add_course(real_course)
    assert real_course.teacher == teacher

def test_add_multiple_courses_should_all_have_teacher_set(teacher):
    courses = [Course(name=f"Cours {i}", start_date=date(2024, 1, 1), end_date=date(2024, 6, 30))
        for i in range(3)]
    for c in courses:
        teacher.add_course(c)
    for c in courses:
        assert c.teacher == teacher

#----------------comportemnet incorrect?-----------
def test_add_course_should_not_add_course_to_course_teached(teacher,course):
    teacher.add_course(course)
    assert course not in teacher.courses_teached

#-----ajout d'un test qui met en lumière le bug avec un vrai objet Course--------
#note: j'avais besoin d'avoir un vrai objet course pour que teacher.courses_teached
##sois modifié puisque le mock ne connais pas teacher
def test_add_course_should_add_course_to_courses_teached(teacher):
    course = Course(
        name="Maths",
        start_date=date(2023,9,4),
        end_date=date(2023,9,5)
    )
    teacher.add_course(course)
    assert course in teacher.courses_teached

#-----------------------test str---------------------------
def test_str_should_match_expected_format_without_address(teacher):
    assert str(teacher) == "Victor Hugo (23 ans), arrivé(e) le 2023-09-04"