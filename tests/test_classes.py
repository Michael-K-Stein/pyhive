from pyhive.client import HiveClient
from pyhive.types import Class, Subject
from tests.common import get_client_params


def test_get_classes():
    with HiveClient(**get_client_params()) as client:
        classes = list(client.get_classes())
        assert len(classes) > 0, "No classes available to test."
        for hive_class in classes:
            assert hive_class is not None
            assert isinstance(hive_class, Class)


def test_get_class_by_id():
    with HiveClient(**get_client_params()) as client:
        all_classes = list(client.get_classes())
        assert len(all_classes) > 0, "No classes available for testing."
        c = all_classes[0]
        looked_up = client.get_class(c.id)
        assert looked_up.id == c.id
        assert looked_up.name == c.name


def test_get_classes_by_name():
    with HiveClient(**get_client_params()) as client:
        all_classes = list(client.get_classes())
        assert len(all_classes) > 0, "No classes available for class name test."
        test_name = all_classes[0].name
        filtered = list(client.get_classes(name=test_name))
        assert all(c.name == test_name for c in filtered)
        if filtered:
            assert isinstance(filtered[0], Class)


def test_get_classes_by_nonexistent_name():
    with HiveClient(**get_client_params()) as client:
        result = list(client.get_classes(name="__unlikely_to_exist__"))
        assert len(result) == 0


def test_get_classes_by_program_id():
    with HiveClient(**get_client_params()) as client:
        all_classes = list[Subject](client.get_classes())
        assert (
            len(all_classes) > 0
        ), "No classes available for program_id relationship test."
        program_id = None
        for c in all_classes:
            if hasattr(c, "program_id") and c.program_id is not None:
                program_id = c.program_id
                break
        assert (
            program_id is not None
        ), "No program_id found in available classes for this test."
        filtered = list(client.get_classes(program__id__in=[program_id]))
        assert (
            all(
                hasattr(c, "program_id") and c.program_id == program_id
                for c in filtered
            )
            or len(filtered) == 0
        )


def test_get_classes_by_type_enum():
    with HiveClient(**get_client_params()) as client:
        all_classes = list(client.get_classes())
        assert len(all_classes) > 0, "No classes available for type filter test."
        type_value = None
        for c in all_classes:
            if hasattr(c, "type_") and c.type_ is not None:
                type_value = c.type_
                break
        assert (
            type_value is not None
        ), "No class type found in available classes for type_ test."
        filtered = list(client.get_classes(type_=type_value))
        assert (
            all(hasattr(c, "type_") and c.type_ == type_value for c in filtered)
            or len(filtered) == 0
        )
