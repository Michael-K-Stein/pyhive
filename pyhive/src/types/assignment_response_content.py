from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define, field
from typing import TYPE_CHECKING, Any, TypeVar
from .src.types.form_field import FormField

if TYPE_CHECKING:
    from ...client import HiveClient
    from .form_field import FormField
    from .assignment import Assignment
    from .assignment_response import AssignmentResponse

T = TypeVar("T", bound="AssignmentResponseContent")


@define
class AssignmentResponseContent:
    """
    Attributes:
        content (str):
        field_id (int):
    """

    hive_client: "HiveClient"
    assignment_id: int
    assignment_response_id: int
    raw_content: str
    field_id: int

    # Lazy-loaded objects
    _content: "str | int | list[str | int] | None" = field(init=False, default=None)
    _field: "FormField | None" = field(init=False, default=None)
    _assignment: "Assignment | None" = field(init=False, default=None)
    _assignment_response: "AssignmentResponse | None" = field(init=False, default=None)

    def to_dict(self) -> dict[str, Any]:
        raw_content = self.raw_content

        field_id = self.field_id

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "content": raw_content,
                "field": field_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(
        cls: type[T],
        src_dict: Mapping[str, Any],
        assignment_id: int,
        assignment_response_id: int,
        hive_client: "HiveClient",
    ) -> T:
        d = dict(src_dict)
        raw_content = d.pop("content")
        field_id = d.pop("field")

        return cls(
            hive_client=hive_client,
            assignment_id=assignment_id,
            assignment_response_id=assignment_response_id,
            raw_content=raw_content,
            field_id=field_id,
        )

    @property
    def field(self) -> "FormField":
        """Lazily load and return the field this assignment belongs to."""
        if self._field is None:
            self._field = self.hive_client.get_exercise_field(
                exercise_id=self.assignment.exercise_id, field_id=self.field_id
            )
        return self._field

    @property
    def assignment(self) -> "Assignment":
        if self._assignment is None:
            self._assignment = self.hive_client.get_assignment(
                assignment_id=self.assignment_id
            )
        return self._assignment

    @property
    def assignment_response(self) -> "AssignmentResponse":
        if self._assignment_response is None:
            self._assignment_response = self.hive_client.get_assignment_response(
                assignment_id=self.assignment_id,
                response_id=self.assignment_response_id,
            )
        return self._assignment_response

    @property
    def content(self) -> "str | int | list[str | int]":
        from .enums.form_field_type_enum import FormFieldTypeEnum

        if self._content is None:
            if self.field.type_ is FormFieldTypeEnum.NUMBER:
                self._content = int(self.raw_content)
            elif self.field.type_ is FormFieldTypeEnum.TEXT:
                self._content = str(self.raw_content)
            elif self.field.type_ is FormFieldTypeEnum.MULTIPLE:
                self._content = self.field.choices[int(self.raw_content)]
            elif self.field.type_ is FormFieldTypeEnum.MULTIRESPONSE:
                self._content = list(
                    self.field.choices[int(i)] for i in self.raw_content.split(",")
                )
            else:
                raise ValueError(f"Unsupported form field type: {self.field.type_}")
        return self._content

    def __str__(self):
        return str(self.content)
