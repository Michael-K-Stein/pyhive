from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum

if TYPE_CHECKING:
    from ..models.help_responses_create_contents_error_component import HelpResponsesCreateContentsErrorComponent
    from ..models.help_responses_create_dear_student_error_component import HelpResponsesCreateDearStudentErrorComponent
    from ..models.help_responses_create_file_error_component import HelpResponsesCreateFileErrorComponent
    from ..models.help_responses_create_file_name_error_component import HelpResponsesCreateFileNameErrorComponent
    from ..models.help_responses_create_hide_checker_name_error_component import (
        HelpResponsesCreateHideCheckerNameErrorComponent,
    )
    from ..models.help_responses_create_non_field_errors_error_component import (
        HelpResponsesCreateNonFieldErrorsErrorComponent,
    )
    from ..models.help_responses_create_response_type_error_component import (
        HelpResponsesCreateResponseTypeErrorComponent,
    )
    from ..models.help_responses_create_segel_only_error_component import HelpResponsesCreateSegelOnlyErrorComponent


T = TypeVar("T", bound="HelpResponsesCreateValidationError")


@_attrs_define
class HelpResponsesCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum):
            * `validation_error` - Validation Error
        errors (list[Union['HelpResponsesCreateContentsErrorComponent', 'HelpResponsesCreateDearStudentErrorComponent',
            'HelpResponsesCreateFileErrorComponent', 'HelpResponsesCreateFileNameErrorComponent',
            'HelpResponsesCreateHideCheckerNameErrorComponent', 'HelpResponsesCreateNonFieldErrorsErrorComponent',
            'HelpResponsesCreateResponseTypeErrorComponent', 'HelpResponsesCreateSegelOnlyErrorComponent']]):
    """

    type_: ValidationErrorEnum
    errors: list[
        Union[
            "HelpResponsesCreateContentsErrorComponent",
            "HelpResponsesCreateDearStudentErrorComponent",
            "HelpResponsesCreateFileErrorComponent",
            "HelpResponsesCreateFileNameErrorComponent",
            "HelpResponsesCreateHideCheckerNameErrorComponent",
            "HelpResponsesCreateNonFieldErrorsErrorComponent",
            "HelpResponsesCreateResponseTypeErrorComponent",
            "HelpResponsesCreateSegelOnlyErrorComponent",
        ]
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.help_responses_create_contents_error_component import HelpResponsesCreateContentsErrorComponent
        from ..models.help_responses_create_dear_student_error_component import (
            HelpResponsesCreateDearStudentErrorComponent,
        )
        from ..models.help_responses_create_file_error_component import HelpResponsesCreateFileErrorComponent
        from ..models.help_responses_create_file_name_error_component import HelpResponsesCreateFileNameErrorComponent
        from ..models.help_responses_create_hide_checker_name_error_component import (
            HelpResponsesCreateHideCheckerNameErrorComponent,
        )
        from ..models.help_responses_create_non_field_errors_error_component import (
            HelpResponsesCreateNonFieldErrorsErrorComponent,
        )
        from ..models.help_responses_create_segel_only_error_component import HelpResponsesCreateSegelOnlyErrorComponent

        type_ = self.type_.value

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, HelpResponsesCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, HelpResponsesCreateContentsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, HelpResponsesCreateFileNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, HelpResponsesCreateFileErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, HelpResponsesCreateDearStudentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, HelpResponsesCreateHideCheckerNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, HelpResponsesCreateSegelOnlyErrorComponent):
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
        from ..models.help_responses_create_contents_error_component import HelpResponsesCreateContentsErrorComponent
        from ..models.help_responses_create_dear_student_error_component import (
            HelpResponsesCreateDearStudentErrorComponent,
        )
        from ..models.help_responses_create_file_error_component import HelpResponsesCreateFileErrorComponent
        from ..models.help_responses_create_file_name_error_component import HelpResponsesCreateFileNameErrorComponent
        from ..models.help_responses_create_hide_checker_name_error_component import (
            HelpResponsesCreateHideCheckerNameErrorComponent,
        )
        from ..models.help_responses_create_non_field_errors_error_component import (
            HelpResponsesCreateNonFieldErrorsErrorComponent,
        )
        from ..models.help_responses_create_response_type_error_component import (
            HelpResponsesCreateResponseTypeErrorComponent,
        )
        from ..models.help_responses_create_segel_only_error_component import HelpResponsesCreateSegelOnlyErrorComponent

        d = dict(src_dict)
        type_ = ValidationErrorEnum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> Union[
                "HelpResponsesCreateContentsErrorComponent",
                "HelpResponsesCreateDearStudentErrorComponent",
                "HelpResponsesCreateFileErrorComponent",
                "HelpResponsesCreateFileNameErrorComponent",
                "HelpResponsesCreateHideCheckerNameErrorComponent",
                "HelpResponsesCreateNonFieldErrorsErrorComponent",
                "HelpResponsesCreateResponseTypeErrorComponent",
                "HelpResponsesCreateSegelOnlyErrorComponent",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_help_responses_create_error_type_0 = (
                        HelpResponsesCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_help_responses_create_error_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_help_responses_create_error_type_1 = (
                        HelpResponsesCreateContentsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_help_responses_create_error_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_help_responses_create_error_type_2 = (
                        HelpResponsesCreateFileNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_help_responses_create_error_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_help_responses_create_error_type_3 = (
                        HelpResponsesCreateFileErrorComponent.from_dict(data)
                    )

                    return componentsschemas_help_responses_create_error_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_help_responses_create_error_type_4 = (
                        HelpResponsesCreateDearStudentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_help_responses_create_error_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_help_responses_create_error_type_5 = (
                        HelpResponsesCreateHideCheckerNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_help_responses_create_error_type_5
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_help_responses_create_error_type_6 = (
                        HelpResponsesCreateSegelOnlyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_help_responses_create_error_type_6
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_help_responses_create_error_type_7 = (
                    HelpResponsesCreateResponseTypeErrorComponent.from_dict(data)
                )

                return componentsschemas_help_responses_create_error_type_7

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        help_responses_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        help_responses_create_validation_error.additional_properties = d
        return help_responses_create_validation_error

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
