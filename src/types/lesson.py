from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from client import HiveClient
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from src.common import UNSET, Unset

T = TypeVar("T", bound="Lesson")


@_attrs_define
class Lesson:
    """
    Attributes:
        id (int):
        name (str):
        module (int):
        module_order (str):
        module_name (str):
        subject_symbol (str):
        subject_name (str):
        program_name (str):
        description (Union[None, Unset, str]):
    """

    hive_client: "HiveClient"
    id: int
    name: str
    module: int
    module_order: str
    module_name: str
    subject_symbol: str
    subject_name: str
    program_name: str
    description: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        module = self.module

        module_order = self.module_order

        module_name = self.module_name

        subject_symbol = self.subject_symbol

        subject_name = self.subject_name

        program_name = self.program_name

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "module": module,
                "module_order": module_order,
                "module_name": module_name,
                "subject_symbol": subject_symbol,
                "subject_name": subject_name,
                "program_name": program_name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any], hive_client: "HiveClient") -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        module = d.pop("module")

        module_order = d.pop("module_order")

        module_name = d.pop("module_name")

        subject_symbol = d.pop("subject_symbol")

        subject_name = d.pop("subject_name")

        program_name = d.pop("program_name")

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        lesson = cls(
            hive_client=hive_client,
            id=id,
            name=name,
            module=module,
            module_order=module_order,
            module_name=module_name,
            subject_symbol=subject_symbol,
            subject_name=subject_name,
            program_name=program_name,
            description=description,
        )

        lesson.additional_properties = d
        return lesson

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
