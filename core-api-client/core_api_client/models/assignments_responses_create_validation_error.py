from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum

if TYPE_CHECKING:
    from ..models.assignments_responses_create_contents_index_content_error_component import (
        AssignmentsResponsesCreateContentsINDEXContentErrorComponent,
    )
    from ..models.assignments_responses_create_contents_index_field_error_component import (
        AssignmentsResponsesCreateContentsINDEXFieldErrorComponent,
    )
    from ..models.assignments_responses_create_contents_index_non_field_errors_error_component import (
        AssignmentsResponsesCreateContentsINDEXNonFieldErrorsErrorComponent,
    )
    from ..models.assignments_responses_create_contents_non_field_errors_error_component import (
        AssignmentsResponsesCreateContentsNonFieldErrorsErrorComponent,
    )
    from ..models.assignments_responses_create_dear_student_error_component import (
        AssignmentsResponsesCreateDearStudentErrorComponent,
    )
    from ..models.assignments_responses_create_file_error_component import AssignmentsResponsesCreateFileErrorComponent
    from ..models.assignments_responses_create_file_name_error_component import (
        AssignmentsResponsesCreateFileNameErrorComponent,
    )
    from ..models.assignments_responses_create_hide_checker_name_error_component import (
        AssignmentsResponsesCreateHideCheckerNameErrorComponent,
    )
    from ..models.assignments_responses_create_non_field_errors_error_component import (
        AssignmentsResponsesCreateNonFieldErrorsErrorComponent,
    )
    from ..models.assignments_responses_create_response_type_error_component import (
        AssignmentsResponsesCreateResponseTypeErrorComponent,
    )
    from ..models.assignments_responses_create_segel_only_error_component import (
        AssignmentsResponsesCreateSegelOnlyErrorComponent,
    )


T = TypeVar("T", bound="AssignmentsResponsesCreateValidationError")


