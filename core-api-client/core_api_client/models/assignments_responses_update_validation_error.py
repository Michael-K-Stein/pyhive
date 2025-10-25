from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum

if TYPE_CHECKING:
    from ..models.assignments_responses_update_contents_index_content_error_component import (
        AssignmentsResponsesUpdateContentsINDEXContentErrorComponent,
    )
    from ..models.assignments_responses_update_contents_index_field_error_component import (
        AssignmentsResponsesUpdateContentsINDEXFieldErrorComponent,
    )
    from ..models.assignments_responses_update_contents_index_non_field_errors_error_component import (
        AssignmentsResponsesUpdateContentsINDEXNonFieldErrorsErrorComponent,
    )
    from ..models.assignments_responses_update_contents_non_field_errors_error_component import (
        AssignmentsResponsesUpdateContentsNonFieldErrorsErrorComponent,
    )
    from ..models.assignments_responses_update_dear_student_error_component import (
        AssignmentsResponsesUpdateDearStudentErrorComponent,
    )
    from ..models.assignments_responses_update_file_error_component import AssignmentsResponsesUpdateFileErrorComponent
    from ..models.assignments_responses_update_file_name_error_component import (
        AssignmentsResponsesUpdateFileNameErrorComponent,
    )
    from ..models.assignments_responses_update_hide_checker_name_error_component import (
        AssignmentsResponsesUpdateHideCheckerNameErrorComponent,
    )
    from ..models.assignments_responses_update_non_field_errors_error_component import (
        AssignmentsResponsesUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.assignments_responses_update_response_type_error_component import (
        AssignmentsResponsesUpdateResponseTypeErrorComponent,
    )
    from ..models.assignments_responses_update_segel_only_error_component import (
        AssignmentsResponsesUpdateSegelOnlyErrorComponent,
    )


T = TypeVar("T", bound="AssignmentsResponsesUpdateValidationError")


@_attrs_define
class AssignmentsResponsesUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum):
            * `validation_error` - Validation Error
        errors (list[Union['AssignmentsResponsesUpdateContentsINDEXContentErrorComponent',
            'AssignmentsResponsesUpdateContentsINDEXFieldErrorComponent',
            'AssignmentsResponsesUpdateContentsINDEXNonFieldErrorsErrorComponent',
            'AssignmentsResponsesUpdateContentsNonFieldErrorsErrorComponent',
            'AssignmentsResponsesUpdateDearStudentErrorComponent', 'AssignmentsResponsesUpdateFileErrorComponent',
            'AssignmentsResponsesUpdateFileNameErrorComponent', 'AssignmentsResponsesUpdateHideCheckerNameErrorComponent',
            'AssignmentsResponsesUpdateNonFieldErrorsErrorComponent',
            'AssignmentsResponsesUpdateResponseTypeErrorComponent', 'AssignmentsResponsesUpdateSegelOnlyErrorComponent']]):
    """

    type_: ValidationErrorEnum
    errors: list[
        Union[
            "AssignmentsResponsesUpdateContentsINDEXContentErrorComponent",
            "AssignmentsResponsesUpdateContentsINDEXFieldErrorComponent",
            "AssignmentsResponsesUpdateContentsINDEXNonFieldErrorsErrorComponent",
            "AssignmentsResponsesUpdateContentsNonFieldErrorsErrorComponent",
            "AssignmentsResponsesUpdateDearStudentErrorComponent",
            "AssignmentsResponsesUpdateFileErrorComponent",
            "AssignmentsResponsesUpdateFileNameErrorComponent",
            "AssignmentsResponsesUpdateHideCheckerNameErrorComponent",
            "AssignmentsResponsesUpdateNonFieldErrorsErrorComponent",
            "AssignmentsResponsesUpdateResponseTypeErrorComponent",
            "AssignmentsResponsesUpdateSegelOnlyErrorComponent",
        ]
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.assignments_responses_update_contents_index_content_error_component import (
            AssignmentsResponsesUpdateContentsINDEXContentErrorComponent,
        )
        from ..models.assignments_responses_update_contents_index_field_error_component import (
            AssignmentsResponsesUpdateContentsINDEXFieldErrorComponent,
        )
        from ..models.assignments_responses_update_contents_index_non_field_errors_error_component import (
            AssignmentsResponsesUpdateContentsINDEXNonFieldErrorsErrorComponent,
        )
        from ..models.assignments_responses_update_contents_non_field_errors_error_component import (
            AssignmentsResponsesUpdateContentsNonFieldErrorsErrorComponent,
        )
        from ..models.assignments_responses_update_dear_student_error_component import (
            AssignmentsResponsesUpdateDearStudentErrorComponent,
        )
        from ..models.assignments_responses_update_file_error_component import (
            AssignmentsResponsesUpdateFileErrorComponent,
        )
        from ..models.assignments_responses_update_file_name_error_component import (
            AssignmentsResponsesUpdateFileNameErrorComponent,
        )
        from ..models.assignments_responses_update_hide_checker_name_error_component import (
            AssignmentsResponsesUpdateHideCheckerNameErrorComponent,
        )
        from ..models.assignments_responses_update_non_field_errors_error_component import (
            AssignmentsResponsesUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.assignments_responses_update_segel_only_error_component import (
            AssignmentsResponsesUpdateSegelOnlyErrorComponent,
        )

        type_ = self.type_.value

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, AssignmentsResponsesUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsResponsesUpdateContentsNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsResponsesUpdateContentsINDEXNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsResponsesUpdateContentsINDEXContentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsResponsesUpdateContentsINDEXFieldErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsResponsesUpdateFileNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsResponsesUpdateFileErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsResponsesUpdateDearStudentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsResponsesUpdateHideCheckerNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsResponsesUpdateSegelOnlyErrorComponent):
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
        from ..models.assignments_responses_update_contents_index_content_error_component import (
            AssignmentsResponsesUpdateContentsINDEXContentErrorComponent,
        )
        from ..models.assignments_responses_update_contents_index_field_error_component import (
            AssignmentsResponsesUpdateContentsINDEXFieldErrorComponent,
        )
        from ..models.assignments_responses_update_contents_index_non_field_errors_error_component import (
            AssignmentsResponsesUpdateContentsINDEXNonFieldErrorsErrorComponent,
        )
        from ..models.assignments_responses_update_contents_non_field_errors_error_component import (
            AssignmentsResponsesUpdateContentsNonFieldErrorsErrorComponent,
        )
        from ..models.assignments_responses_update_dear_student_error_component import (
            AssignmentsResponsesUpdateDearStudentErrorComponent,
        )
        from ..models.assignments_responses_update_file_error_component import (
            AssignmentsResponsesUpdateFileErrorComponent,
        )
        from ..models.assignments_responses_update_file_name_error_component import (
            AssignmentsResponsesUpdateFileNameErrorComponent,
        )
        from ..models.assignments_responses_update_hide_checker_name_error_component import (
            AssignmentsResponsesUpdateHideCheckerNameErrorComponent,
        )
        from ..models.assignments_responses_update_non_field_errors_error_component import (
            AssignmentsResponsesUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.assignments_responses_update_response_type_error_component import (
            AssignmentsResponsesUpdateResponseTypeErrorComponent,
        )
        from ..models.assignments_responses_update_segel_only_error_component import (
            AssignmentsResponsesUpdateSegelOnlyErrorComponent,
        )

        d = dict(src_dict)
        type_ = ValidationErrorEnum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> Union[
                "AssignmentsResponsesUpdateContentsINDEXContentErrorComponent",
                "AssignmentsResponsesUpdateContentsINDEXFieldErrorComponent",
                "AssignmentsResponsesUpdateContentsINDEXNonFieldErrorsErrorComponent",
                "AssignmentsResponsesUpdateContentsNonFieldErrorsErrorComponent",
                "AssignmentsResponsesUpdateDearStudentErrorComponent",
                "AssignmentsResponsesUpdateFileErrorComponent",
                "AssignmentsResponsesUpdateFileNameErrorComponent",
                "AssignmentsResponsesUpdateHideCheckerNameErrorComponent",
                "AssignmentsResponsesUpdateNonFieldErrorsErrorComponent",
                "AssignmentsResponsesUpdateResponseTypeErrorComponent",
                "AssignmentsResponsesUpdateSegelOnlyErrorComponent",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_responses_update_error_type_0 = (
                        AssignmentsResponsesUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_responses_update_error_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_responses_update_error_type_1 = (
                        AssignmentsResponsesUpdateContentsNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_responses_update_error_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_responses_update_error_type_2 = (
                        AssignmentsResponsesUpdateContentsINDEXNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_responses_update_error_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_responses_update_error_type_3 = (
                        AssignmentsResponsesUpdateContentsINDEXContentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_responses_update_error_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_responses_update_error_type_4 = (
                        AssignmentsResponsesUpdateContentsINDEXFieldErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_responses_update_error_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_responses_update_error_type_5 = (
                        AssignmentsResponsesUpdateFileNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_responses_update_error_type_5
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_responses_update_error_type_6 = (
                        AssignmentsResponsesUpdateFileErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_responses_update_error_type_6
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_responses_update_error_type_7 = (
                        AssignmentsResponsesUpdateDearStudentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_responses_update_error_type_7
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_responses_update_error_type_8 = (
                        AssignmentsResponsesUpdateHideCheckerNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_responses_update_error_type_8
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_responses_update_error_type_9 = (
                        AssignmentsResponsesUpdateSegelOnlyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_responses_update_error_type_9
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_assignments_responses_update_error_type_10 = (
                    AssignmentsResponsesUpdateResponseTypeErrorComponent.from_dict(data)
                )

                return componentsschemas_assignments_responses_update_error_type_10

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        assignments_responses_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        assignments_responses_update_validation_error.additional_properties = d
        return assignments_responses_update_validation_error

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
