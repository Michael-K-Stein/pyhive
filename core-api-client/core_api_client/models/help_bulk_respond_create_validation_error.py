from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum

if TYPE_CHECKING:
    from ..models.help_bulk_respond_create_contents_error_component import HelpBulkRespondCreateContentsErrorComponent
    from ..models.help_bulk_respond_create_dear_student_error_component import (
        HelpBulkRespondCreateDearStudentErrorComponent,
    )
    from ..models.help_bulk_respond_create_file_error_component import HelpBulkRespondCreateFileErrorComponent
    from ..models.help_bulk_respond_create_file_name_error_component import HelpBulkRespondCreateFileNameErrorComponent
    from ..models.help_bulk_respond_create_hide_checker_name_error_component import (
        HelpBulkRespondCreateHideCheckerNameErrorComponent,
    )
    from ..models.help_bulk_respond_create_non_field_errors_error_component import (
        HelpBulkRespondCreateNonFieldErrorsErrorComponent,
    )
    from ..models.help_bulk_respond_create_response_type_error_component import (
        HelpBulkRespondCreateResponseTypeErrorComponent,
    )
    from ..models.help_bulk_respond_create_segel_only_error_component import (
        HelpBulkRespondCreateSegelOnlyErrorComponent,
    )


T = TypeVar("T", bound="HelpBulkRespondCreateValidationError")


@_attrs_define
class HelpBulkRespondCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum):
            * `validation_error` - Validation Error
        errors (list[Union['HelpBulkRespondCreateContentsErrorComponent',
            'HelpBulkRespondCreateDearStudentErrorComponent', 'HelpBulkRespondCreateFileErrorComponent',
            'HelpBulkRespondCreateFileNameErrorComponent', 'HelpBulkRespondCreateHideCheckerNameErrorComponent',
            'HelpBulkRespondCreateNonFieldErrorsErrorComponent', 'HelpBulkRespondCreateResponseTypeErrorComponent',
            'HelpBulkRespondCreateSegelOnlyErrorComponent']]):
    """

    type_: ValidationErrorEnum
    errors: list[
        Union[
            "HelpBulkRespondCreateContentsErrorComponent",
            "HelpBulkRespondCreateDearStudentErrorComponent",
            "HelpBulkRespondCreateFileErrorComponent",
            "HelpBulkRespondCreateFileNameErrorComponent",
            "HelpBulkRespondCreateHideCheckerNameErrorComponent",
            "HelpBulkRespondCreateNonFieldErrorsErrorComponent",
            "HelpBulkRespondCreateResponseTypeErrorComponent",
            "HelpBulkRespondCreateSegelOnlyErrorComponent",
        ]
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.help_bulk_respond_create_contents_error_component import (
            HelpBulkRespondCreateContentsErrorComponent,
        )
        from ..models.help_bulk_respond_create_dear_student_error_component import (
            HelpBulkRespondCreateDearStudentErrorComponent,
        )
        from ..models.help_bulk_respond_create_file_error_component import HelpBulkRespondCreateFileErrorComponent
        from ..models.help_bulk_respond_create_file_name_error_component import (
            HelpBulkRespondCreateFileNameErrorComponent,
        )
        from ..models.help_bulk_respond_create_hide_checker_name_error_component import (
            HelpBulkRespondCreateHideCheckerNameErrorComponent,
        )
        from ..models.help_bulk_respond_create_non_field_errors_error_component import (
            HelpBulkRespondCreateNonFieldErrorsErrorComponent,
        )
        from ..models.help_bulk_respond_create_segel_only_error_component import (
            HelpBulkRespondCreateSegelOnlyErrorComponent,
        )

        type_ = self.type_.value

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, HelpBulkRespondCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, HelpBulkRespondCreateContentsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, HelpBulkRespondCreateFileNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, HelpBulkRespondCreateFileErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, HelpBulkRespondCreateDearStudentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, HelpBulkRespondCreateHideCheckerNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, HelpBulkRespondCreateSegelOnlyErrorComponent):
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
        from ..models.help_bulk_respond_create_contents_error_component import (
            HelpBulkRespondCreateContentsErrorComponent,
        )
        from ..models.help_bulk_respond_create_dear_student_error_component import (
            HelpBulkRespondCreateDearStudentErrorComponent,
        )
        from ..models.help_bulk_respond_create_file_error_component import HelpBulkRespondCreateFileErrorComponent
        from ..models.help_bulk_respond_create_file_name_error_component import (
            HelpBulkRespondCreateFileNameErrorComponent,
        )
        from ..models.help_bulk_respond_create_hide_checker_name_error_component import (
            HelpBulkRespondCreateHideCheckerNameErrorComponent,
        )
        from ..models.help_bulk_respond_create_non_field_errors_error_component import (
            HelpBulkRespondCreateNonFieldErrorsErrorComponent,
        )
        from ..models.help_bulk_respond_create_response_type_error_component import (
            HelpBulkRespondCreateResponseTypeErrorComponent,
        )
        from ..models.help_bulk_respond_create_segel_only_error_component import (
            HelpBulkRespondCreateSegelOnlyErrorComponent,
        )

        d = dict(src_dict)
        type_ = ValidationErrorEnum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> Union[
                "HelpBulkRespondCreateContentsErrorComponent",
                "HelpBulkRespondCreateDearStudentErrorComponent",
                "HelpBulkRespondCreateFileErrorComponent",
                "HelpBulkRespondCreateFileNameErrorComponent",
                "HelpBulkRespondCreateHideCheckerNameErrorComponent",
                "HelpBulkRespondCreateNonFieldErrorsErrorComponent",
                "HelpBulkRespondCreateResponseTypeErrorComponent",
                "HelpBulkRespondCreateSegelOnlyErrorComponent",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_help_bulk_respond_create_error_type_0 = (
                        HelpBulkRespondCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_help_bulk_respond_create_error_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_help_bulk_respond_create_error_type_1 = (
                        HelpBulkRespondCreateContentsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_help_bulk_respond_create_error_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_help_bulk_respond_create_error_type_2 = (
                        HelpBulkRespondCreateFileNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_help_bulk_respond_create_error_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_help_bulk_respond_create_error_type_3 = (
                        HelpBulkRespondCreateFileErrorComponent.from_dict(data)
                    )

                    return componentsschemas_help_bulk_respond_create_error_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_help_bulk_respond_create_error_type_4 = (
                        HelpBulkRespondCreateDearStudentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_help_bulk_respond_create_error_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_help_bulk_respond_create_error_type_5 = (
                        HelpBulkRespondCreateHideCheckerNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_help_bulk_respond_create_error_type_5
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_help_bulk_respond_create_error_type_6 = (
                        HelpBulkRespondCreateSegelOnlyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_help_bulk_respond_create_error_type_6
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_help_bulk_respond_create_error_type_7 = (
                    HelpBulkRespondCreateResponseTypeErrorComponent.from_dict(data)
                )

                return componentsschemas_help_bulk_respond_create_error_type_7

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        help_bulk_respond_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        help_bulk_respond_create_validation_error.additional_properties = d
        return help_bulk_respond_create_validation_error

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