@_attrs_define
class AssignmentsResponsesCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum):
            * `validation_error` - Validation Error
        errors (list[Union['AssignmentsResponsesCreateContentsINDEXContentErrorComponent',
            'AssignmentsResponsesCreateContentsINDEXFieldErrorComponent',
            'AssignmentsResponsesCreateContentsINDEXNonFieldErrorsErrorComponent',
            'AssignmentsResponsesCreateContentsNonFieldErrorsErrorComponent',
            'AssignmentsResponsesCreateDearStudentErrorComponent', 'AssignmentsResponsesCreateFileErrorComponent',
            'AssignmentsResponsesCreateFileNameErrorComponent', 'AssignmentsResponsesCreateHideCheckerNameErrorComponent',
            'AssignmentsResponsesCreateNonFieldErrorsErrorComponent',
            'AssignmentsResponsesCreateResponseTypeErrorComponent', 'AssignmentsResponsesCreateSegelOnlyErrorComponent']]):
    """

    type_: ValidationErrorEnum
    errors: list[
        Union[
            "AssignmentsResponsesCreateContentsINDEXContentErrorComponent",
            "AssignmentsResponsesCreateContentsINDEXFieldErrorComponent",
            "AssignmentsResponsesCreateContentsINDEXNonFieldErrorsErrorComponent",
            "AssignmentsResponsesCreateContentsNonFieldErrorsErrorComponent",
            "AssignmentsResponsesCreateDearStudentErrorComponent",
            "AssignmentsResponsesCreateFileErrorComponent",
            "AssignmentsResponsesCreateFileNameErrorComponent",
            "AssignmentsResponsesCreateHideCheckerNameErrorComponent",
            "AssignmentsResponsesCreateNonFieldErrorsErrorComponent",
            "AssignmentsResponsesCreateResponseTypeErrorComponent",
            "AssignmentsResponsesCreateSegelOnlyErrorComponent",
        ]
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.assignments_responses_create_contents_index_content_error_component import (
            AssignmentsResponsesCreateContentsINDEXContentErrorComponent,
        )
        from ..models.assignments_responses_create_contents_index_field_error_component import (
            AssignmentsResponsesCreateContentsINDEXFieldErrorComponent,
        )
        from ..models.assignments_responses_create_contents_index_non_field_errors_error_component import (
            AssignmentsResponsesCreateContentsINDEXNonFieldErrorsErrorComponent,
        )
        from ..models.assignments_responses_create_contents_non_field_errors_error_component import (
            AssignmentsResponsesCreateContentsNonFieldErrorsErrorComponent,
        )
        from ..models.assignments_responses_create_dear_student_error_component import (
            AssignmentsResponsesCreateDearStudentErrorComponent,
        )
        from ..models.assignments_responses_create_file_error_component import (
            AssignmentsResponsesCreateFileErrorComponent,
        )
        from ..models.assignments_responses_create_file_name_error_component import (
            AssignmentsResponsesCreateFileNameErrorComponent,
        )
        from ..models.assignments_responses_create_hide_checker_name_error_component import (
            AssignmentsResponsesCreateHideCheckerNameErrorComponent,
        )
        from ..models.assignments_responses_create_non_field_errors_error_component import (
            AssignmentsResponsesCreateNonFieldErrorsErrorComponent,
        )
        from ..models.assignments_responses_create_segel_only_error_component import (
            AssignmentsResponsesCreateSegelOnlyErrorComponent,
        )

        type_ = self.type_.value

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, AssignmentsResponsesCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsResponsesCreateContentsNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsResponsesCreateContentsINDEXNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsResponsesCreateContentsINDEXContentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsResponsesCreateContentsINDEXFieldErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsResponsesCreateFileNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsResponsesCreateFileErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsResponsesCreateDearStudentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsResponsesCreateHideCheckerNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsResponsesCreateSegelOnlyErrorComponent):
                errors_item = errors_item_data.to_dict()
            else:
                errors_item = errors_item_data.to_dict()

            errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.assignments_responses_create_contents_index_content_error_component import (
            AssignmentsResponsesCreateContentsINDEXContentErrorComponent,
        )
        from ..models.assignments_responses_create_contents_index_field_error_component import (
            AssignmentsResponsesCreateContentsINDEXFieldErrorComponent,
        )
        from ..models.assignments_responses_create_contents_index_non_field_errors_error_component import (
            AssignmentsResponsesCreateContentsINDEXNonFieldErrorsErrorComponent,
        )
        from ..models.assignments_responses_create_contents_non_field_errors_error_component import (
            AssignmentsResponsesCreateContentsNonFieldErrorsErrorComponent,
        )
        from ..models.assignments_responses_create_dear_student_error_component import (
            AssignmentsResponsesCreateDearStudentErrorComponent,
        )
        from ..models.assignments_responses_create_file_error_component import (
            AssignmentsResponsesCreateFileErrorComponent,
        )
        from ..models.assignments_responses_create_file_name_error_component import (
            AssignmentsResponsesCreateFileNameErrorComponent,
        )
        from ..models.assignments_responses_create_hide_checker_name_error_component import (
            AssignmentsResponsesCreateHideCheckerNameErrorComponent,
        )
        from ..models.assignments_responses_create_non_field_errors_error_component import (
            AssignmentsResponsesCreateNonFieldErrorsErrorComponent,
        )
        from ..models.assignments_responses_create_response_type_error_component import (
            AssignmentsResponsesCreateResponseTypeErrorComponent,
        )
        from ..models.assignments_responses_create_segel_only_error_component import (
            AssignmentsResponsesCreateSegelOnlyErrorComponent,
        )

        d = dict(src_dict)
        type_ = ValidationErrorEnum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> Union[
                "AssignmentsResponsesCreateContentsINDEXContentErrorComponent",
                "AssignmentsResponsesCreateContentsINDEXFieldErrorComponent",
                "AssignmentsResponsesCreateContentsINDEXNonFieldErrorsErrorComponent",
                "AssignmentsResponsesCreateContentsNonFieldErrorsErrorComponent",
                "AssignmentsResponsesCreateDearStudentErrorComponent",
                "AssignmentsResponsesCreateFileErrorComponent",
                "AssignmentsResponsesCreateFileNameErrorComponent",
                "AssignmentsResponsesCreateHideCheckerNameErrorComponent",
                "AssignmentsResponsesCreateNonFieldErrorsErrorComponent",
                "AssignmentsResponsesCreateResponseTypeErrorComponent",
                "AssignmentsResponsesCreateSegelOnlyErrorComponent",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_responses_create_error_type_0 = (
                        AssignmentsResponsesCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_responses_create_error_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_responses_create_error_type_1 = (
                        AssignmentsResponsesCreateContentsNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_responses_create_error_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_responses_create_error_type_2 = (
                        AssignmentsResponsesCreateContentsINDEXNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_responses_create_error_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_responses_create_error_type_3 = (
                        AssignmentsResponsesCreateContentsINDEXContentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_responses_create_error_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_responses_create_error_type_4 = (
                        AssignmentsResponsesCreateContentsINDEXFieldErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_responses_create_error_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_responses_create_error_type_5 = (
                        AssignmentsResponsesCreateFileNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_responses_create_error_type_5
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_responses_create_error_type_6 = (
                        AssignmentsResponsesCreateFileErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_responses_create_error_type_6
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_responses_create_error_type_7 = (
                        AssignmentsResponsesCreateDearStudentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_responses_create_error_type_7
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_responses_create_error_type_8 = (
                        AssignmentsResponsesCreateHideCheckerNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_responses_create_error_type_8
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_responses_create_error_type_9 = (
                        AssignmentsResponsesCreateSegelOnlyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_responses_create_error_type_9
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_assignments_responses_create_error_type_10 = (
                    AssignmentsResponsesCreateResponseTypeErrorComponent.from_dict(data)
                )

                return componentsschemas_assignments_responses_create_error_type_10

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        assignments_responses_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        assignments_responses_create_validation_error.additional_properties = d
        return assignments_responses_create_validation_error

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
