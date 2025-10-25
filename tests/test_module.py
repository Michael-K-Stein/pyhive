from client import HiveClient
from src.types.exercise import Exercise
from src.types.module import Module
from tests.common import get_client_params


def test_get():
    with HiveClient(**get_client_params()) as client:
        for module in client.get_course_modules():
            assert module is not None
            assert isinstance(module, Module)


def test_module_exercises():
    with HiveClient(**get_client_params()) as client:
        for module in client.get_course_modules():
            exercises = list(module.get_exercises())
            assert len(exercises) > 0
            assert all(isinstance(exercise, Exercise) for exercise in exercises)
            for exercise in exercises:
                assert exercise.parent_module_id == module.id
                assert exercise.parent_module_name == module.name
                assert exercise.parent_module_order == module.order
                assert exercise.parent_subject_id == module.parent_subject_id
                assert exercise.parent_subject_name == module.parent_subject_name
                assert exercise.parent_subject_symbol == module.parent_subject_symbol
                assert exercise.parent_module.parent_subject == module.parent_subject
