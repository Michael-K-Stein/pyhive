"""High-level Hive API client.

This module provides ``HiveClient``, a small, synchronous authenticated
client for the Hive service. It exposes convenience methods that return
typed model objects from :mod:`src.types` and generator-based list
endpoints for memory-efficient iteration.
"""

from collections.abc import Generator
from typing import TYPE_CHECKING, Optional, TypeVar, Any

import httpx

from .src.authenticated_hive_client import _AuthenticatedHiveClient
from .src.types.class_ import Class
from .src.types.enums.class_type_enum import ClassTypeEnum
from .src.types.exercise import Exercise
from .src.types.form_field import FormField
from .src.types.module import Module
from .src.types.program import Program
from .src.types.subject import Subject
from .src.types.user import User

if TYPE_CHECKING:
    from .src.types.core_item import HiveCoreItem

CoreItemTypeT = TypeVar("CoreItemTypeT", bound="HiveCoreItem")


class HiveClient(_AuthenticatedHiveClient):
    """HTTP client for accessing Hive API.

    The client is used as a context manager and provides typed helpers for
    common Hive resources (programs, subjects, modules, exercises, users,
    classes, and form fields).
    """

    def __enter__(self) -> "HiveClient":
        """Enter context manager and return this client instance.

        This delegates to the base class context manager which manages the
        underlying :class:`httpx.Client` session.
        """
        super().__enter__()
        return self

    def get_course_programs(
        self,
        id__in: Optional[list[int]] = None,
    ) -> Generator[Program]:
        """Yield :class:`Program` objects.

        Args:
            id__in: Optional list of program ids to filter the results.

        Yields:
            Program instances parsed from the API response.
        """

        query_params = httpx.QueryParams()
        if id__in is not None:
            query_params.set("id__in", id__in)
        return (
            Program.from_dict(program_dict, hive_client=self)
            for program_dict in super().get(
                "/api/core/course/programs/",
                params=query_params,
            )
        )

    def get_program(self, program_id: int) -> Program:
        """Return a single :class:`Program` by id.

        Args:
            program_id: The program identifier.

        Returns:
            A populated :class:`Program` object.
        """
        return Program.from_dict(
            super().get(f"/api/core/course/programs/{program_id}/"),
            hive_client=self,
        )

    def get_course_subjects(
        self,
        parent_program__id__in: Optional[list[int]] = None,
    ) -> Generator[Subject]:
        """Yield :class:`Subject` objects for course subjects.

        Args:
            parent_program__id__in: Optional list of parent program ids to
                filter subjects.

        Yields:
            Subject instances.
        """

        query_params = httpx.QueryParams()
        if parent_program__id__in is not None:
            query_params.set("parent_program__id__in", parent_program__id__in)
        return (
            Subject.from_dict(subject_dict, hive_client=self)
            for subject_dict in super().get(
                "/api/core/course/subjects/",
                params=query_params,
            )
        )

    def get_subject(self, subject_id: int) -> Subject:
        """Return a single :class:`Subject` by id.

        Args:
            subject_id: The subject identifier.

        Returns:
            A populated :class:`Subject` object.
        """
        return Subject.from_dict(
            super().get(f"/api/core/course/subjects/{subject_id}/"),
            hive_client=self,
        )

    def get_course_modules(
        self,
        /,
        parent_subject__id: Optional[int] = None,
        parent_subject__parent_program__id__in: Optional[list[int]] = None,
    ) -> Generator[Module]:
        """Yield :class:`Module` objects for course modules.

        Args:
            parent_subject__id: Optional subject id to restrict modules.
            parent_subject__parent_program__id__in: Optional list of program
                ids to restrict modules.

        Yields:
            Module instances.
        """

        query_params = httpx.QueryParams()
        if parent_subject__parent_program__id__in is not None:
            query_params.set(
                "parent_subject__parent_program__id__in",
                parent_subject__parent_program__id__in,
            )
        if parent_subject__id is not None:
            query_params.set("parent_subject__id", parent_subject__id)

        return (
            Module.from_dict(subject_dict, hive_client=self)
            for subject_dict in super().get(
                "/api/core/course/modules/",
                params=query_params,
            )
        )

    def get_module(self, module_id: int) -> Module:
        """Return a single :class:`Module` by id.

        Args:
            module_id: The module identifier.

        Returns:
            A populated :class:`Module` object.
        """
        return Module.from_dict(
            super().get(f"/api/core/course/modules/{module_id}/"),
            hive_client=self,
        )

    def get_exercises(  # pylint: disable=too-many-arguments
        self,
        *,
        parent_module__id: Optional[int] = None,
        parent_module__parent_subject__id: Optional[int] = None,
        parent_module__parent_subject__parent_program__id__in: Optional[
            list[int]
        ] = None,
        queue__id: Optional[int] = None,
        tags__id__in: Optional[list[int]] = None,
    ):
        """Yield :class:`Exercise` objects.

        Accepts common filtering keyword args which are forwarded to the
        underlying list endpoint.
        """

        return self._get_core_items(
            "/api/core/course/exercises/",
            Exercise,
            parent_module__id=parent_module__id,
            parent_module__parent_subject__id=parent_module__parent_subject__id,
            parent_module__parent_subject__parent_program__id__in=parent_module__parent_subject__parent_program__id__in,
            queue__id=queue__id,
            tags__id__in=tags__id__in,
        )

    def get_exercise(self, exercise_id: int) -> Exercise:
        """Return a single :class:`Exercise` by id.

        Args:
            exercise_id: The exercise identifier.

        Returns:
            A populated :class:`Exercise` object.
        """
        return Exercise.from_dict(
            super().get(f"/api/core/course/exercises/{exercise_id}/"),
            hive_client=self,
        )

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
    ) -> Generator[User]:
        """Yield :class:`User` objects from the management users endpoint.

        All kwargs are optional filters forwarded to the API.
        """

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
        """Return a single :class:`User` by id.

        Args:
            user_id: The user identifier.

        Returns:
            A populated :class:`User` object.
        """
        return User.from_dict(
            super().get(f"/api/core/management/users/{user_id}/"),
            hive_client=self,
        )

    def get_classes(
        self,
        *,
        id__in: Optional[list[int]] = None,
        name: Optional[str] = None,
        program__id__in: Optional[list[int]] = None,
        type_: Optional[ClassTypeEnum] = None,
    ) -> Generator[Class]:
        """Yield :class:`Class` objects from the management classes endpoint.

        Filters may be provided as keyword arguments.
        """

        return self._get_core_items(
            "/api/core/management/classes/",
            Class,
            id__in=id__in,
            name=name,
            program__id__in=program__id__in,
            type_=type_,
        )

    def get_class(
        self,
        class_id: int,
    ) -> Class:
        """Return a single :class:`Class` by id.

        Args:
            class_id: The class identifier.

        Returns:
            A populated :class:`Class` object.
        """
        return Class.from_dict(
            super().get(f"/api/core/management/classes/{class_id}/"),
            hive_client=self,
        )

    def get_exercise_fields(
        self,
        exercise_id: int,
    ) -> Generator[FormField]:
        """Yield :class:`FormField` objects for an exercise.

        Args:
            exercise_id: The exercise identifier.
        """

        return self._get_core_items(
            f"/api/core/course/exercises/{exercise_id}/fields/",
            FormField,
            exercise_id=exercise_id,
        )

    def get_exercise_field(
        self,
        exercise_id: int,
        field_id: int,
    ) -> FormField:
        """Return a single :class:`FormField` for an exercise by id.

        Args:
            exercise_id: The exercise identifier.
            field_id: The field identifier.

        Returns:
            A populated :class:`FormField` object.
        """
        return FormField.from_dict(
            super().get(f"/api/core/course/exercises/{exercise_id}/fields/{field_id}/"),
            hive_client=self,
        )

    def _get_core_items(
        self,
        endpoint: str,
        item_type: type[CoreItemTypeT],
        /,
        **kwargs: dict[str, Any],  # noqa: ANN401
    ) -> Generator[CoreItemTypeT]:
        """Internal helper to yield typed core items from a list endpoint.

        Args:
            endpoint: API endpoint path for the list resource.
            item_type: Model class with a ``from_dict`` constructor.
            **kwargs: Filter query parameters forwarded to the endpoint.

        Yields:
            Instances of ``item_type`` created via ``from_dict``.
        """

        query_params = httpx.QueryParams()
        for name, value in kwargs.items():
            if value is not None:
                query_params = query_params.set(name, value)

        return (
            item_type.from_dict(x, hive_client=self)
            for x in super().get(endpoint, params=query_params)
        )
