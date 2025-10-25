from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum

if TYPE_CHECKING:
    from ..models.assignments_list_exercise_id_error_component import AssignmentsListExerciseIdErrorComponent
    from ..models.assignments_list_exercise_parent_module_id_error_component import (
        AssignmentsListExerciseParentModuleIdErrorComponent,
    )
    from ..models.assignments_list_exercise_parent_module_parent_subject_id_error_component import (
        AssignmentsListExerciseParentModuleParentSubjectIdErrorComponent,
    )
    from ..models.assignments_list_exercise_tags_id_in_error_component import (
        AssignmentsListExerciseTagsIdInErrorComponent,
    )
    from ..models.assignments_list_queue_id_error_component import AssignmentsListQueueIdErrorComponent
    from ..models.assignments_list_user_classes_id_error_component import AssignmentsListUserClassesIdErrorComponent
    from ..models.assignments_list_user_classes_id_in_error_component import (
        AssignmentsListUserClassesIdInErrorComponent,
    )
    from ..models.assignments_list_user_id_in_error_component import AssignmentsListUserIdInErrorComponent
    from ..models.assignments_list_user_mentor_id_error_component import AssignmentsListUserMentorIdErrorComponent
    from ..models.assignments_list_user_mentor_id_in_error_component import AssignmentsListUserMentorIdInErrorComponent
    from ..models.assignments_list_user_program_id_in_error_component import (
        AssignmentsListUserProgramIdInErrorComponent,
    )


T = TypeVar("T", bound="AssignmentsListValidationError")


