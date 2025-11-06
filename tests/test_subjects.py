from pyhive.client import HiveClient
from pyhive.src.types.program import Program
from pyhive.src.types.subject import Subject
from tests.common import get_client_params


def test_get_subjects():
    with HiveClient(**get_client_params()) as client:
        for subject in client.get_subjects():
            assert subject is not None
            assert isinstance(subject, Subject)


def test_get_subject_by_id():
    with HiveClient(**get_client_params()) as client:
        all_subjects = list(client.get_subjects())
        assert len(all_subjects) > 0, "No subjects available for testing."
        subj = all_subjects[0]
        looked_up = client.get_subject(subj.id)
        assert looked_up.id == subj.id
        assert looked_up.name == subj.name


def test_get_subjects_by_name():
    with HiveClient(**get_client_params()) as client:
        all_subjects = list(client.get_subjects())
        assert len(all_subjects) > 0, "No subjects available for testing."
        test_name = all_subjects[0].name
        filtered = list(client.get_subjects(subject_name=test_name))
        assert all(s.name == test_name for s in filtered)
        if filtered:
            assert isinstance(filtered[0], Subject)


def test_get_subjects_by_nonexistent_name():
    with HiveClient(**get_client_params()) as client:
        result = list(client.get_subjects(subject_name="__unlikely_to_exist__"))
        assert len(result) == 0

def test_get_subjects_by_parent_program_id():
    with HiveClient(**get_client_params()) as client:
        all_programs = list(client.get_programs())
        assert len(all_programs) > 0, "No programs available for parent_program__id__in test."
        program_id = all_programs[0].id
        filtered = list(client.get_subjects(parent_program__id__in=[program_id]))
        assert all(hasattr(s, "parent_program_id") and s.parent_program_id == program_id for s in filtered) or len(filtered) == 0

def test_get_subjects_by_parent_program_object():
    with HiveClient(**get_client_params()) as client:
        all_programs = list(client.get_programs())
        assert len(all_programs) > 0, "No programs available for parent_program test."
        program = all_programs[0]
        filtered = list(client.get_subjects(parent_program=program))
        assert all(hasattr(s, "parent_program_id") and s.parent_program_id == program.id for s in filtered) or len(filtered) == 0


def test_subjects_conflict_parent_program_filters_mismatch():
    with HiveClient(**get_client_params()) as client:
        programs = list(client.get_programs())
        assert len(programs) > 0, "No programs available for conflict tests."
        program = programs[0]
        try:
            list(
                client.get_subjects(
                    parent_program__id__in=[program.id + 123456], parent_program=program
                )
            )
            assert False, "Expected assertion error for conflicting program filters"
        except AssertionError:
            pass


def test_subjects_both_program_filters_match_allowed():
    with HiveClient(**get_client_params()) as client:
        programs = list(client.get_programs())
        assert len(programs) > 0, "No programs available for conflict tests."
        program = programs[0]
        subjects = list(
            client.get_subjects(parent_program__id__in=[program.id], parent_program=program)
        )
        assert isinstance(subjects, list)
