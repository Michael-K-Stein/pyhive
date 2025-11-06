"""Users mixin for HiveClient.

Provides listing and retrieval of user records from the management API.
"""

from typing import Generator, Optional, TypeVar

from ..src.types.user import User
from .client_shared import ClientCoreMixin


class UserClientMixin(ClientCoreMixin):
    """Mixin that exposes user management endpoints (list, get, me)."""

    def get_users(  # pylint: disable=too-many-arguments
        self,
        *,
        classes__id__in: Optional[list[int]] = None,
        clearance__in: Optional[list[int]] = None,
        id__in: Optional[list[int]] = None,
        mentor__id: Optional[int] = None,
        mentor__id__in: Optional[list[int]] = None,
        program__id__in: Optional[list[int]] = None,
        program_checker__id__in: Optional[list[int]] = None,
    ) -> Generator[User, None, None]:
        """Yield users filtered by the provided criteria."""
        from ..client import HiveClient

        assert isinstance(self, HiveClient), "self must be an instance of HiveClient"

        return self._get_core_items(
            "/api/core/management/users/",
            User,
            classes__id__in=classes__id__in,
            clearance__in=clearance__in,
            id__in=id__in,
            mentor__id=mentor__id,
            mentor__id__in=mentor__id__in,
            program__id__in=program__id__in,
            program_checker__id__in=program_checker__id__in,
        )

    def get_user(self, user_id: int) -> User:
        """Return a single user by ``user_id``."""
        from ..client import HiveClient

        assert isinstance(self, HiveClient), "self must be an instance of HiveClient"

        return User.from_dict(
            self.get(f"/api/core/management/users/{user_id}/"),
            hive_client=self,
        )

    def get_user_me(self) -> User:  # pragma: no cover
        """Return the current user.

        Note: This endpoint is intentionally not implemented because it does not
        return the same shape as ``/users/{id}/`` in the current API.
        """
        raise NotImplementedError("get_user_me() is not implemented")
        # For some reason this endpoint does not return the same data as /users/{id}/
        # return User.from_dict(
        #     self.get("/api/core/management/users/me/"),
        #     hive_client=self,
        # )

