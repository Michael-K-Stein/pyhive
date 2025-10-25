from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum

if TYPE_CHECKING:
    from ..models.management_users_list_classes_id_in_error_component import (
        ManagementUsersListClassesIdInErrorComponent,
    )
    from ..models.management_users_list_clearance_in_error_component import ManagementUsersListClearanceInErrorComponent
    from ..models.management_users_list_id_in_error_component import ManagementUsersListIdInErrorComponent
    from ..models.management_users_list_mentor_id_error_component import ManagementUsersListMentorIdErrorComponent
    from ..models.management_users_list_mentor_id_in_error_component import ManagementUsersListMentorIdInErrorComponent
    from ..models.management_users_list_program_checker_id_in_error_component import (
        ManagementUsersListProgramCheckerIdInErrorComponent,
    )
    from ..models.management_users_list_program_id_in_error_component import (
        ManagementUsersListProgramIdInErrorComponent,
    )


T = TypeVar("T", bound="ManagementUsersListValidationError")


@_attrs_define
class ManagementUsersListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum):
            * `validation_error` - Validation Error
        errors (list[Union['ManagementUsersListClassesIdInErrorComponent',
            'ManagementUsersListClearanceInErrorComponent', 'ManagementUsersListIdInErrorComponent',
            'ManagementUsersListMentorIdErrorComponent', 'ManagementUsersListMentorIdInErrorComponent',
            'ManagementUsersListProgramCheckerIdInErrorComponent', 'ManagementUsersListProgramIdInErrorComponent']]):
    """

    type_: ValidationErrorEnum
    errors: list[
        Union[
            "ManagementUsersListClassesIdInErrorComponent",
            "ManagementUsersListClearanceInErrorComponent",
            "ManagementUsersListIdInErrorComponent",
            "ManagementUsersListMentorIdErrorComponent",
            "ManagementUsersListMentorIdInErrorComponent",
            "ManagementUsersListProgramCheckerIdInErrorComponent",
            "ManagementUsersListProgramIdInErrorComponent",
        ]
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.management_users_list_clearance_in_error_component import (
            ManagementUsersListClearanceInErrorComponent,
        )
        from ..models.management_users_list_id_in_error_component import ManagementUsersListIdInErrorComponent
        from ..models.management_users_list_mentor_id_error_component import ManagementUsersListMentorIdErrorComponent
        from ..models.management_users_list_mentor_id_in_error_component import (
            ManagementUsersListMentorIdInErrorComponent,
        )
        from ..models.management_users_list_program_checker_id_in_error_component import (
            ManagementUsersListProgramCheckerIdInErrorComponent,
        )
        from ..models.management_users_list_program_id_in_error_component import (
            ManagementUsersListProgramIdInErrorComponent,
        )

        type_ = self.type_.value

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ManagementUsersListProgramIdInErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersListClearanceInErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersListIdInErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersListMentorIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersListMentorIdInErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ManagementUsersListProgramCheckerIdInErrorComponent):
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
        from ..models.management_users_list_classes_id_in_error_component import (
            ManagementUsersListClassesIdInErrorComponent,
        )
        from ..models.management_users_list_clearance_in_error_component import (
            ManagementUsersListClearanceInErrorComponent,
        )
        from ..models.management_users_list_id_in_error_component import ManagementUsersListIdInErrorComponent
        from ..models.management_users_list_mentor_id_error_component import ManagementUsersListMentorIdErrorComponent
        from ..models.management_users_list_mentor_id_in_error_component import (
            ManagementUsersListMentorIdInErrorComponent,
        )
        from ..models.management_users_list_program_checker_id_in_error_component import (
            ManagementUsersListProgramCheckerIdInErrorComponent,
        )
        from ..models.management_users_list_program_id_in_error_component import (
            ManagementUsersListProgramIdInErrorComponent,
        )

        d = dict(src_dict)
        type_ = ValidationErrorEnum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> Union[
                "ManagementUsersListClassesIdInErrorComponent",
                "ManagementUsersListClearanceInErrorComponent",
                "ManagementUsersListIdInErrorComponent",
                "ManagementUsersListMentorIdErrorComponent",
                "ManagementUsersListMentorIdInErrorComponent",
                "ManagementUsersListProgramCheckerIdInErrorComponent",
                "ManagementUsersListProgramIdInErrorComponent",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_list_error_type_0 = (
                        ManagementUsersListProgramIdInErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_list_error_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_list_error_type_1 = (
                        ManagementUsersListClearanceInErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_list_error_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_list_error_type_2 = (
                        ManagementUsersListIdInErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_list_error_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_list_error_type_3 = (
                        ManagementUsersListMentorIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_list_error_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_list_error_type_4 = (
                        ManagementUsersListMentorIdInErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_list_error_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_management_users_list_error_type_5 = (
                        ManagementUsersListProgramCheckerIdInErrorComponent.from_dict(data)
                    )

                    return componentsschemas_management_users_list_error_type_5
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_management_users_list_error_type_6 = (
                    ManagementUsersListClassesIdInErrorComponent.from_dict(data)
                )

                return componentsschemas_management_users_list_error_type_6

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        management_users_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        management_users_list_validation_error.additional_properties = d
        return management_users_list_validation_error

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
