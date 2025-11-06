from typing import Iterable

from pyhive.client import HiveClient
from pyhive.types import Exercise, Module, Program, Subject
from tests.common import get_client_params


def test_get() -> None:
    with HiveClient(**get_client_params()) as client:
        modules = list(client.get_modules())
        assert len(modules) > 0, "No modules available to test!"
        assert all(
            module is not None and isinstance(module, Module) for module in modules
        ), "Module in modules is not of a valid form!"


def test_module_exercises() -> None:
    with HiveClient(**get_client_params()) as client:
        for module in client.get_modules():
            exercises = list(module.get_exercises())
            assert len(exercises) > 0, "No exercises available to test!"
            assert all(isinstance(exercise, Exercise) for exercise in exercises)
            for exercise in exercises:
                assert exercise.parent_module_id == module.id
                assert exercise.parent_module_name == module.name
                assert exercise.parent_module_order == module.order
                assert exercise.parent_subject_id == module.parent_subject_id
                assert exercise.parent_subject_name == module.parent_subject_name
                assert exercise.parent_subject_symbol == module.parent_subject_symbol
                assert exercise.parent_module.parent_subject == module.parent_subject


def test_get_module_by_name():
    with HiveClient(**get_client_params()) as client:
        MODULE_NAME = "כחול לבן"
        modules = list(client.get_modules(module_name=MODULE_NAME))
        assert (
            len(modules) == 1
        ), f"Expected exactly one module with name '{MODULE_NAME}'"
        assert isinstance(modules[0], Module)
        assert modules[0].name == MODULE_NAME
        assert modules[0].parent_subject_name == "Apple"
        assert modules[0].parent_subject_symbol == "A"


def test_get_modules_by_subject_id() -> None:
    with HiveClient(**get_client_params()) as client:
        all_subjects = list(client.get_subjects())
        assert (
            len(all_subjects) > 0
        ), "No subjects available for parent_subject__id test."
        sub_id = all_subjects[0].id
        filtered = list(client.get_modules(parent_subject__id=sub_id))
        assert (
            all(
                hasattr(m, "parent_subject_id") and m.parent_subject_id == sub_id
                for m in filtered
            )
            or len(filtered) == 0
        )


def test_get_modules_by_subject_object():
    with HiveClient(**get_client_params()) as client:
        all_subjects = list(client.get_subjects())
        assert len(all_subjects) > 0, "No subjects available for parent_subject test."
        subject = all_subjects[0]
        filtered = list(client.get_modules(parent_subject=subject))
        assert (
            all(
                hasattr(m, "parent_subject_id") and m.parent_subject_id == subject.id
                for m in filtered
            )
            or len(filtered) == 0
        )


def test_get_modules_by_subject_program_id() -> None:
    with HiveClient(**get_client_params()) as client:
        all_subjects: list[Subject] = list(client.get_subjects())
        assert (
            len(all_subjects) > 0
        ), "No subjects available for parent_subject__parent_program__id__in test."
        program_id = all_subjects[0].parent_program_id
        assert (
            program_id is not None
        ), "No program_id found in subjects for module relationship test."
        filtered: list[Module] = list(
            client.get_modules(parent_subject__parent_program__id__in=[program_id])
        )
        assert len(filtered) > 0, f"No modules found under parent program {program_id}"
        assert all(
            x.parent_subject.parent_program_id == program_id for x in filtered
        ), "Mismatched module found under program search!"


def test_get_modules_by_name() -> None:
    with HiveClient(**get_client_params()) as client:
        all_modules = list(client.get_modules())
        assert len(all_modules) > 0, "No modules available for module_name test."
        module_name = all_modules[0].name
        filtered = list(client.get_modules(module_name=module_name))
        assert all(m.name == module_name for m in filtered)
        if filtered:
            assert isinstance(filtered[0], Module)


def test_get_modules_by_nonexistent_name():
    with HiveClient(**get_client_params()) as client:
        result = list(client.get_modules(module_name="__unlikely_to_exist__"))
        assert len(result) == 0


def test_get_modules_by_program() -> None:
    with HiveClient(**get_client_params()) as client:
        program = list(client.get_programs())[0]
        modules = list(client.get_modules(parent_program=program))
        assert len(modules) > 0, f"No modules found under {program}"
        assert all(
            (
                isinstance(module, Module)
                and (module.parent_program_name == program.name)
                and (module.parent_subject.parent_program_id == program.id)
            )
            for module in modules
        )


def test_modules_conflict_parent_program_filters_mismatch():
    with HiveClient(**get_client_params()) as client:
        programs = list(client.get_programs())
        assert len(programs) > 0, "No programs available for module conflict tests."
        program = programs[0]
        try:
            list(
                client.get_modules(
                    parent_subject__parent_program__id__in=[program.id + 98765],
                    parent_program=program,
                )
            )
            assert False, "Expected assertion error for conflicting program filters"
        except AssertionError:
            pass


def test_modules_both_program_filters_match_allowed():
    with HiveClient(**get_client_params()) as client:
        programs = list(client.get_programs())
        assert len(programs) > 0, "No programs available for module conflict tests."
        program = programs[0]
        modules = list(
            client.get_modules(
                parent_subject__parent_program__id__in=[program.id], parent_program=program
            )
        )
        assert isinstance(modules, list)
