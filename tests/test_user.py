from pyhive.client import HiveClient
from pyhive.src.types.user import User
from tests.common import get_client_params


def test_user_me():
    with HiveClient(**get_client_params()) as client:
        me = client.get_user_me()
        assert isinstance(me, User)
        assert me.id == client.get_user(me.id).id
