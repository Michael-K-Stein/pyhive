import pytest

from pyhive.client import HiveClient
from pyhive.types import Exercise


def test_get_exercises(client: HiveClient):
    for exercise in client.get_exercises():
        assert exercise is not None
        assert isinstance(exercise, Exercise)


def test_get_exercise_by_id(client: HiveClient):
    all_exercises = list(client.get_exercises())
    if not all_exercises:
        pytest.skip("No exercises available to test.")
    ex = all_exercises[0]
    looked_up = client.get_exercise(ex.id)
    assert looked_up.id == ex.id
    assert looked_up.name == ex.name


@pytest.mark.parametrize(
    "getter_name,filter_arg,attr_name",
    [
        ("get_modules", "parent_module__id", "parent_module_id"),
        ("get_modules", "parent_module", "parent_module_id"),
        ("get_subjects", "parent_module__parent_subject__id", "parent_subject_id"),
        ("get_subjects", "parent_subject", "parent_subject_id"),
    ],
)
def test_get_exercises_by_parent(
    client: HiveClient, getter_name, filter_arg, attr_name
):
    items = list(getattr(client, getter_name)())
    if not items:
        pytest.skip(f"No {getter_name} available for test.")
    item = items[0]

    filtered = list(
        client.get_exercises(
            **{filter_arg: item if "object" in filter_arg else item.id}
        )
    )
    assert all(getattr(e, attr_name) == item.id for e in filtered) or len(filtered) == 0


def test_get_exercises_by_name(client: HiveClient):
    all_exercises = list(client.get_exercises())
    if not all_exercises:
        pytest.skip("No exercises available for exercise_name test.")
    test_name = all_exercises[0].name
    filtered = list(client.get_exercises(exercise_name=test_name))
    assert all(e.name == test_name for e in filtered)
    if filtered:
        assert isinstance(filtered[0], Exercise)


def test_get_exercises_by_nonexistent_name(client: HiveClient):
    result = list(client.get_exercises(exercise_name="__unlikely_to_exist__"))
    assert len(result) == 0


@pytest.mark.parametrize(
    "conflict_case",
    [
        ("module", "parent_module", "parent_module__id"),
        ("subject", "parent_subject", "parent_module__parent_subject__id"),
    ],
)
def test_exercises_conflict(client: HiveClient, conflict_case):
    name, obj_arg, id_arg = conflict_case
    items = list(getattr(client, f"get_{name}s")())
    if not items:
        pytest.skip(f"No {name}s available for exercise conflict test.")
    item = items[0]

    with pytest.raises(AssertionError):
        list(client.get_exercises(**{obj_arg: item, id_arg: item.id + 1}))
