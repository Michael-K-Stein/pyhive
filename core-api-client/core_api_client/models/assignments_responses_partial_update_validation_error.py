from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum

if TYPE_CHECKING:
    from ..models.assignments_responses_partial_update_contents_index_content_error_component import (
        AssignmentsResponsesPartialUpdateContentsINDEXContentErrorComponent,
    )
    from ..models.assignments_responses_partial_update_contents_index_field_error_component import (
        AssignmentsResponsesPartialUpdateContentsINDEXFieldErrorComponent,
    )
    from ..models.assignments_responses_partial_update_contents_index_non_field_errors_error_component import (
        AssignmentsResponsesPartialUpdateContentsINDEXNonFieldErrorsErrorComponent,
    )
    from ..models.assignments_responses_partial_update_contents_non_field_errors_error_component import (
        AssignmentsResponsesPartialUpdateContentsNonFieldErrorsErrorComponent,
    )
    from ..models.assignments_responses_partial_update_dear_student_error_component import (
        AssignmentsResponsesPartialUpdateDearStudentErrorComponent,
    )
    from ..models.assignments_responses_partial_update_file_error_component import (
        AssignmentsResponsesPartialUpdateFileErrorComponent,
    )
    from ..models.assignments_responses_partial_update_file_name_error_component import (
        AssignmentsResponsesPartialUpdateFileNameErrorComponent,
    )
    from ..models.assignments_responses_partial_update_hide_checker_name_error_component import (
        AssignmentsResponsesPartialUpdateHideCheckerNameErrorComponent,
    )
    from ..models.assignments_responses_partial_update_non_field_errors_error_component import (
        AssignmentsResponsesPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.assignments_responses_partial_update_response_type_error_component import (
        AssignmentsResponsesPartialUpdateResponseTypeErrorComponent,
    )
    from ..models.assignments_responses_partial_update_segel_only_error_component import (
        AssignmentsResponsesPartialUpdateSegelOnlyErrorComponent,
    )


T = TypeVar("T", bound="AssignmentsResponsesPartialUpdateValidationError")


@_attrs_define
class AssignmentsResponsesPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum):
            * `validation_error` - Validation Error
        errors (list[Union['AssignmentsResponsesPartialUpdateContentsINDEXContentErrorComponent',
            'AssignmentsResponsesPartialUpdateContentsINDEXFieldErrorComponent',
            'AssignmentsResponsesPartialUpdateContentsINDEXNonFieldErrorsErrorComponent',
            'AssignmentsResponsesPartialUpdateContentsNonFieldErrorsErrorComponent',
            'AssignmentsResponsesPartialUpdateDearStudentErrorComponent',
            'AssignmentsResponsesPartialUpdateFileErrorComponent',
            'AssignmentsResponsesPartialUpdateFileNameErrorComponent',
            'AssignmentsResponsesPartialUpdateHideCheckerNameErrorComponent',
            'AssignmentsResponsesPartialUpdateNonFieldErrorsErrorComponent',
            'AssignmentsResponsesPartialUpdateResponseTypeErrorComponent',
            'AssignmentsResponsesPartialUpdateSegelOnlyErrorComponent']]):
    """

    type_: ValidationErrorEnum
    errors: list[
        Union[
            "AssignmentsResponsesPartialUpdateContentsINDEXContentErrorComponent",
            "AssignmentsResponsesPartialUpdateContentsINDEXFieldErrorComponent",
            "AssignmentsResponsesPartialUpdateContentsINDEXNonFieldErrorsErrorComponent",
            "AssignmentsResponsesPartialUpdateContentsNonFieldErrorsErrorComponent",
            "AssignmentsResponsesPartialUpdateDearStudentErrorComponent",
            "AssignmentsResponsesPartialUpdateFileErrorComponent",
            "AssignmentsResponsesPartialUpdateFileNameErrorComponent",
            "AssignmentsResponsesPartialUpdateHideCheckerNameErrorComponent",
            "AssignmentsResponsesPartialUpdateNonFieldErrorsErrorComponent",
            "AssignmentsResponsesPartialUpdateResponseTypeErrorComponent",
            "AssignmentsResponsesPartialUpdateSegelOnlyErrorComponent",
        ]
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.assignments_responses_partial_update_contents_index_content_error_component import (
            AssignmentsResponsesPartialUpdateContentsINDEXContentErrorComponent,
        )
        from ..models.assignments_responses_partial_update_contents_index_field_error_component import (
            AssignmentsResponsesPartialUpdateContentsINDEXFieldErrorComponent,
        )
        from ..models.assignments_responses_partial_update_contents_index_non_field_errors_error_component import (
            AssignmentsResponsesPartialUpdateContentsINDEXNonFieldErrorsErrorComponent,
        )
        from ..models.assignments_responses_partial_update_contents_non_field_errors_error_component import (
            AssignmentsResponsesPartialUpdateContentsNonFieldErrorsErrorComponent,
        )
        from ..models.assignments_responses_partial_update_dear_student_error_component import (
            AssignmentsResponsesPartialUpdateDearStudentErrorComponent,
        )
        from ..models.assignments_responses_partial_update_file_error_component import (
            AssignmentsResponsesPartialUpdateFileErrorComponent,
        )
        from ..models.assignments_responses_partial_update_file_name_error_component import (
            AssignmentsResponsesPartialUpdateFileNameErrorComponent,
        )
        from ..models.assignments_responses_partial_update_hide_checker_name_error_component import (
            AssignmentsResponsesPartialUpdateHideCheckerNameErrorComponent,
        )
        from ..models.assignments_responses_partial_update_non_field_errors_error_component import (
            AssignmentsResponsesPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.assignments_responses_partial_update_segel_only_error_component import (
            AssignmentsResponsesPartialUpdateSegelOnlyErrorComponent,
        )

        type_ = self.type_.value

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, AssignmentsResponsesPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsResponsesPartialUpdateContentsNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, AssignmentsResponsesPartialUpdateContentsINDEXNonFieldErrorsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsResponsesPartialUpdateContentsINDEXContentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsResponsesPartialUpdateContentsINDEXFieldErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsResponsesPartialUpdateFileNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsResponsesPartialUpdateFileErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsResponsesPartialUpdateDearStudentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsResponsesPartialUpdateHideCheckerNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsResponsesPartialUpdateSegelOnlyErrorComponent):
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
        from ..models.assignments_responses_partial_update_contents_index_content_error_component import (
            AssignmentsResponsesPartialUpdateContentsINDEXContentErrorComponent,
        )
        from ..models.assignments_responses_partial_update_contents_index_field_error_component import (
            AssignmentsResponsesPartialUpdateContentsINDEXFieldErrorComponent,
        )
        from ..models.assignments_responses_partial_update_contents_index_non_field_errors_error_component import (
            AssignmentsResponsesPartialUpdateContentsINDEXNonFieldErrorsErrorComponent,
        )
        from ..models.assignments_responses_partial_update_contents_non_field_errors_error_component import (
            AssignmentsResponsesPartialUpdateContentsNonFieldErrorsErrorComponent,
        )
        from ..models.assignments_responses_partial_update_dear_student_error_component import (
            AssignmentsResponsesPartialUpdateDearStudentErrorComponent,
        )
        from ..models.assignments_responses_partial_update_file_error_component import (
            AssignmentsResponsesPartialUpdateFileErrorComponent,
        )
        from ..models.assignments_responses_partial_update_file_name_error_component import (
            AssignmentsResponsesPartialUpdateFileNameErrorComponent,
        )
        from ..models.assignments_responses_partial_update_hide_checker_name_error_component import (
            AssignmentsResponsesPartialUpdateHideCheckerNameErrorComponent,
        )
        from ..models.assignments_responses_partial_update_non_field_errors_error_component import (
            AssignmentsResponsesPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.assignments_responses_partial_update_response_type_error_component import (
            AssignmentsResponsesPartialUpdateResponseTypeErrorComponent,
        )
        from ..models.assignments_responses_partial_update_segel_only_error_component import (
            AssignmentsResponsesPartialUpdateSegelOnlyErrorComponent,
        )

        d = dict(src_dict)
        type_ = ValidationErrorEnum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> Union[
                "AssignmentsResponsesPartialUpdateContentsINDEXContentErrorComponent",
                "AssignmentsResponsesPartialUpdateContentsINDEXFieldErrorComponent",
                "AssignmentsResponsesPartialUpdateContentsINDEXNonFieldErrorsErrorComponent",
                "AssignmentsResponsesPartialUpdateContentsNonFieldErrorsErrorComponent",
                "AssignmentsResponsesPartialUpdateDearStudentErrorComponent",
                "AssignmentsResponsesPartialUpdateFileErrorComponent",
                "AssignmentsResponsesPartialUpdateFileNameErrorComponent",
                "AssignmentsResponsesPartialUpdateHideCheckerNameErrorComponent",
                "AssignmentsResponsesPartialUpdateNonFieldErrorsErrorComponent",
                "AssignmentsResponsesPartialUpdateResponseTypeErrorComponent",
                "AssignmentsResponsesPartialUpdateSegelOnlyErrorComponent",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_responses_partial_update_error_type_0 = (
                        AssignmentsResponsesPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_responses_partial_update_error_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_responses_partial_update_error_type_1 = (
                        AssignmentsResponsesPartialUpdateContentsNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_responses_partial_update_error_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_responses_partial_update_error_type_2 = (
                        AssignmentsResponsesPartialUpdateContentsINDEXNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_responses_partial_update_error_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_responses_partial_update_error_type_3 = (
                        AssignmentsResponsesPartialUpdateContentsINDEXContentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_responses_partial_update_error_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_responses_partial_update_error_type_4 = (
                        AssignmentsResponsesPartialUpdateContentsINDEXFieldErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_responses_partial_update_error_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_responses_partial_update_error_type_5 = (
                        AssignmentsResponsesPartialUpdateFileNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_responses_partial_update_error_type_5
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_responses_partial_update_error_type_6 = (
                        AssignmentsResponsesPartialUpdateFileErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_responses_partial_update_error_type_6
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_responses_partial_update_error_type_7 = (
                        AssignmentsResponsesPartialUpdateDearStudentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_responses_partial_update_error_type_7
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_responses_partial_update_error_type_8 = (
                        AssignmentsResponsesPartialUpdateHideCheckerNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_responses_partial_update_error_type_8
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_responses_partial_update_error_type_9 = (
                        AssignmentsResponsesPartialUpdateSegelOnlyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_responses_partial_update_error_type_9
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_assignments_responses_partial_update_error_type_10 = (
                    AssignmentsResponsesPartialUpdateResponseTypeErrorComponent.from_dict(data)
                )

                return componentsschemas_assignments_responses_partial_update_error_type_10

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        assignments_responses_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        assignments_responses_partial_update_validation_error.additional_properties = d
        return assignments_responses_partial_update_validation_error

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
