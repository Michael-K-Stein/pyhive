from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum

if TYPE_CHECKING:
    from ..models.tags_update_color_error_component import TagsUpdateColorErrorComponent
    from ..models.tags_update_name_error_component import TagsUpdateNameErrorComponent
    from ..models.tags_update_non_field_errors_error_component import TagsUpdateNonFieldErrorsErrorComponent


T = TypeVar("T", bound="TagsUpdateValidationError")


@_attrs_define
class TagsUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum):
            * `validation_error` - Validation Error
        errors (list[Union['TagsUpdateColorErrorComponent', 'TagsUpdateNameErrorComponent',
            'TagsUpdateNonFieldErrorsErrorComponent']]):
    """

    type_: ValidationErrorEnum
    errors: list[
        Union["TagsUpdateColorErrorComponent", "TagsUpdateNameErrorComponent", "TagsUpdateNonFieldErrorsErrorComponent"]
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.tags_update_name_error_component import TagsUpdateNameErrorComponent
        from ..models.tags_update_non_field_errors_error_component import TagsUpdateNonFieldErrorsErrorComponent

        type_ = self.type_.value

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, TagsUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, TagsUpdateNameErrorComponent):
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
        from ..models.tags_update_color_error_component import TagsUpdateColorErrorComponent
        from ..models.tags_update_name_error_component import TagsUpdateNameErrorComponent
        from ..models.tags_update_non_field_errors_error_component import TagsUpdateNonFieldErrorsErrorComponent

        d = dict(src_dict)
        type_ = ValidationErrorEnum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> Union[
                "TagsUpdateColorErrorComponent",
                "TagsUpdateNameErrorComponent",
                "TagsUpdateNonFieldErrorsErrorComponent",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_tags_update_error_type_0 = TagsUpdateNonFieldErrorsErrorComponent.from_dict(data)

                    return componentsschemas_tags_update_error_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_tags_update_error_type_1 = TagsUpdateNameErrorComponent.from_dict(data)

                    return componentsschemas_tags_update_error_type_1
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_tags_update_error_type_2 = TagsUpdateColorErrorComponent.from_dict(data)

                return componentsschemas_tags_update_error_type_2

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        tags_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        tags_update_validation_error.additional_properties = d
        return tags_update_validation_error

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
