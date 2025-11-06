import re

import httpx
import pytest

from pyhive.client import HiveClient
from pyhive.src.types.assignment import Assignment
from pyhive.src.types.assignment_response import AssignmentResponse
from pyhive.src.types.class_ import Class
from pyhive.src.types.enums.class_type_enum import ClassTypeEnum
from pyhive.src.types.exercise import Exercise
from pyhive.src.types.form_field import FormField
from pyhive.src.types.user import User
from tests.common import get_client_params


def test_client():
    hive_url = "https://hive.org"
    with HiveClient("michaelks", "Password1", hive_url, verify=False) as client:
        assert client.hive_url == hive_url


def test_get():
    with HiveClient(**get_client_params()) as client:
        response = client._get("/")
        response.raise_for_status()
        assert response.status_code == httpx.codes.OK


def test_get_classes_returns_generator_and_calls_get():
    with HiveClient(**get_client_params()) as client:
        result = list(client.get_classes())
        assert len(result) == 4
        assert all(isinstance(item, Class) for item in result)


def test_get_classes_with_filters():
    with HiveClient(**get_client_params()) as client:
        # Test with name filter
        classes = list(client.get_classes(name="בינוניים"))
        assert all(c.name == "בינוניים" for c in classes)

        # Test with type filter
        filtered_classes = list(client.get_classes(type_=ClassTypeEnum.STUDENT_GROUP))
        assert all(c.type_ == ClassTypeEnum.STUDENT_GROUP for c in filtered_classes)


def test_get_class_by_id():
    with HiveClient(**get_client_params()) as client:
        classes = list(client.get_classes())

        assert len(classes) > 0, "No classes available to test."

        class_id = classes[0].id
        specific_class = client.get_class(class_id)
        assert isinstance(specific_class, Class)
        assert specific_class.id == class_id


def test_get_users():
    with HiveClient(**get_client_params()) as client:
        users = list(client.get_users())
        assert all(isinstance(user, User) for user in users)


def test_get_user_by_id():
    with HiveClient(**get_client_params()) as client:
        users = list(client.get_users())

        assert len(users) > 0, "No users available to test."

        user_id = users[0].id
        specific_user = client.get_user(user_id)
        assert isinstance(specific_user, User)
        assert specific_user.id == user_id


def test_get_exercises():
    with HiveClient(**get_client_params()) as client:
        exercises = list(client.get_exercises())
        assert len(exercises) > 0, "No exercises available to test."
        assert all(isinstance(exercise, Exercise) for exercise in exercises)


def test_get_exercise_by_id():
    with HiveClient(**get_client_params()) as client:
        exercises = list(client.get_exercises())
        assert len(exercises) > 0, "No exercises available to test."

        exercise_id = exercises[0].id
        specific_exercise = client.get_exercise(exercise_id)
        assert isinstance(specific_exercise, Exercise)
        assert specific_exercise.id == exercise_id


def test_get_exercise_fields():
    with HiveClient(**get_client_params()) as client:
        exercises = list(client.get_exercises())

        assert len(exercises) > 0, "No exercises available to test."

        fields = list(client.get_exercise_fields(exercises[0]))
        assert all(isinstance(field, FormField) for field in fields)


def test_get_exercise_field_by_id():
    with HiveClient(**get_client_params()) as client:
        exercises = list(client.get_exercises())

        assert len(exercises) > 0, "No exercises available to test."

        found_at_least_one_field = False
        for exercise in exercises:
            for field in client.get_exercise_fields(exercise):
                sanity_field = client.get_exercise_field(exercise, field.id)
                assert isinstance(sanity_field, FormField)
                assert sanity_field.id == field.id
                assert isinstance(field, FormField)
                assert field == sanity_field
                found_at_least_one_field = True
        assert found_at_least_one_field, "No exercise fields available to test."


def test_get_assignments():
    with HiveClient(**get_client_params()) as client:
        assignments = list(client.get_assignments())
        assert all(isinstance(assignment, Assignment) for assignment in assignments)
        assert all(
            isinstance(assignment.exercise, Exercise) for assignment in assignments
        )


# TODO: Remove xfail once assignments are seeded in the test dataset
@pytest.mark.xfail(strict=False, reason="No assignments available yet in fixtures")
def test_get_assignment_by_id():
    with HiveClient(**get_client_params()) as client:
        assignments = list(client.get_assignments())

        assert len(assignments) > 0, "No assignments available to test."

        assignment_id = assignments[0].id
        specific_assignment = client.get_assignment(assignment_id)
        assert isinstance(specific_assignment, Assignment)
        assert specific_assignment.id == assignment_id


