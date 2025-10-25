from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum

if TYPE_CHECKING:
    from ..models.help_partial_update_exercise_id_error_component import HelpPartialUpdateExerciseIdErrorComponent
    from ..models.help_partial_update_help_type_error_component import HelpPartialUpdateHelpTypeErrorComponent
    from ..models.help_partial_update_non_field_errors_error_component import (
        HelpPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.help_partial_update_title_error_component import HelpPartialUpdateTitleErrorComponent
    from ..models.help_partial_update_user_error_component import HelpPartialUpdateUserErrorComponent
    from ..models.help_partial_update_visibility_error_component import HelpPartialUpdateVisibilityErrorComponent


T = TypeVar("T", bound="HelpPartialUpdateValidationError")


@_attrs_define
class HelpPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum):
            * `validation_error` - Validation Error
        errors (list[Union['HelpPartialUpdateExerciseIdErrorComponent', 'HelpPartialUpdateHelpTypeErrorComponent',
            'HelpPartialUpdateNonFieldErrorsErrorComponent', 'HelpPartialUpdateTitleErrorComponent',
            'HelpPartialUpdateUserErrorComponent', 'HelpPartialUpdateVisibilityErrorComponent']]):
    """

    type_: ValidationErrorEnum
    errors: list[
        Union[
            "HelpPartialUpdateExerciseIdErrorComponent",
            "HelpPartialUpdateHelpTypeErrorComponent",
            "HelpPartialUpdateNonFieldErrorsErrorComponent",
            "HelpPartialUpdateTitleErrorComponent",
            "HelpPartialUpdateUserErrorComponent",
            "HelpPartialUpdateVisibilityErrorComponent",
        ]
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.help_partial_update_exercise_id_error_component import HelpPartialUpdateExerciseIdErrorComponent
        from ..models.help_partial_update_help_type_error_component import HelpPartialUpdateHelpTypeErrorComponent
        from ..models.help_partial_update_non_field_errors_error_component import (
            HelpPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.help_partial_update_title_error_component import HelpPartialUpdateTitleErrorComponent
        from ..models.help_partial_update_user_error_component import HelpPartialUpdateUserErrorComponent

        type_ = self.type_.value

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, HelpPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, HelpPartialUpdateUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, HelpPartialUpdateTitleErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, HelpPartialUpdateHelpTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, HelpPartialUpdateExerciseIdErrorComponent):
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
        from ..models.help_partial_update_exercise_id_error_component import HelpPartialUpdateExerciseIdErrorComponent
        from ..models.help_partial_update_help_type_error_component import HelpPartialUpdateHelpTypeErrorComponent
        from ..models.help_partial_update_non_field_errors_error_component import (
            HelpPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.help_partial_update_title_error_component import HelpPartialUpdateTitleErrorComponent
        from ..models.help_partial_update_user_error_component import HelpPartialUpdateUserErrorComponent
        from ..models.help_partial_update_visibility_error_component import HelpPartialUpdateVisibilityErrorComponent

        d = dict(src_dict)
        type_ = ValidationErrorEnum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> Union[
                "HelpPartialUpdateExerciseIdErrorComponent",
                "HelpPartialUpdateHelpTypeErrorComponent",
                "HelpPartialUpdateNonFieldErrorsErrorComponent",
                "HelpPartialUpdateTitleErrorComponent",
                "HelpPartialUpdateUserErrorComponent",
                "HelpPartialUpdateVisibilityErrorComponent",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_help_partial_update_error_type_0 = (
                        HelpPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_help_partial_update_error_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_help_partial_update_error_type_1 = HelpPartialUpdateUserErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_help_partial_update_error_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_help_partial_update_error_type_2 = HelpPartialUpdateTitleErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_help_partial_update_error_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_help_partial_update_error_type_3 = (
                        HelpPartialUpdateHelpTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_help_partial_update_error_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_help_partial_update_error_type_4 = (
                        HelpPartialUpdateExerciseIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_help_partial_update_error_type_4
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_help_partial_update_error_type_5 = (
                    HelpPartialUpdateVisibilityErrorComponent.from_dict(data)
                )

                return componentsschemas_help_partial_update_error_type_5

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        help_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        help_partial_update_validation_error.additional_properties = d
        return help_partial_update_validation_error

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
