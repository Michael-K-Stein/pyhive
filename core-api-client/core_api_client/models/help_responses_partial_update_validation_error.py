from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum

if TYPE_CHECKING:
    from ..models.help_responses_partial_update_contents_error_component import (
        HelpResponsesPartialUpdateContentsErrorComponent,
    )
    from ..models.help_responses_partial_update_dear_student_error_component import (
        HelpResponsesPartialUpdateDearStudentErrorComponent,
    )
    from ..models.help_responses_partial_update_file_error_component import HelpResponsesPartialUpdateFileErrorComponent
    from ..models.help_responses_partial_update_file_name_error_component import (
        HelpResponsesPartialUpdateFileNameErrorComponent,
    )
    from ..models.help_responses_partial_update_hide_checker_name_error_component import (
        HelpResponsesPartialUpdateHideCheckerNameErrorComponent,
    )
    from ..models.help_responses_partial_update_non_field_errors_error_component import (
        HelpResponsesPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.help_responses_partial_update_response_type_error_component import (
        HelpResponsesPartialUpdateResponseTypeErrorComponent,
    )
    from ..models.help_responses_partial_update_segel_only_error_component import (
        HelpResponsesPartialUpdateSegelOnlyErrorComponent,
    )


T = TypeVar("T", bound="HelpResponsesPartialUpdateValidationError")


@_attrs_define
class HelpResponsesPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum):
            * `validation_error` - Validation Error
        errors (list[Union['HelpResponsesPartialUpdateContentsErrorComponent',
            'HelpResponsesPartialUpdateDearStudentErrorComponent', 'HelpResponsesPartialUpdateFileErrorComponent',
            'HelpResponsesPartialUpdateFileNameErrorComponent', 'HelpResponsesPartialUpdateHideCheckerNameErrorComponent',
            'HelpResponsesPartialUpdateNonFieldErrorsErrorComponent',
            'HelpResponsesPartialUpdateResponseTypeErrorComponent', 'HelpResponsesPartialUpdateSegelOnlyErrorComponent']]):
    """

    type_: ValidationErrorEnum
    errors: list[
        Union[
            "HelpResponsesPartialUpdateContentsErrorComponent",
            "HelpResponsesPartialUpdateDearStudentErrorComponent",
            "HelpResponsesPartialUpdateFileErrorComponent",
            "HelpResponsesPartialUpdateFileNameErrorComponent",
            "HelpResponsesPartialUpdateHideCheckerNameErrorComponent",
            "HelpResponsesPartialUpdateNonFieldErrorsErrorComponent",
            "HelpResponsesPartialUpdateResponseTypeErrorComponent",
            "HelpResponsesPartialUpdateSegelOnlyErrorComponent",
        ]
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.help_responses_partial_update_contents_error_component import (
            HelpResponsesPartialUpdateContentsErrorComponent,
        )
        from ..models.help_responses_partial_update_dear_student_error_component import (
            HelpResponsesPartialUpdateDearStudentErrorComponent,
        )
        from ..models.help_responses_partial_update_file_error_component import (
            HelpResponsesPartialUpdateFileErrorComponent,
        )
        from ..models.help_responses_partial_update_file_name_error_component import (
            HelpResponsesPartialUpdateFileNameErrorComponent,
        )
        from ..models.help_responses_partial_update_hide_checker_name_error_component import (
            HelpResponsesPartialUpdateHideCheckerNameErrorComponent,
        )
        from ..models.help_responses_partial_update_non_field_errors_error_component import (
            HelpResponsesPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.help_responses_partial_update_segel_only_error_component import (
            HelpResponsesPartialUpdateSegelOnlyErrorComponent,
        )

        type_ = self.type_.value

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, HelpResponsesPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, HelpResponsesPartialUpdateContentsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, HelpResponsesPartialUpdateFileNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, HelpResponsesPartialUpdateFileErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, HelpResponsesPartialUpdateDearStudentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, HelpResponsesPartialUpdateHideCheckerNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, HelpResponsesPartialUpdateSegelOnlyErrorComponent):
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
        from ..models.help_responses_partial_update_contents_error_component import (
            HelpResponsesPartialUpdateContentsErrorComponent,
        )
        from ..models.help_responses_partial_update_dear_student_error_component import (
            HelpResponsesPartialUpdateDearStudentErrorComponent,
        )
        from ..models.help_responses_partial_update_file_error_component import (
            HelpResponsesPartialUpdateFileErrorComponent,
        )
        from ..models.help_responses_partial_update_file_name_error_component import (
            HelpResponsesPartialUpdateFileNameErrorComponent,
        )
        from ..models.help_responses_partial_update_hide_checker_name_error_component import (
            HelpResponsesPartialUpdateHideCheckerNameErrorComponent,
        )
        from ..models.help_responses_partial_update_non_field_errors_error_component import (
            HelpResponsesPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.help_responses_partial_update_response_type_error_component import (
            HelpResponsesPartialUpdateResponseTypeErrorComponent,
        )
        from ..models.help_responses_partial_update_segel_only_error_component import (
            HelpResponsesPartialUpdateSegelOnlyErrorComponent,
        )

        d = dict(src_dict)
        type_ = ValidationErrorEnum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> Union[
                "HelpResponsesPartialUpdateContentsErrorComponent",
                "HelpResponsesPartialUpdateDearStudentErrorComponent",
                "HelpResponsesPartialUpdateFileErrorComponent",
                "HelpResponsesPartialUpdateFileNameErrorComponent",
                "HelpResponsesPartialUpdateHideCheckerNameErrorComponent",
                "HelpResponsesPartialUpdateNonFieldErrorsErrorComponent",
                "HelpResponsesPartialUpdateResponseTypeErrorComponent",
                "HelpResponsesPartialUpdateSegelOnlyErrorComponent",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_help_responses_partial_update_error_type_0 = (
                        HelpResponsesPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_help_responses_partial_update_error_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_help_responses_partial_update_error_type_1 = (
                        HelpResponsesPartialUpdateContentsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_help_responses_partial_update_error_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_help_responses_partial_update_error_type_2 = (
                        HelpResponsesPartialUpdateFileNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_help_responses_partial_update_error_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_help_responses_partial_update_error_type_3 = (
                        HelpResponsesPartialUpdateFileErrorComponent.from_dict(data)
                    )

                    return componentsschemas_help_responses_partial_update_error_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_help_responses_partial_update_error_type_4 = (
                        HelpResponsesPartialUpdateDearStudentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_help_responses_partial_update_error_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_help_responses_partial_update_error_type_5 = (
                        HelpResponsesPartialUpdateHideCheckerNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_help_responses_partial_update_error_type_5
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_help_responses_partial_update_error_type_6 = (
                        HelpResponsesPartialUpdateSegelOnlyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_help_responses_partial_update_error_type_6
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_help_responses_partial_update_error_type_7 = (
                    HelpResponsesPartialUpdateResponseTypeErrorComponent.from_dict(data)
                )

                return componentsschemas_help_responses_partial_update_error_type_7

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        help_responses_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        help_responses_partial_update_validation_error.additional_properties = d
        return help_responses_partial_update_validation_error

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
