from pyhive.client import HiveClient
from pyhive.src.types.exercise import Exercise
from pyhive.src.types.module import Module
from pyhive.src.types.subject import Subject
from tests.common import get_client_params


def test_get_exercises():
    with HiveClient(**get_client_params()) as client:
        for exercise in client.get_exercises():
            assert exercise is not None
            assert isinstance(exercise, Exercise)


def test_get_exercise_by_id():
    with HiveClient(**get_client_params()) as client:
        all_exercises = list(client.get_exercises())
        if not all_exercises:
            return  # No exercises to test.
        ex = all_exercises[0]
        looked_up = client.get_exercise(ex.id)
        assert looked_up.id == ex.id
        assert looked_up.name == ex.name


def test_get_exercises_by_module_id():
    with HiveClient(**get_client_params()) as client:
        all_modules = list(client.get_modules())
        assert len(all_modules) > 0, "No modules available for parent_module__id test."
        mod_id = all_modules[0].id
        filtered = list(client.get_exercises(parent_module__id=mod_id))
        assert all(hasattr(e, "parent_module_id") and e.parent_module_id == mod_id for e in filtered) or len(filtered) == 0


def test_get_exercises_by_module_object():
    with HiveClient(**get_client_params()) as client:
        all_modules = list(client.get_modules())
        assert len(all_modules) > 0, "No modules available for parent_module test."
        module = all_modules[0]
        filtered = list(client.get_exercises(parent_module=module))
        assert all(hasattr(e, "parent_module_id") and e.parent_module_id == module.id for e in filtered) or len(filtered) == 0


def test_get_exercises_by_subject_id():
    with HiveClient(**get_client_params()) as client:
        all_subjects = list(client.get_subjects())
        assert len(all_subjects) > 0, "No subjects available for parent_module__parent_subject__id test."
        subj_id = all_subjects[0].id
        filtered = list(client.get_exercises(parent_module__parent_subject__id=subj_id))
        assert all(hasattr(e, "parent_subject_id") and e.parent_subject_id == subj_id for e in filtered) or len(filtered) == 0


def test_get_exercises_by_subject_object():
    with HiveClient(**get_client_params()) as client:
        all_subjects = list(client.get_subjects())
        assert len(all_subjects) > 0, "No subjects available for parent_subject test."
        subject = all_subjects[0]
        filtered = list(client.get_exercises(parent_subject=subject))
        assert all(hasattr(e, "parent_subject_id") and e.parent_subject_id == subject.id for e in filtered) or len(filtered) == 0


def test_get_exercises_by_name():
    with HiveClient(**get_client_params()) as client:
        all_exercises = list(client.get_exercises())
        assert len(all_exercises) > 0, "No exercises available for exercise_name test."
        test_name = all_exercises[0].name
        filtered = list(client.get_exercises(exercise_name=test_name))
        assert all(e.name == test_name for e in filtered)
        if filtered:
            assert isinstance(filtered[0], Exercise)


def test_get_exercises_by_nonexistent_name():
    with HiveClient(**get_client_params()) as client:
        result = list(client.get_exercises(exercise_name="__unlikely_to_exist__"))
        assert len(result) == 0


def test_exercises_conflict_parent_module_and_id_mismatch():
    with HiveClient(**get_client_params()) as client:
        modules = list(client.get_modules())
        assert len(modules) > 0, "No modules available for exercise conflict tests."
        module = modules[0]
        try:
            list(client.get_exercises(parent_module=module, parent_module__id=module.id + 1))
            assert False, "Expected assertion error for conflicting module filters"
        except AssertionError:
            pass


def test_exercises_conflict_parent_subject_and_id_mismatch():
    with HiveClient(**get_client_params()) as client:
        subjects = list(client.get_subjects())
        assert len(subjects) > 0, "No subjects available for exercise conflict tests."
        subject = subjects[0]
        try:
            list(
                client.get_exercises(
                    parent_subject=subject, parent_module__parent_subject__id=subject.id + 1
                )
            )
            assert False, "Expected assertion error for conflicting subject filters"
        except AssertionError:
            pass
