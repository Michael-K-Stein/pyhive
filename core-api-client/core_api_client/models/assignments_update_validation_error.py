from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum

if TYPE_CHECKING:
    from ..models.assignments_update_assignment_status_error_component import (
        AssignmentsUpdateAssignmentStatusErrorComponent,
    )
    from ..models.assignments_update_description_error_component import AssignmentsUpdateDescriptionErrorComponent
    from ..models.assignments_update_flagged_error_component import AssignmentsUpdateFlaggedErrorComponent
    from ..models.assignments_update_manual_check_count_error_component import (
        AssignmentsUpdateManualCheckCountErrorComponent,
    )
    from ..models.assignments_update_non_field_errors_error_component import (
        AssignmentsUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.assignments_update_student_assignment_status_error_component import (
        AssignmentsUpdateStudentAssignmentStatusErrorComponent,
    )
    from ..models.assignments_update_submission_count_error_component import (
        AssignmentsUpdateSubmissionCountErrorComponent,
    )
    from ..models.assignments_update_timer_error_component import AssignmentsUpdateTimerErrorComponent
    from ..models.assignments_update_total_check_count_error_component import (
        AssignmentsUpdateTotalCheckCountErrorComponent,
    )


T = TypeVar("T", bound="AssignmentsUpdateValidationError")


@_attrs_define
class AssignmentsUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum):
            * `validation_error` - Validation Error
        errors (list[Union['AssignmentsUpdateAssignmentStatusErrorComponent',
            'AssignmentsUpdateDescriptionErrorComponent', 'AssignmentsUpdateFlaggedErrorComponent',
            'AssignmentsUpdateManualCheckCountErrorComponent', 'AssignmentsUpdateNonFieldErrorsErrorComponent',
            'AssignmentsUpdateStudentAssignmentStatusErrorComponent', 'AssignmentsUpdateSubmissionCountErrorComponent',
            'AssignmentsUpdateTimerErrorComponent', 'AssignmentsUpdateTotalCheckCountErrorComponent']]):
    """

    type_: ValidationErrorEnum
    errors: list[
        Union[
            "AssignmentsUpdateAssignmentStatusErrorComponent",
            "AssignmentsUpdateDescriptionErrorComponent",
            "AssignmentsUpdateFlaggedErrorComponent",
            "AssignmentsUpdateManualCheckCountErrorComponent",
            "AssignmentsUpdateNonFieldErrorsErrorComponent",
            "AssignmentsUpdateStudentAssignmentStatusErrorComponent",
            "AssignmentsUpdateSubmissionCountErrorComponent",
            "AssignmentsUpdateTimerErrorComponent",
            "AssignmentsUpdateTotalCheckCountErrorComponent",
        ]
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.assignments_update_assignment_status_error_component import (
            AssignmentsUpdateAssignmentStatusErrorComponent,
        )
        from ..models.assignments_update_description_error_component import AssignmentsUpdateDescriptionErrorComponent
        from ..models.assignments_update_flagged_error_component import AssignmentsUpdateFlaggedErrorComponent
        from ..models.assignments_update_manual_check_count_error_component import (
            AssignmentsUpdateManualCheckCountErrorComponent,
        )
        from ..models.assignments_update_non_field_errors_error_component import (
            AssignmentsUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.assignments_update_student_assignment_status_error_component import (
            AssignmentsUpdateStudentAssignmentStatusErrorComponent,
        )
        from ..models.assignments_update_submission_count_error_component import (
            AssignmentsUpdateSubmissionCountErrorComponent,
        )
        from ..models.assignments_update_total_check_count_error_component import (
            AssignmentsUpdateTotalCheckCountErrorComponent,
        )

        type_ = self.type_.value

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, AssignmentsUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsUpdateAssignmentStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsUpdateStudentAssignmentStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsUpdateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsUpdateSubmissionCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsUpdateTotalCheckCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsUpdateManualCheckCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsUpdateFlaggedErrorComponent):
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
        from ..models.assignments_update_assignment_status_error_component import (
            AssignmentsUpdateAssignmentStatusErrorComponent,
        )
        from ..models.assignments_update_description_error_component import AssignmentsUpdateDescriptionErrorComponent
        from ..models.assignments_update_flagged_error_component import AssignmentsUpdateFlaggedErrorComponent
        from ..models.assignments_update_manual_check_count_error_component import (
            AssignmentsUpdateManualCheckCountErrorComponent,
        )
        from ..models.assignments_update_non_field_errors_error_component import (
            AssignmentsUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.assignments_update_student_assignment_status_error_component import (
            AssignmentsUpdateStudentAssignmentStatusErrorComponent,
        )
        from ..models.assignments_update_submission_count_error_component import (
            AssignmentsUpdateSubmissionCountErrorComponent,
        )
        from ..models.assignments_update_timer_error_component import AssignmentsUpdateTimerErrorComponent
        from ..models.assignments_update_total_check_count_error_component import (
            AssignmentsUpdateTotalCheckCountErrorComponent,
        )

        d = dict(src_dict)
        type_ = ValidationErrorEnum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> Union[
                "AssignmentsUpdateAssignmentStatusErrorComponent",
                "AssignmentsUpdateDescriptionErrorComponent",
                "AssignmentsUpdateFlaggedErrorComponent",
                "AssignmentsUpdateManualCheckCountErrorComponent",
                "AssignmentsUpdateNonFieldErrorsErrorComponent",
                "AssignmentsUpdateStudentAssignmentStatusErrorComponent",
                "AssignmentsUpdateSubmissionCountErrorComponent",
                "AssignmentsUpdateTimerErrorComponent",
                "AssignmentsUpdateTotalCheckCountErrorComponent",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_update_error_type_0 = (
                        AssignmentsUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_update_error_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_update_error_type_1 = (
                        AssignmentsUpdateAssignmentStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_update_error_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_update_error_type_2 = (
                        AssignmentsUpdateStudentAssignmentStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_update_error_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_update_error_type_3 = (
                        AssignmentsUpdateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_update_error_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_update_error_type_4 = (
                        AssignmentsUpdateSubmissionCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_update_error_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_update_error_type_5 = (
                        AssignmentsUpdateTotalCheckCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_update_error_type_5
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_update_error_type_6 = (
                        AssignmentsUpdateManualCheckCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_update_error_type_6
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_update_error_type_7 = (
                        AssignmentsUpdateFlaggedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_update_error_type_7
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_assignments_update_error_type_8 = AssignmentsUpdateTimerErrorComponent.from_dict(data)

                return componentsschemas_assignments_update_error_type_8

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        assignments_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        assignments_update_validation_error.additional_properties = d
        return assignments_update_validation_error

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