@_attrs_define
class AssignmentsListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum):
            * `validation_error` - Validation Error
        errors (list[Union['AssignmentsListExerciseIdErrorComponent',
            'AssignmentsListExerciseParentModuleIdErrorComponent',
            'AssignmentsListExerciseParentModuleParentSubjectIdErrorComponent',
            'AssignmentsListExerciseTagsIdInErrorComponent', 'AssignmentsListQueueIdErrorComponent',
            'AssignmentsListUserClassesIdErrorComponent', 'AssignmentsListUserClassesIdInErrorComponent',
            'AssignmentsListUserIdInErrorComponent', 'AssignmentsListUserMentorIdErrorComponent',
            'AssignmentsListUserMentorIdInErrorComponent', 'AssignmentsListUserProgramIdInErrorComponent']]):
    """

    type_: ValidationErrorEnum
    errors: list[
        Union[
            "AssignmentsListExerciseIdErrorComponent",
            "AssignmentsListExerciseParentModuleIdErrorComponent",
            "AssignmentsListExerciseParentModuleParentSubjectIdErrorComponent",
            "AssignmentsListExerciseTagsIdInErrorComponent",
            "AssignmentsListQueueIdErrorComponent",
            "AssignmentsListUserClassesIdErrorComponent",
            "AssignmentsListUserClassesIdInErrorComponent",
            "AssignmentsListUserIdInErrorComponent",
            "AssignmentsListUserMentorIdErrorComponent",
            "AssignmentsListUserMentorIdInErrorComponent",
            "AssignmentsListUserProgramIdInErrorComponent",
        ]
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.assignments_list_exercise_id_error_component import AssignmentsListExerciseIdErrorComponent
        from ..models.assignments_list_exercise_parent_module_id_error_component import (
            AssignmentsListExerciseParentModuleIdErrorComponent,
        )
        from ..models.assignments_list_exercise_parent_module_parent_subject_id_error_component import (
            AssignmentsListExerciseParentModuleParentSubjectIdErrorComponent,
        )
        from ..models.assignments_list_queue_id_error_component import AssignmentsListQueueIdErrorComponent
        from ..models.assignments_list_user_classes_id_error_component import AssignmentsListUserClassesIdErrorComponent
        from ..models.assignments_list_user_classes_id_in_error_component import (
            AssignmentsListUserClassesIdInErrorComponent,
        )
        from ..models.assignments_list_user_id_in_error_component import AssignmentsListUserIdInErrorComponent
        from ..models.assignments_list_user_mentor_id_error_component import AssignmentsListUserMentorIdErrorComponent
        from ..models.assignments_list_user_mentor_id_in_error_component import (
            AssignmentsListUserMentorIdInErrorComponent,
        )
        from ..models.assignments_list_user_program_id_in_error_component import (
            AssignmentsListUserProgramIdInErrorComponent,
        )

        type_ = self.type_.value

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, AssignmentsListExerciseIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsListExerciseParentModuleIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsListUserIdInErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsListExerciseParentModuleParentSubjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsListUserClassesIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsListUserClassesIdInErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsListUserMentorIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsListUserMentorIdInErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsListUserProgramIdInErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, AssignmentsListQueueIdErrorComponent):
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
        from ..models.assignments_list_exercise_id_error_component import AssignmentsListExerciseIdErrorComponent
        from ..models.assignments_list_exercise_parent_module_id_error_component import (
            AssignmentsListExerciseParentModuleIdErrorComponent,
        )
        from ..models.assignments_list_exercise_parent_module_parent_subject_id_error_component import (
            AssignmentsListExerciseParentModuleParentSubjectIdErrorComponent,
        )
        from ..models.assignments_list_exercise_tags_id_in_error_component import (
            AssignmentsListExerciseTagsIdInErrorComponent,
        )
        from ..models.assignments_list_queue_id_error_component import AssignmentsListQueueIdErrorComponent
        from ..models.assignments_list_user_classes_id_error_component import AssignmentsListUserClassesIdErrorComponent
        from ..models.assignments_list_user_classes_id_in_error_component import (
            AssignmentsListUserClassesIdInErrorComponent,
        )
        from ..models.assignments_list_user_id_in_error_component import AssignmentsListUserIdInErrorComponent
        from ..models.assignments_list_user_mentor_id_error_component import AssignmentsListUserMentorIdErrorComponent
        from ..models.assignments_list_user_mentor_id_in_error_component import (
            AssignmentsListUserMentorIdInErrorComponent,
        )
        from ..models.assignments_list_user_program_id_in_error_component import (
            AssignmentsListUserProgramIdInErrorComponent,
        )

        d = dict(src_dict)
        type_ = ValidationErrorEnum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> Union[
                "AssignmentsListExerciseIdErrorComponent",
                "AssignmentsListExerciseParentModuleIdErrorComponent",
                "AssignmentsListExerciseParentModuleParentSubjectIdErrorComponent",
                "AssignmentsListExerciseTagsIdInErrorComponent",
                "AssignmentsListQueueIdErrorComponent",
                "AssignmentsListUserClassesIdErrorComponent",
                "AssignmentsListUserClassesIdInErrorComponent",
                "AssignmentsListUserIdInErrorComponent",
                "AssignmentsListUserMentorIdErrorComponent",
                "AssignmentsListUserMentorIdInErrorComponent",
                "AssignmentsListUserProgramIdInErrorComponent",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_list_error_type_0 = AssignmentsListExerciseIdErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_assignments_list_error_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_list_error_type_1 = (
                        AssignmentsListExerciseParentModuleIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_list_error_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_list_error_type_2 = AssignmentsListUserIdInErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_assignments_list_error_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_list_error_type_3 = (
                        AssignmentsListExerciseParentModuleParentSubjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_list_error_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_list_error_type_4 = (
                        AssignmentsListUserClassesIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_list_error_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_list_error_type_5 = (
                        AssignmentsListUserClassesIdInErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_list_error_type_5
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_list_error_type_6 = (
                        AssignmentsListUserMentorIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_list_error_type_6
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_list_error_type_7 = (
                        AssignmentsListUserMentorIdInErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_list_error_type_7
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_list_error_type_8 = (
                        AssignmentsListUserProgramIdInErrorComponent.from_dict(data)
                    )

                    return componentsschemas_assignments_list_error_type_8
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_assignments_list_error_type_9 = AssignmentsListQueueIdErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_assignments_list_error_type_9
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_assignments_list_error_type_10 = (
                    AssignmentsListExerciseTagsIdInErrorComponent.from_dict(data)
                )

                return componentsschemas_assignments_list_error_type_10

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        assignments_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        assignments_list_validation_error.additional_properties = d
        return assignments_list_validation_error

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
