"""
Assignment resource mixin for HiveClient.

Adds methods for listing and retrieving Assignment records via the Hive API. Meant only
for use as a mixin on HiveClient.
"""

from typing import Optional, Sequence, Iterable, TYPE_CHECKING

from ..src.types.assignment import Assignment
from .client_shared import resolve_item_or_id, ClientCoreMixin

if TYPE_CHECKING:
    from ..src.types.module import ModuleLike
    from ..src.types.subject import SubjectLike

class AssignmentClientMixin(ClientCoreMixin):
    """
    Mixin class providing assignment-related API methods to HiveClient.

    Methods
    -------
    get_assignments(...various filters...)
        List all or filtered assignments, supporting complex relational filters.
    get_assignment(assignment_id)
        Retrieve a single assignment by its id.
    """

    def get_assignments(  # pylint: disable=too-many-arguments
        self,
        *,
        exercise__id: Optional[int] = None,
        exercise__parent_module__id: Optional[int] = None,
        exercise__parent_module__parent_subject__id: Optional[int] = None,
        exercise__tags__id__in: Optional[Sequence[int]] = None,
        queue__id: Optional[int] = None,
        user__classes__id: Optional[int] = None,
        user__classes__id__in: Optional[Sequence[int]] = None,
        user__id__in: Optional[Sequence[int]] = None,
        user__mentor__id: Optional[int] = None,
        user__mentor__id__in: Optional[Sequence[int]] = None,
        user__program__id__in: Optional[Sequence[int]] = None,
        # Non built-in filters
        parent_module: Optional["ModuleLike"] = None,
        parent_subject: Optional["SubjectLike"] = None,
    ) -> Iterable[Assignment]:
        """Yield ``Assignment`` objects filtered by the provided criteria."""
        from ..client import HiveClient

        assert isinstance(self, HiveClient), "self must be an instance of HiveClient"
        if parent_module is not None and exercise__parent_module__id is not None:
            assert exercise__parent_module__id == resolve_item_or_id(parent_module)
        exercise__parent_module__id = (
            exercise__parent_module__id
            if exercise__parent_module__id is not None
            else resolve_item_or_id(parent_module)
        )
        if parent_subject is not None and exercise__parent_module__parent_subject__id is not None:
            assert exercise__parent_module__parent_subject__id == resolve_item_or_id(parent_subject)
        exercise__parent_module__parent_subject__id = (
            exercise__parent_module__parent_subject__id
            if exercise__parent_module__parent_subject__id is not None
            else resolve_item_or_id(parent_subject)
        )
        return self._get_core_items(
            "/api/core/assignments/",
            Assignment,
            exercise__id=exercise__id,
            exercise__parent_module__id=exercise__parent_module__id,
            exercise__parent_module__parent_subject__id=exercise__parent_module__parent_subject__id,
            exercise__tags__id__in=exercise__tags__id__in,
            queue__id=queue__id,
            user__classes__id=user__classes__id,
            user__classes__id__in=user__classes__id__in,
            user__id__in=user__id__in,
            user__mentor__id=user__mentor__id,
            user__mentor__id__in=user__mentor__id__in,
            user__program__id__in=user__program__id__in,
        )

    def get_assignment(self, assignment_id: int) -> Assignment:
        """Return a single ``Assignment`` by its id."""
        from ..client import HiveClient

        assert isinstance(self, HiveClient), "self must be an instance of HiveClient"
        return Assignment.from_dict(
            self.get(f"/api/core/assignments/{assignment_id}/"),
            hive_client=self,
        )
