from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum

if TYPE_CHECKING:
    from ..models.assignments_create_assignment_status_error_component import (
        AssignmentsCreateAssignmentStatusErrorComponent,
    )
    from ..models.assignments_create_description_error_component import AssignmentsCreateDescriptionErrorComponent
    from ..models.assignments_create_flagged_error_component import AssignmentsCreateFlaggedErrorComponent
    from ..models.assignments_create_manual_check_count_error_component import (
        AssignmentsCreateManualCheckCountErrorComponent,
    )
    from ..models.assignments_create_non_field_errors_error_component import (
        AssignmentsCreateNonFieldErrorsErrorComponent,
    )
    from ..models.assignments_create_student_assignment_status_error_component import (
        AssignmentsCreateStudentAssignmentStatusErrorComponent,
    )
    from ..models.assignments_create_submission_count_error_component import (
        AssignmentsCreateSubmissionCountErrorComponent,
    )
    from ..models.assignments_create_timer_error_component import AssignmentsCreateTimerErrorComponent
    from ..models.assignments_create_total_check_count_error_component import (
        AssignmentsCreateTotalCheckCountErrorComponent,
    )


T = TypeVar("T", bound="AssignmentsCreateValidationError")


@_attrs_define
class AssignmentsCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum):
            * `validation_error` - Validation Error
        errors (list[Union['AssignmentsCreateAssignmentStatusErrorComponent',
            'AssignmentsCreateDescriptionErrorComponent', 'AssignmentsCreateFlaggedErrorComponent',
            'AssignmentsCreateManualCheckCountErrorComponent', 'AssignmentsCreateNonFieldErrorsErrorComponent',
            'AssignmentsCreateStudentAssignmentStatusErrorComponent', 'AssignmentsCreateSubmissionCountErrorComponent',
            'AssignmentsCreateTimerErrorComponent', 'AssignmentsCreateTotalCheckCountErrorComponent']]):
    """

    type_: ValidationErrorEnum
    errors: list[
        Union[
            "AssignmentsCreateAssignmentStatusErrorComponent",
            "AssignmentsCreateDescriptionErrorComponent",
            "AssignmentsCreateFlaggedErrorComponent",
            "AssignmentsCreateManualCheckCountErrorComponent",
            "AssignmentsCreateNonFieldErrorsErrorComponent",
            "AssignmentsCreateStudentAssignmentStatusErrorComponent",
            "AssignmentsCreateSubmissionCountErrorComponent",
            "AssignmentsCreateTimerErrorComponent",
            "AssignmentsCreateTotalCheckCountErrorComponent",
        ]
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.assignments_create_assignment_status_error_component import (
            AssignmentsCreateAssignmentStatusErrorComponent,
        )
        from ..models.assignments_create_description_error_component import AssignmentsCreateDescriptionErrorComponent
        from ..models.assignments_create_flagged_error_component import AssignmentsCreateFlaggedErrorComponent
        from ..models.assignments_create_manual_check_count_error_component import (
            AssignmentsCreateManualCheckCountErrorComponent,
        )
        from ..models.assignments_create_non_field_errors_error_component import (
            AssignmentsCreateNonFieldErrorsErrorComponent,
        )
        from ..models.assignments_create_student_assignment_status_error_component import (
            AssignmentsCreateStudentAssignmentStatusErrorComponent,
        )
        from ..models.assignments_create_submission_count_error_component import (
            AssignmentsCreateSubmissionCountErrorComponent,
        )
        from ..models.assignments_create_total_check_count_error_component import (
            AssignmentsCreateTotalCheckCountErrorComponent,
        )

        type_ = self.type_.value

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, AssignmentsCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsCreateAssignmentStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsCreateStudentAssignmentStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsCreateSubmissionCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsCreateTotalCheckCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsCreateManualCheckCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsCreateFlaggedErrorComponent):
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
        from ..models.assignments_create_assignment_status_error_component import (
            AssignmentsCreateAssignmentStatusErrorComponent,
        )
        from ..models.assignments_create_description_error_component import AssignmentsCreateDescriptionErrorComponent
        from ..models.assignments_create_flagged_error_component import AssignmentsCreateFlaggedErrorComponent
        from ..models.assignments_create_manual_check_count_error_component import (
            AssignmentsCreateManualCheckCountErrorComponent,
        )
        from ..models.assignments_create_non_field_errors_error_component import (
            AssignmentsCreateNonFieldErrorsErrorComponent,
        )
        from ..models.assignments_create_student_assignment_status_error_component import (
            AssignmentsCreateStudentAssignmentStatusErrorComponent,
        )
        from ..models.assignments_create_submission_count_error_component import (
            AssignmentsCreateSubmissionCountErrorComponent,
        )
        from ..models.assignments_create_timer_error_component import AssignmentsCreateTimerErrorComponent
        from ..models.assignments_create_total_check_count_error_component import (
            AssignmentsCreateTotalCheckCountErrorComponent,
        )

        d = dict(src_dict)
        type_ = ValidationErrorEnum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> Union[
                "AssignmentsCreateAssignmentStatusErrorComponent",
                "AssignmentsCreateDescriptionErrorComponent",
                "AssignmentsCreateFlaggedErrorComponent",
                "AssignmentsCreateManualCheckCountErrorComponent",
                "AssignmentsCreateNonFieldErrorsErrorComponent",
                "AssignmentsCreateStudentAssignmentStatusErrorComponent",
                "AssignmentsCreateSubmissionCountErrorComponent",
                "AssignmentsCreateTimerErrorComponent",
                "AssignmentsCreateTotalCheckCountErrorComponent",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_create_error_type_0 = (
                        AssignmentsCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_create_error_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_create_error_type_1 = (
                        AssignmentsCreateAssignmentStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_create_error_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_create_error_type_2 = (
                        AssignmentsCreateStudentAssignmentStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_create_error_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_create_error_type_3 = (
                        AssignmentsCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_create_error_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_create_error_type_4 = (
                        AssignmentsCreateSubmissionCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_create_error_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_create_error_type_5 = (
                        AssignmentsCreateTotalCheckCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_create_error_type_5
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_create_error_type_6 = (
                        AssignmentsCreateManualCheckCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_create_error_type_6
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_create_error_type_7 = (
                        AssignmentsCreateFlaggedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_create_error_type_7
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_assignments_create_error_type_8 = AssignmentsCreateTimerErrorComponent.from_dict(data)

                return componentsschemas_assignments_create_error_type_8

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        assignments_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        assignments_create_validation_error.additional_properties = d
        return assignments_create_validation_error

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
