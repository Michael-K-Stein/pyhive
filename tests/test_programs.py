from pyhive.client import HiveClient
from pyhive.src.types.program import Program
from tests.common import get_client_params


def test_get_programs():
    with HiveClient(**get_client_params()) as client:
        for program in client.get_programs():
            assert program is not None
            assert isinstance(program, Program)


def test_get_program_by_id():
    with HiveClient(**get_client_params()) as client:
        all_programs = list(client.get_programs())
        assert len(all_programs) > 0, "No programs available for testing."
        prog = all_programs[0]
        looked_up = client.get_program(prog.id)
        assert looked_up.id == prog.id
        assert looked_up.name == prog.name


def test_get_programs_by_name():
    with HiveClient(**get_client_params()) as client:
        all_programs = list(client.get_programs())
        assert len(all_programs) > 0, "No programs available for testing."
        test_name = all_programs[0].name
        filtered = list(client.get_programs(program_name=test_name))
        assert all(p.name == test_name for p in filtered)
        if filtered:
            assert isinstance(filtered[0], Program)


def test_get_programs_by_nonexistent_name():
    with HiveClient(**get_client_params()) as client:
        result = list(client.get_programs(program_name="__unlikely_to_exist__"))
        assert len(result) == 0
