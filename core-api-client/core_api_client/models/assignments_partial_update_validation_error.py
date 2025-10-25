from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum

if TYPE_CHECKING:
    from ..models.assignments_partial_update_assignment_status_error_component import (
        AssignmentsPartialUpdateAssignmentStatusErrorComponent,
    )
    from ..models.assignments_partial_update_description_error_component import (
        AssignmentsPartialUpdateDescriptionErrorComponent,
    )
    from ..models.assignments_partial_update_flagged_error_component import (
        AssignmentsPartialUpdateFlaggedErrorComponent,
    )
    from ..models.assignments_partial_update_manual_check_count_error_component import (
        AssignmentsPartialUpdateManualCheckCountErrorComponent,
    )
    from ..models.assignments_partial_update_non_field_errors_error_component import (
        AssignmentsPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.assignments_partial_update_student_assignment_status_error_component import (
        AssignmentsPartialUpdateStudentAssignmentStatusErrorComponent,
    )
    from ..models.assignments_partial_update_submission_count_error_component import (
        AssignmentsPartialUpdateSubmissionCountErrorComponent,
    )
    from ..models.assignments_partial_update_timer_error_component import AssignmentsPartialUpdateTimerErrorComponent
    from ..models.assignments_partial_update_total_check_count_error_component import (
        AssignmentsPartialUpdateTotalCheckCountErrorComponent,
    )


T = TypeVar("T", bound="AssignmentsPartialUpdateValidationError")


@_attrs_define
class AssignmentsPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum):
            * `validation_error` - Validation Error
        errors (list[Union['AssignmentsPartialUpdateAssignmentStatusErrorComponent',
            'AssignmentsPartialUpdateDescriptionErrorComponent', 'AssignmentsPartialUpdateFlaggedErrorComponent',
            'AssignmentsPartialUpdateManualCheckCountErrorComponent',
            'AssignmentsPartialUpdateNonFieldErrorsErrorComponent',
            'AssignmentsPartialUpdateStudentAssignmentStatusErrorComponent',
            'AssignmentsPartialUpdateSubmissionCountErrorComponent', 'AssignmentsPartialUpdateTimerErrorComponent',
            'AssignmentsPartialUpdateTotalCheckCountErrorComponent']]):
    """

    type_: ValidationErrorEnum
    errors: list[
        Union[
            "AssignmentsPartialUpdateAssignmentStatusErrorComponent",
            "AssignmentsPartialUpdateDescriptionErrorComponent",
            "AssignmentsPartialUpdateFlaggedErrorComponent",
            "AssignmentsPartialUpdateManualCheckCountErrorComponent",
            "AssignmentsPartialUpdateNonFieldErrorsErrorComponent",
            "AssignmentsPartialUpdateStudentAssignmentStatusErrorComponent",
            "AssignmentsPartialUpdateSubmissionCountErrorComponent",
            "AssignmentsPartialUpdateTimerErrorComponent",
            "AssignmentsPartialUpdateTotalCheckCountErrorComponent",
        ]
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.assignments_partial_update_assignment_status_error_component import (
            AssignmentsPartialUpdateAssignmentStatusErrorComponent,
        )
        from ..models.assignments_partial_update_description_error_component import (
            AssignmentsPartialUpdateDescriptionErrorComponent,
        )
        from ..models.assignments_partial_update_flagged_error_component import (
            AssignmentsPartialUpdateFlaggedErrorComponent,
        )
        from ..models.assignments_partial_update_manual_check_count_error_component import (
            AssignmentsPartialUpdateManualCheckCountErrorComponent,
        )
        from ..models.assignments_partial_update_non_field_errors_error_component import (
            AssignmentsPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.assignments_partial_update_student_assignment_status_error_component import (
            AssignmentsPartialUpdateStudentAssignmentStatusErrorComponent,
        )
        from ..models.assignments_partial_update_submission_count_error_component import (
            AssignmentsPartialUpdateSubmissionCountErrorComponent,
        )
        from ..models.assignments_partial_update_total_check_count_error_component import (
            AssignmentsPartialUpdateTotalCheckCountErrorComponent,
        )

        type_ = self.type_.value

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, AssignmentsPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsPartialUpdateAssignmentStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsPartialUpdateStudentAssignmentStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsPartialUpdateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsPartialUpdateSubmissionCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsPartialUpdateTotalCheckCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsPartialUpdateManualCheckCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsPartialUpdateFlaggedErrorComponent):
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
        from ..models.assignments_partial_update_assignment_status_error_component import (
            AssignmentsPartialUpdateAssignmentStatusErrorComponent,
        )
        from ..models.assignments_partial_update_description_error_component import (
            AssignmentsPartialUpdateDescriptionErrorComponent,
        )
        from ..models.assignments_partial_update_flagged_error_component import (
            AssignmentsPartialUpdateFlaggedErrorComponent,
        )
        from ..models.assignments_partial_update_manual_check_count_error_component import (
            AssignmentsPartialUpdateManualCheckCountErrorComponent,
        )
        from ..models.assignments_partial_update_non_field_errors_error_component import (
            AssignmentsPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.assignments_partial_update_student_assignment_status_error_component import (
            AssignmentsPartialUpdateStudentAssignmentStatusErrorComponent,
        )
        from ..models.assignments_partial_update_submission_count_error_component import (
            AssignmentsPartialUpdateSubmissionCountErrorComponent,
        )
        from ..models.assignments_partial_update_timer_error_component import (
            AssignmentsPartialUpdateTimerErrorComponent,
        )
        from ..models.assignments_partial_update_total_check_count_error_component import (
            AssignmentsPartialUpdateTotalCheckCountErrorComponent,
        )

        d = dict(src_dict)
        type_ = ValidationErrorEnum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> Union[
                "AssignmentsPartialUpdateAssignmentStatusErrorComponent",
                "AssignmentsPartialUpdateDescriptionErrorComponent",
                "AssignmentsPartialUpdateFlaggedErrorComponent",
                "AssignmentsPartialUpdateManualCheckCountErrorComponent",
                "AssignmentsPartialUpdateNonFieldErrorsErrorComponent",
                "AssignmentsPartialUpdateStudentAssignmentStatusErrorComponent",
                "AssignmentsPartialUpdateSubmissionCountErrorComponent",
                "AssignmentsPartialUpdateTimerErrorComponent",
                "AssignmentsPartialUpdateTotalCheckCountErrorComponent",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_partial_update_error_type_0 = (
                        AssignmentsPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_partial_update_error_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_partial_update_error_type_1 = (
                        AssignmentsPartialUpdateAssignmentStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_partial_update_error_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_partial_update_error_type_2 = (
                        AssignmentsPartialUpdateStudentAssignmentStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_partial_update_error_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_partial_update_error_type_3 = (
                        AssignmentsPartialUpdateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_partial_update_error_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_partial_update_error_type_4 = (
                        AssignmentsPartialUpdateSubmissionCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_partial_update_error_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_partial_update_error_type_5 = (
                        AssignmentsPartialUpdateTotalCheckCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_partial_update_error_type_5
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_partial_update_error_type_6 = (
                        AssignmentsPartialUpdateManualCheckCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_partial_update_error_type_6
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_partial_update_error_type_7 = (
                        AssignmentsPartialUpdateFlaggedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_partial_update_error_type_7
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_assignments_partial_update_error_type_8 = (
                    AssignmentsPartialUpdateTimerErrorComponent.from_dict(data)
                )

                return componentsschemas_assignments_partial_update_error_type_8

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        assignments_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        assignments_partial_update_validation_error.additional_properties = d
        return assignments_partial_update_validation_error

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
