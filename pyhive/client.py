from collections.abc import Generator
from types import TracebackType
from typing import TYPE_CHECKING, Any, TypeVar

import httpx
from src.authenticated_hive_client import (
    _AuthenticatedHiveClient,  # pyright: ignore[reportPrivateUsage]
)
from src.types.class_ import Class
from src.types.enums.class_type_enum import ClassTypeEnum
from src.types.exercise import Exercise
from src.types.form_field import FormField
from src.types.module import Module
from src.types.program import Program
from src.types.subject import Subject
from src.types.user import User

if TYPE_CHECKING:
    from src.types.core_item import HiveCoreItem

CoreItemType = TypeVar("CoreItemType", bound="HiveCoreItem")


class HiveClient(_AuthenticatedHiveClient):
    """HTTP client for accessing Hive API."""

    def __init__(
        self,
        username: str,
        password: str,
        hive_url: str,
        **kwargs: Any,
    ) -> None:
        super().__init__(username, password, hive_url, **kwargs)

    def __enter__(self) -> "HiveClient":
        super().__enter__()
        return self

    def __exit__(
        self,
        type_: type[BaseException] | None,
        value: BaseException | None,
        traceback: TracebackType | None,
    ) -> bool | None:
        return super().__exit__(type_, value, traceback)

    def get_course_programs(
        self,
        id__in: list[int] | None = None,
    ) -> Generator[Program]:
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
        return Program.from_dict(
            super().get(f"/api/core/course/programs/{program_id}/"),
            hive_client=self,
        )

    def get_course_subjects(
        self,
        parent_program__id__in: list[int] | None = None,
    ) -> Generator[Subject]:
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
        return Subject.from_dict(
            super().get(f"/api/core/course/subjects/{subject_id}/"),
            hive_client=self,
        )

    def get_course_modules(
        self,
        /,
        parent_subject__id: int | None = None,
        parent_subject__parent_program__id__in: list[int] | None = None,
    ) -> Generator[Module]:
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
        return Module.from_dict(
            super().get(f"/api/core/course/modules/{module_id}/"),
            hive_client=self,
        )

    def get_exercises(
        self,
        /,
        parent_module__id: int | None = None,
        parent_module__parent_subject__id: int | None = None,
        parent_module__parent_subject__parent_program__id__in: list[int] | None = None,
        queue__id: int | None = None,
        tags__id__in: list[int] | None = None,
    ):
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
        return Exercise.from_dict(
            super().get(f"/api/core/course/exercises/{exercise_id}/"),
            hive_client=self,
        )

    def get_users(
        self,
        /,
        classes__id__in: list[int] | None = None,
        clearance__in: list[int] | None = None,
        id__in: list[int] | None = None,
        mentor__id: int | None = None,
        mentor__id__in: list[int] | None = None,
        program__id__in: list[int] | None = None,
        program_checker__id__in: list[int] | None = None,
    ) -> Generator[User]:
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
        return User.from_dict(
            super().get(f"/api/core/management/users/{user_id}/"),
            hive_client=self,
        )

    def get_classes(
        self,
        /,
        id__in: list[int] | None = None,
        name: str | None = None,
        program__id__in: list[int] | None = None,
        type_: ClassTypeEnum | None = None,
    ) -> Generator[Class]:
        return self._get_core_items(
            "/api/core/management/classes/",
            Class,
            id__in=id__in,
            name=name,
            program__id__in=program__id__in,
            type_=type_,
        )

    def get_class(self, class_id: int) -> Class:
        """Retrieve a Class object by its unique identifier.

        Args:
            class_id (int): The unique identifier of the class to retrieve.

        Returns:
            Class: An instance of the Class object populated with data from the API.

        Raises:
            requests.HTTPError: If the API request fails or returns an error response.

        """
        return Class.from_dict(
            super().get(f"/api/core/management/classes/{class_id}/"),
            hive_client=self,
        )

    def get_exercise_fields(self, exercise_id: int) -> Generator[FormField]:
        return self._get_core_items(
            f"/api/core/course/exercises/{exercise_id}/fields/",
            FormField,
            exercise_id=exercise_id,
        )

    def get_exercise_field(self, exercise_id: int, field_id: int) -> FormField:
        return FormField.from_dict(
            super().get(f"/api/core/course/exercises/{exercise_id}/fields/{field_id}/"),
            hive_client=self,
        )

    def _get_core_items(
        self,
        endpoint: str,
        item_type: type[CoreItemType],
        /,
        **kwargs: Any,  # noqa: ANN401
    ) -> Generator[CoreItemType]:
        query_params = httpx.QueryParams()
        for name, value in kwargs.items():
            if value is not None:
                query_params = query_params.set(name, value)

        return (
            item_type.from_dict(x, hive_client=self)
            for x in super().get(endpoint, params=query_params)
        )