# TODO: Remove xfail once assignments are seeded in the test dataset
@pytest.mark.xfail(strict=False, reason="No assignments available yet in fixtures")
def test_get_assignment_responses():
    with HiveClient(**get_client_params()) as client:
        assignments = list(client.get_assignments())

        assert len(assignments) > 0, "No assignments available to test."

        responses = list(client.get_assignment_responses(assignments[0]))
        assert all(isinstance(response, AssignmentResponse) for response in responses)


# TODO: Remove xfail once assignments are seeded in the test dataset
@pytest.mark.xfail(strict=False, reason="No assignments available yet in fixtures")
def test_get_assignment_response_by_id():
    with HiveClient(**get_client_params()) as client:
        assignments = list(client.get_assignments())

        assert len(assignments) > 0, "No assignments available to test."

        responses = list(client.get_assignment_responses(assignments[0]))
        if responses:
            response = client.get_assignment_response(assignments[0], responses[0].id)
            assert isinstance(response, AssignmentResponse)
            assert response.id == responses[0].id


def test_assignments_conflict_module_id_and_object_mismatch():
    with HiveClient(**get_client_params()) as client:
        modules = list(client.get_modules())
        assert modules, "No modules available for assignment conflict tests."
        module = modules[0]

        with pytest.raises(AssertionError):
            list(
                client.get_assignments(
                    parent_module=module,
                    exercise__parent_module__id=module.id + 1,
                )
            )


def test_assignments_conflict_subject_id_and_object_mismatch():
    with HiveClient(**get_client_params()) as client:
        subjects = list(client.get_subjects())
        assert subjects, "No subjects available for assignment conflict tests."
        subject = subjects[0]

        with pytest.raises(AssertionError):
            list(
                client.get_assignments(
                    parent_subject=subject,
                    exercise__parent_module__parent_subject__id=subject.id + 1,
                )
            )


def test_assignments_conflict_user_classes_id_and_id_in():
    with HiveClient(**get_client_params()) as client:
        with pytest.raises(AssertionError):
            list(
                client.get_assignments(
                    user__classes__id=1,
                    user__classes__id__in=[1, 2],
                )
            )


def test_assignments_conflict_user_id_in_and_for_user_mismatch():
    with HiveClient(**get_client_params()) as client:
        users = list(client.get_users())
        assert users, "No users available for assignment conflict tests."
        user = users[0]

        with pytest.raises(AssertionError):
            list(
                client.get_assignments(
                    user__id__in=[user.id + 1],
                    for_user=user,
                )
            )


@pytest.mark.parametrize(
    "kwargs",
    [
        {"user__mentor__id": 1, "user__mentor__id__in": [1]},
        {"user__mentor__id": 1, "for_mentees_of": 1},
        {"user__mentor__id__in": [1], "for_mentees_of": 1},
    ],
)
def test_assignments_conflict_mentor_filters_any_two(kwargs):
    with HiveClient(**get_client_params()) as client:
        with pytest.raises(AssertionError):
            list(client.get_assignments(**kwargs))


def test_get_hive_version():
    with HiveClient(**get_client_params()) as client:
        version = client.get_hive_version()
        assert isinstance(version, str)
        assert len(version) > 0
        assert re.match(r"^\d+\.\d+\.\d+", version)


def test_invalid_hive_version_raises(monkeypatch):
    from pyhive.src.api_versions import LATEST_API_VERSION, MIN_API_VERSION

    invalid = "0.0.0-unsupported"
    monkeypatch.setattr(HiveClient, "get_hive_version", lambda self: invalid)
    with pytest.raises(RuntimeError) as ei:
        # Constructing triggers version check in __init__
        HiveClient(**get_client_params())
    msg = str(ei.value)
    assert f"Unsupported Hive API version '{invalid}'" in msg
    assert f"{MIN_API_VERSION} .. {LATEST_API_VERSION}" in msg


def test_skip_version_check(monkeypatch):
    invalid = "0.0.0-unsupported"
    monkeypatch.setattr(HiveClient, "get_hive_version", lambda self: invalid)
    # Should not raise when skip_version_check=True
    with HiveClient(**get_client_params(), skip_version_check=True) as client:
        assert client is not None
