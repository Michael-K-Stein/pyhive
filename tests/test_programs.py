from pyhive.client import HiveClient
from tests.common import get_client_params


def test_get_programs() -> None:
    with HiveClient(**get_client_params()) as client:
        for program in client.get_course_programs():
            assert program.id == client.get_program(program.id).id
            assert program.name == client.get_program(program.id).name
            assert program.auto_toilet == client.get_program(program.id).auto_toilet


def test_program_checker_resolution() -> None:
    """Check that the checker field is resolved to an item rather than an id (int)."""
    with HiveClient(**get_client_params()) as client:
        for program in client.get_course_programs():
            assert program.id == client.get_program(program.id).id
            assert program.name == client.get_program(program.id).name
            assert not isinstance(
                program.checker, int
            ), "Program checker is an integer!"
            assert program.checker_id == program.checker.id
