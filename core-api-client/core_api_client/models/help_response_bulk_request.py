from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.help_response_type_enum import HelpResponseTypeEnum
from ..types import UNSET, File, FileTypes, Unset

T = TypeVar("T", bound="HelpResponseBulkRequest")


@_attrs_define
class HelpResponseBulkRequest:
    """
    Attributes:
        response_type (HelpResponseTypeEnum):
            * `Resolve` - Resolve
            * `Open` - Open
            * `Comment` - Comment
        contents (Union[None, Unset, str]):
        file_name (Union[Unset, str]):
        file (Union[File, None, Unset]):
        dear_student (Union[Unset, bool]):  Default: True.
        hide_checker_name (Union[Unset, bool]):
        segel_only (Union[Unset, bool]):
    """

    response_type: HelpResponseTypeEnum
    contents: Union[None, Unset, str] = UNSET
    file_name: Union[Unset, str] = UNSET
    file: Union[File, None, Unset] = UNSET
    dear_student: Union[Unset, bool] = True
    hide_checker_name: Union[Unset, bool] = UNSET
    segel_only: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        response_type = self.response_type.value

        contents: Union[None, Unset, str]
        if isinstance(self.contents, Unset):
            contents = UNSET
        else:
            contents = self.contents

        file_name = self.file_name

        file: Union[FileTypes, None, Unset]
        if isinstance(self.file, Unset):
            file = UNSET
        elif isinstance(self.file, File):
            file = self.file.to_tuple()

        else:
            file = self.file

        dear_student = self.dear_student

        hide_checker_name = self.hide_checker_name

        segel_only = self.segel_only

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "response_type": response_type,
            }
        )
        if contents is not UNSET:
            field_dict["contents"] = contents
        if file_name is not UNSET:
            field_dict["file_name"] = file_name
        if file is not UNSET:
            field_dict["file"] = file
        if dear_student is not UNSET:
            field_dict["dear_student"] = dear_student
        if hide_checker_name is not UNSET:
            field_dict["hide_checker_name"] = hide_checker_name
        if segel_only is not UNSET:
            field_dict["segel_only"] = segel_only

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("response_type", (None, str(self.response_type.value).encode(), "text/plain")))

        if not isinstance(self.contents, Unset):
            if isinstance(self.contents, str):
                files.append(("contents", (None, str(self.contents).encode(), "text/plain")))
            else:
                files.append(("contents", (None, str(self.contents).encode(), "text/plain")))

        if not isinstance(self.file_name, Unset):
            files.append(("file_name", (None, str(self.file_name).encode(), "text/plain")))

        if not isinstance(self.file, Unset):
            if isinstance(self.file, File):
                files.append(("file", self.file.to_tuple()))
            else:
                files.append(("file", (None, str(self.file).encode(), "text/plain")))

        if not isinstance(self.dear_student, Unset):
            files.append(("dear_student", (None, str(self.dear_student).encode(), "text/plain")))

        if not isinstance(self.hide_checker_name, Unset):
            files.append(("hide_checker_name", (None, str(self.hide_checker_name).encode(), "text/plain")))

        if not isinstance(self.segel_only, Unset):
            files.append(("segel_only", (None, str(self.segel_only).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        response_type = HelpResponseTypeEnum(d.pop("response_type"))

        def _parse_contents(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        contents = _parse_contents(d.pop("contents", UNSET))

        file_name = d.pop("file_name", UNSET)

        def _parse_file(data: object) -> Union[File, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, bytes):
                    raise TypeError()
                file_type_0 = File(payload=BytesIO(data))

                return file_type_0
            except:  # noqa: E722
                pass
            return cast(Union[File, None, Unset], data)

        file = _parse_file(d.pop("file", UNSET))

        dear_student = d.pop("dear_student", UNSET)

        hide_checker_name = d.pop("hide_checker_name", UNSET)

        segel_only = d.pop("segel_only", UNSET)

        help_response_bulk_request = cls(
            response_type=response_type,
            contents=contents,
            file_name=file_name,
            file=file,
            dear_student=dear_student,
            hide_checker_name=hide_checker_name,
            segel_only=segel_only,
        )

        help_response_bulk_request.additional_properties = d
        return help_response_bulk_request

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
