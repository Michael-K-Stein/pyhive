from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum

if TYPE_CHECKING:
    from ..models.help_responses_update_contents_error_component import HelpResponsesUpdateContentsErrorComponent
    from ..models.help_responses_update_dear_student_error_component import HelpResponsesUpdateDearStudentErrorComponent
    from ..models.help_responses_update_file_error_component import HelpResponsesUpdateFileErrorComponent
    from ..models.help_responses_update_file_name_error_component import HelpResponsesUpdateFileNameErrorComponent
    from ..models.help_responses_update_hide_checker_name_error_component import (
        HelpResponsesUpdateHideCheckerNameErrorComponent,
    )
    from ..models.help_responses_update_non_field_errors_error_component import (
        HelpResponsesUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.help_responses_update_response_type_error_component import (
        HelpResponsesUpdateResponseTypeErrorComponent,
    )
    from ..models.help_responses_update_segel_only_error_component import HelpResponsesUpdateSegelOnlyErrorComponent


T = TypeVar("T", bound="HelpResponsesUpdateValidationError")


@_attrs_define
class HelpResponsesUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum):
            * `validation_error` - Validation Error
        errors (list[Union['HelpResponsesUpdateContentsErrorComponent', 'HelpResponsesUpdateDearStudentErrorComponent',
            'HelpResponsesUpdateFileErrorComponent', 'HelpResponsesUpdateFileNameErrorComponent',
            'HelpResponsesUpdateHideCheckerNameErrorComponent', 'HelpResponsesUpdateNonFieldErrorsErrorComponent',
            'HelpResponsesUpdateResponseTypeErrorComponent', 'HelpResponsesUpdateSegelOnlyErrorComponent']]):
    """

    type_: ValidationErrorEnum
    errors: list[
        Union[
            "HelpResponsesUpdateContentsErrorComponent",
            "HelpResponsesUpdateDearStudentErrorComponent",
            "HelpResponsesUpdateFileErrorComponent",
            "HelpResponsesUpdateFileNameErrorComponent",
            "HelpResponsesUpdateHideCheckerNameErrorComponent",
            "HelpResponsesUpdateNonFieldErrorsErrorComponent",
            "HelpResponsesUpdateResponseTypeErrorComponent",
            "HelpResponsesUpdateSegelOnlyErrorComponent",
        ]
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.help_responses_update_contents_error_component import HelpResponsesUpdateContentsErrorComponent
        from ..models.help_responses_update_dear_student_error_component import (
            HelpResponsesUpdateDearStudentErrorComponent,
        )
        from ..models.help_responses_update_file_error_component import HelpResponsesUpdateFileErrorComponent
        from ..models.help_responses_update_file_name_error_component import HelpResponsesUpdateFileNameErrorComponent
        from ..models.help_responses_update_hide_checker_name_error_component import (
            HelpResponsesUpdateHideCheckerNameErrorComponent,
        )
        from ..models.help_responses_update_non_field_errors_error_component import (
            HelpResponsesUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.help_responses_update_segel_only_error_component import HelpResponsesUpdateSegelOnlyErrorComponent

        type_ = self.type_.value

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, HelpResponsesUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, HelpResponsesUpdateContentsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, HelpResponsesUpdateFileNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, HelpResponsesUpdateFileErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, HelpResponsesUpdateDearStudentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, HelpResponsesUpdateHideCheckerNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, HelpResponsesUpdateSegelOnlyErrorComponent):
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
        from ..models.help_responses_update_contents_error_component import HelpResponsesUpdateContentsErrorComponent
        from ..models.help_responses_update_dear_student_error_component import (
            HelpResponsesUpdateDearStudentErrorComponent,
        )
        from ..models.help_responses_update_file_error_component import HelpResponsesUpdateFileErrorComponent
        from ..models.help_responses_update_file_name_error_component import HelpResponsesUpdateFileNameErrorComponent
        from ..models.help_responses_update_hide_checker_name_error_component import (
            HelpResponsesUpdateHideCheckerNameErrorComponent,
        )
        from ..models.help_responses_update_non_field_errors_error_component import (
            HelpResponsesUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.help_responses_update_response_type_error_component import (
            HelpResponsesUpdateResponseTypeErrorComponent,
        )
        from ..models.help_responses_update_segel_only_error_component import HelpResponsesUpdateSegelOnlyErrorComponent

        d = dict(src_dict)
        type_ = ValidationErrorEnum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> Union[
                "HelpResponsesUpdateContentsErrorComponent",
                "HelpResponsesUpdateDearStudentErrorComponent",
                "HelpResponsesUpdateFileErrorComponent",
                "HelpResponsesUpdateFileNameErrorComponent",
                "HelpResponsesUpdateHideCheckerNameErrorComponent",
                "HelpResponsesUpdateNonFieldErrorsErrorComponent",
                "HelpResponsesUpdateResponseTypeErrorComponent",
                "HelpResponsesUpdateSegelOnlyErrorComponent",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_help_responses_update_error_type_0 = (
                        HelpResponsesUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_help_responses_update_error_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_help_responses_update_error_type_1 = (
                        HelpResponsesUpdateContentsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_help_responses_update_error_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_help_responses_update_error_type_2 = (
                        HelpResponsesUpdateFileNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_help_responses_update_error_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_help_responses_update_error_type_3 = (
                        HelpResponsesUpdateFileErrorComponent.from_dict(data)
                    )

                    return componentsschemas_help_responses_update_error_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_help_responses_update_error_type_4 = (
                        HelpResponsesUpdateDearStudentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_help_responses_update_error_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_help_responses_update_error_type_5 = (
                        HelpResponsesUpdateHideCheckerNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_help_responses_update_error_type_5
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_help_responses_update_error_type_6 = (
                        HelpResponsesUpdateSegelOnlyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_help_responses_update_error_type_6
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_help_responses_update_error_type_7 = (
                    HelpResponsesUpdateResponseTypeErrorComponent.from_dict(data)
                )

                return componentsschemas_help_responses_update_error_type_7

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        help_responses_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        help_responses_update_validation_error.additional_properties = d
        return help_responses_update_validation_error

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
