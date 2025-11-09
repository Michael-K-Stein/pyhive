import uuid
from os import name

import pytest

from pyhive import HiveClient
from pyhive.types import ClearanceEnum, GenderEnum, User
from tests.common import get_client_params


@pytest.fixture
def client():
    with HiveClient(**get_client_params()) as c:
        yield c


@pytest.fixture
def mentor(client: HiveClient):
    name_suffix = uuid.uuid4().hex[:8]
    mentor = client.create_user(
        f"TestMentor-{name_suffix}",
        "Password1",
        clearance=ClearanceEnum.SEGEL,
        gender=GenderEnum.NONBINARY,
    )
    yield mentor
    try:
        mentor.delete()
    except Exception:
        pass


@pytest.fixture
def checker(client: HiveClient):
    name_suffix = uuid.uuid4().hex[:8]
    checker = client.create_user(
        f"TestChecker-{name_suffix}",
        "Password1",
        clearance=ClearanceEnum.CHECKER,
        gender=GenderEnum.NONBINARY,
    )
    yield checker
    try:
        checker.delete()
    except Exception:
        pass


@pytest.fixture
def program(client: HiveClient, checker: User):
    name_suffix = uuid.uuid4().hex[:8]
    program = client.create_program(name=f"TestProgram{name_suffix}", checker=checker)
    yield program
    try:
        program.delete()
    except Exception:
        pass
