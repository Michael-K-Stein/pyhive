from pyhive.client import HiveClient
from tests.common import get_client_params


def test_assignments_conflict_module_id_and_object_mismatch():
    with HiveClient(**get_client_params()) as client:
        modules = list(client.get_modules())
        assert len(modules) > 0, "No modules available for assignment conflict tests."
        module = modules[0]
        try:
            list(
                client.get_assignments(
                    parent_module=module, exercise__parent_module__id=module.id + 1
                )
            )
            assert False, "Expected assertion error for conflicting module filters"
        except AssertionError:
            pass


def test_assignments_conflict_subject_id_and_object_mismatch():
    with HiveClient(**get_client_params()) as client:
        subjects = list(client.get_subjects())
        assert len(subjects) > 0, "No subjects available for assignment conflict tests."
        subject = subjects[0]
        try:
            list(
                client.get_assignments(
                    parent_subject=subject,
                    exercise__parent_module__parent_subject__id=subject.id + 1,
                )
            )
            assert False, "Expected assertion error for conflicting subject filters"
        except AssertionError:
            pass


def test_assignments_conflict_user_classes_id_and_id_in():
    with HiveClient(**get_client_params()) as client:
        try:
            list(
                client.get_assignments(
                    user__classes__id=1,
                    user__classes__id__in=[1, 2],
                )
            )
            assert False, "Expected assertion error for user__classes filters"
        except AssertionError:
            pass


essential_user_id = None


def test_assignments_conflict_user_id_in_and_for_user_mismatch():
    with HiveClient(**get_client_params()) as client:
        users = list(client.get_users())
        assert len(users) > 0, "No users available for assignment conflict tests."
        user = users[0]
        try:
            list(
                client.get_assignments(
                    user__id__in=[user.id + 1],
                    for_user=user,
                )
            )
            assert False, "Expected assertion error for user id vs for_user filters"
        except AssertionError:
            pass


def test_assignments_conflict_mentor_filters_any_two():
    with HiveClient(**get_client_params()) as client:
        # Any two of these should conflict
        try:
            list(client.get_assignments(user__mentor__id=1, user__mentor__id__in=[1]))
            assert False, "Expected assertion error for mentor filters (id & id__in)"
        except AssertionError:
            pass
        try:
            list(client.get_assignments(user__mentor__id=1, for_mentees_of=1))
            assert (
                False
            ), "Expected assertion error for mentor filters (id & for_mentees_of)"
        except AssertionError:
            pass
        try:
            list(client.get_assignments(user__mentor__id__in=[1], for_mentees_of=1))
            assert (
                False
            ), "Expected assertion error for mentor filters (id__in & for_mentees_of)"
        except AssertionError:
            pass
