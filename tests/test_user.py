import pytest

from pyhive.client import HiveClient
from pyhive.src.types.user import User
from tests.common import get_client_params


# TODO: Remove xfail once get_user_me is implemented / API parity is ensured
@pytest.mark.xfail(strict=False, reason="get_user_me not implemented in API parity")
def test_user_me():
    with HiveClient(**get_client_params()) as client:
        me = client.get_user_me()
        assert isinstance(me, User)
        assert me.id == client.get_user(me.id).id
