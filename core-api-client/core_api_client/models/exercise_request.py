from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.exercise_preview_types import ExercisePreviewTypes
from ..models.patbas_enum import PatbasEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExerciseRequest")


@_attrs_define
class ExerciseRequest:
    """
    Attributes:
        name (str):
        parent_module (int):
        download (bool):
        preview (ExercisePreviewTypes): * `Disabled` - Disabled
            * `Markdown` - Markdown
            * `PDF` - Pdf
        order (str):
        tags (list[str]):
        patbas (PatbasEnum):
            * `Never` - Never
            * `On Done` - Ondone
            * `Always` - Always
            * `Staff Only` - Staffonly
        patbas_preview (Union[Unset, ExercisePreviewTypes]): * `Disabled` - Disabled
            * `Markdown` - Markdown
            * `PDF` - Pdf
        patbas_download (Union[Unset, bool]):
        is_lecture (Union[Unset, bool]):
        style (Union[None, Unset, str]):
        on_creation_data (Union[Unset, Any]):
        autocheck_tag (Union[None, Unset, str]):
        autodone (Union[Unset, bool]):
        expected_duration (Union[None, Unset, str]):
        segel_brief (Union[Unset, str]):
    """

    name: str
    parent_module: int
    download: bool
    preview: ExercisePreviewTypes
    order: str
    tags: list[str]
    patbas: PatbasEnum
    patbas_preview: Union[Unset, ExercisePreviewTypes] = UNSET
    patbas_download: Union[Unset, bool] = UNSET
    is_lecture: Union[Unset, bool] = UNSET
    style: Union[None, Unset, str] = UNSET
    on_creation_data: Union[Unset, Any] = UNSET
    autocheck_tag: Union[None, Unset, str] = UNSET
    autodone: Union[Unset, bool] = UNSET
    expected_duration: Union[None, Unset, str] = UNSET
    segel_brief: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        parent_module = self.parent_module

        download = self.download

        preview = self.preview.value

        order = self.order

        tags = self.tags

        patbas = self.patbas.value

        patbas_preview: Union[Unset, str] = UNSET
        if not isinstance(self.patbas_preview, Unset):
            patbas_preview = self.patbas_preview.value

        patbas_download = self.patbas_download

        is_lecture = self.is_lecture

        style: Union[None, Unset, str]
        if isinstance(self.style, Unset):
            style = UNSET
        else:
            style = self.style

        on_creation_data = self.on_creation_data

        autocheck_tag: Union[None, Unset, str]
        if isinstance(self.autocheck_tag, Unset):
            autocheck_tag = UNSET
        else:
            autocheck_tag = self.autocheck_tag

        autodone = self.autodone

        expected_duration: Union[None, Unset, str]
        if isinstance(self.expected_duration, Unset):
            expected_duration = UNSET
        else:
            expected_duration = self.expected_duration

        segel_brief = self.segel_brief

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "parent_module": parent_module,
                "download": download,
                "preview": preview,
                "order": order,
                "tags": tags,
                "patbas": patbas,
            }
        )
        if patbas_preview is not UNSET:
            field_dict["patbas_preview"] = patbas_preview
        if patbas_download is not UNSET:
            field_dict["patbas_download"] = patbas_download
        if is_lecture is not UNSET:
            field_dict["is_lecture"] = is_lecture
        if style is not UNSET:
            field_dict["style"] = style
        if on_creation_data is not UNSET:
            field_dict["on_creation_data"] = on_creation_data
        if autocheck_tag is not UNSET:
            field_dict["autocheck_tag"] = autocheck_tag
        if autodone is not UNSET:
            field_dict["autodone"] = autodone
        if expected_duration is not UNSET:
            field_dict["expected_duration"] = expected_duration
        if segel_brief is not UNSET:
            field_dict["segel_brief"] = segel_brief

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("name", (None, str(self.name).encode(), "text/plain")))

        files.append(("parent_module", (None, str(self.parent_module).encode(), "text/plain")))

        files.append(("download", (None, str(self.download).encode(), "text/plain")))

        files.append(("preview", (None, str(self.preview.value).encode(), "text/plain")))

        files.append(("order", (None, str(self.order).encode(), "text/plain")))

        for tags_item_element in self.tags:
            files.append(("tags", (None, str(tags_item_element).encode(), "text/plain")))

        files.append(("patbas", (None, str(self.patbas.value).encode(), "text/plain")))

        if not isinstance(self.patbas_preview, Unset):
            files.append(("patbas_preview", (None, str(self.patbas_preview.value).encode(), "text/plain")))

        if not isinstance(self.patbas_download, Unset):
            files.append(("patbas_download", (None, str(self.patbas_download).encode(), "text/plain")))

        if not isinstance(self.is_lecture, Unset):
            files.append(("is_lecture", (None, str(self.is_lecture).encode(), "text/plain")))

        if not isinstance(self.style, Unset):
            if isinstance(self.style, str):
                files.append(("style", (None, str(self.style).encode(), "text/plain")))
            else:
                files.append(("style", (None, str(self.style).encode(), "text/plain")))

        if not isinstance(self.on_creation_data, Unset):
            files.append(("on_creation_data", (None, str(self.on_creation_data).encode(), "text/plain")))

        if not isinstance(self.autocheck_tag, Unset):
            if isinstance(self.autocheck_tag, str):
                files.append(("autocheck_tag", (None, str(self.autocheck_tag).encode(), "text/plain")))
            else:
                files.append(("autocheck_tag", (None, str(self.autocheck_tag).encode(), "text/plain")))

        if not isinstance(self.autodone, Unset):
            files.append(("autodone", (None, str(self.autodone).encode(), "text/plain")))

        if not isinstance(self.expected_duration, Unset):
            if isinstance(self.expected_duration, str):
                files.append(("expected_duration", (None, str(self.expected_duration).encode(), "text/plain")))
            else:
                files.append(("expected_duration", (None, str(self.expected_duration).encode(), "text/plain")))

        if not isinstance(self.segel_brief, Unset):
            files.append(("segel_brief", (None, str(self.segel_brief).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        parent_module = d.pop("parent_module")

        download = d.pop("download")

        preview = ExercisePreviewTypes(d.pop("preview"))

        order = d.pop("order")

        tags = cast(list[str], d.pop("tags"))

        patbas = PatbasEnum(d.pop("patbas"))

        _patbas_preview = d.pop("patbas_preview", UNSET)
        patbas_preview: Union[Unset, ExercisePreviewTypes]
        if isinstance(_patbas_preview, Unset):
            patbas_preview = UNSET
        else:
            patbas_preview = ExercisePreviewTypes(_patbas_preview)

        patbas_download = d.pop("patbas_download", UNSET)

        is_lecture = d.pop("is_lecture", UNSET)

        def _parse_style(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        style = _parse_style(d.pop("style", UNSET))

        on_creation_data = d.pop("on_creation_data", UNSET)

        def _parse_autocheck_tag(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        autocheck_tag = _parse_autocheck_tag(d.pop("autocheck_tag", UNSET))

        autodone = d.pop("autodone", UNSET)

        def _parse_expected_duration(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        expected_duration = _parse_expected_duration(d.pop("expected_duration", UNSET))

        segel_brief = d.pop("segel_brief", UNSET)

        exercise_request = cls(
            name=name,
            parent_module=parent_module,
            download=download,
            preview=preview,
            order=order,
            tags=tags,
            patbas=patbas,
            patbas_preview=patbas_preview,
            patbas_download=patbas_download,
            is_lecture=is_lecture,
            style=style,
            on_creation_data=on_creation_data,
            autocheck_tag=autocheck_tag,
            autodone=autodone,
            expected_duration=expected_duration,
            segel_brief=segel_brief,
        )

        exercise_request.additional_properties = d
        return exercise_request

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
