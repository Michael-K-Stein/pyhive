from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum

if TYPE_CHECKING:
    from ..models.help_update_exercise_id_error_component import HelpUpdateExerciseIdErrorComponent
    from ..models.help_update_help_type_error_component import HelpUpdateHelpTypeErrorComponent
    from ..models.help_update_non_field_errors_error_component import HelpUpdateNonFieldErrorsErrorComponent
    from ..models.help_update_title_error_component import HelpUpdateTitleErrorComponent
    from ..models.help_update_user_error_component import HelpUpdateUserErrorComponent
    from ..models.help_update_visibility_error_component import HelpUpdateVisibilityErrorComponent


T = TypeVar("T", bound="HelpUpdateValidationError")


@_attrs_define
class HelpUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum):
            * `validation_error` - Validation Error
        errors (list[Union['HelpUpdateExerciseIdErrorComponent', 'HelpUpdateHelpTypeErrorComponent',
            'HelpUpdateNonFieldErrorsErrorComponent', 'HelpUpdateTitleErrorComponent', 'HelpUpdateUserErrorComponent',
            'HelpUpdateVisibilityErrorComponent']]):
    """

    type_: ValidationErrorEnum
    errors: list[
        Union[
            "HelpUpdateExerciseIdErrorComponent",
            "HelpUpdateHelpTypeErrorComponent",
            "HelpUpdateNonFieldErrorsErrorComponent",
            "HelpUpdateTitleErrorComponent",
            "HelpUpdateUserErrorComponent",
            "HelpUpdateVisibilityErrorComponent",
        ]
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.help_update_exercise_id_error_component import HelpUpdateExerciseIdErrorComponent
        from ..models.help_update_help_type_error_component import HelpUpdateHelpTypeErrorComponent
        from ..models.help_update_non_field_errors_error_component import HelpUpdateNonFieldErrorsErrorComponent
        from ..models.help_update_title_error_component import HelpUpdateTitleErrorComponent
        from ..models.help_update_user_error_component import HelpUpdateUserErrorComponent

        type_ = self.type_.value

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, HelpUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, HelpUpdateUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, HelpUpdateTitleErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, HelpUpdateHelpTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, HelpUpdateExerciseIdErrorComponent):
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
        from ..models.help_update_exercise_id_error_component import HelpUpdateExerciseIdErrorComponent
        from ..models.help_update_help_type_error_component import HelpUpdateHelpTypeErrorComponent
        from ..models.help_update_non_field_errors_error_component import HelpUpdateNonFieldErrorsErrorComponent
        from ..models.help_update_title_error_component import HelpUpdateTitleErrorComponent
        from ..models.help_update_user_error_component import HelpUpdateUserErrorComponent
        from ..models.help_update_visibility_error_component import HelpUpdateVisibilityErrorComponent

        d = dict(src_dict)
        type_ = ValidationErrorEnum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> Union[
                "HelpUpdateExerciseIdErrorComponent",
                "HelpUpdateHelpTypeErrorComponent",
                "HelpUpdateNonFieldErrorsErrorComponent",
                "HelpUpdateTitleErrorComponent",
                "HelpUpdateUserErrorComponent",
                "HelpUpdateVisibilityErrorComponent",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_help_update_error_type_0 = HelpUpdateNonFieldErrorsErrorComponent.from_dict(data)

                    return componentsschemas_help_update_error_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_help_update_error_type_1 = HelpUpdateUserErrorComponent.from_dict(data)

                    return componentsschemas_help_update_error_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_help_update_error_type_2 = HelpUpdateTitleErrorComponent.from_dict(data)

                    return componentsschemas_help_update_error_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_help_update_error_type_3 = HelpUpdateHelpTypeErrorComponent.from_dict(data)

                    return componentsschemas_help_update_error_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_help_update_error_type_4 = HelpUpdateExerciseIdErrorComponent.from_dict(data)

                    return componentsschemas_help_update_error_type_4
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_help_update_error_type_5 = HelpUpdateVisibilityErrorComponent.from_dict(data)

                return componentsschemas_help_update_error_type_5

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        help_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        help_update_validation_error.additional_properties = d
        return help_update_validation_error

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
