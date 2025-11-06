"""High-level Hive API client aggregator."""

from types import TracebackType

from .assignment_responses import AssignmentResponsesClientMixin
from .assignments import AssignmentClientMixin
from .classes import ClassesClientMixin
from .exercises import ExerciseClientMixin
from .fields import FieldsClientMixin
from .modules import ModuleClientMixin
from .programs import ProgramClientMixin
from .queues import QueuesClientMixin
from .subjects import SubjectClientMixin
from .users import UserClientMixin
from .version import VersionClientMixin
from ..src.api_versions import (
    SUPPORTED_API_VERSIONS,
    LATEST_API_VERSION,
    MIN_API_VERSION,
)


class HiveClient(  # pylint: disable=too-many-ancestors,abstract-method
    ProgramClientMixin,
    SubjectClientMixin,
    ModuleClientMixin,
    ExerciseClientMixin,
    AssignmentClientMixin,
    UserClientMixin,
    ClassesClientMixin,
    FieldsClientMixin,
    AssignmentResponsesClientMixin,
    QueuesClientMixin,
    VersionClientMixin,
):
    """Aggregated HTTP client for accessing Hive API resources."""

    def __init__(self, *args, skip_version_check: bool = False, **kwargs):
        super().__init__(*args, **kwargs)
        if not skip_version_check:
            self._api_version_check()

    def __repr__(self) -> str:
        """Return a short representation including username and hive_url.

        The representation intentionally omits secrets.
        """

        return f"HiveClient({self.username!r}, input(), {self.hive_url!r})"

    def __enter__(self) -> "HiveClient":
        """Enter context manager and return this client instance.

        The underlying :class:`httpx.Client` is managed by this object's
        lifecycle; entering the context returns the authenticated client so
        callers can perform API calls.
        """
        return self

    def __exit__(
        self,
        type_: type[BaseException] | None,
        value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        """Exit the context and close the underlying httpx session.

        This delegates to the managed :class:`httpx.Client`'s ``__exit__``
        method to ensure resources are released.
        """

        self._session.__exit__(type_, value, traceback)

    def _api_version_check(self) -> None:
        """Validate that the Hive server API version is supported.

        Fetches the server version via ``get_hive_version`` and verifies it is present
        in ``SUPPORTED_API_VERSIONS``. If unsupported, raises a RuntimeError with
        guidance to align the client and server versions.

        Raises:
            RuntimeError: If the server API version is not supported by this client.
        """
        version_str = self.get_hive_version()
        if version_str not in SUPPORTED_API_VERSIONS:
            supported_range = f"{MIN_API_VERSION} .. {LATEST_API_VERSION}"
            raise RuntimeError(
                (
                    f"Unsupported Hive API version '{version_str}'. Supported versions: {supported_range}. "
                    f"Please upgrade/downgrade the server or use a compatible client."
                )
            )
