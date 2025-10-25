from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.exercise_preview_types import ExercisePreviewTypes
from ..models.patbas_enum import PatbasEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedExerciseRequest")


@_attrs_define
class PatchedExerciseRequest:
    """
    Attributes:
        name (Union[Unset, str]):
        parent_module (Union[Unset, int]):
        download (Union[Unset, bool]):
        preview (Union[Unset, ExercisePreviewTypes]): * `Disabled` - Disabled
            * `Markdown` - Markdown
            * `PDF` - Pdf
        patbas_preview (Union[Unset, ExercisePreviewTypes]): * `Disabled` - Disabled
            * `Markdown` - Markdown
            * `PDF` - Pdf
        patbas_download (Union[Unset, bool]):
        is_lecture (Union[Unset, bool]):
        style (Union[None, Unset, str]):
        order (Union[Unset, str]):
        tags (Union[Unset, list[str]]):
        patbas (Union[Unset, PatbasEnum]): * `Never` - Never
            * `On Done` - Ondone
            * `Always` - Always
            * `Staff Only` - Staffonly
        on_creation_data (Union[Unset, Any]):
        autocheck_tag (Union[None, Unset, str]):
        autodone (Union[Unset, bool]):
        expected_duration (Union[None, Unset, str]):
        segel_brief (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    parent_module: Union[Unset, int] = UNSET
    download: Union[Unset, bool] = UNSET
    preview: Union[Unset, ExercisePreviewTypes] = UNSET
    patbas_preview: Union[Unset, ExercisePreviewTypes] = UNSET
    patbas_download: Union[Unset, bool] = UNSET
    is_lecture: Union[Unset, bool] = UNSET
    style: Union[None, Unset, str] = UNSET
    order: Union[Unset, str] = UNSET
    tags: Union[Unset, list[str]] = UNSET
    patbas: Union[Unset, PatbasEnum] = UNSET
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

        preview: Union[Unset, str] = UNSET
        if not isinstance(self.preview, Unset):
            preview = self.preview.value

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

        order = self.order

        tags: Union[Unset, list[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        patbas: Union[Unset, str] = UNSET
        if not isinstance(self.patbas, Unset):
            patbas = self.patbas.value

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
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if parent_module is not UNSET:
            field_dict["parent_module"] = parent_module
        if download is not UNSET:
            field_dict["download"] = download
        if preview is not UNSET:
            field_dict["preview"] = preview
        if patbas_preview is not UNSET:
            field_dict["patbas_preview"] = patbas_preview
        if patbas_download is not UNSET:
            field_dict["patbas_download"] = patbas_download
        if is_lecture is not UNSET:
            field_dict["is_lecture"] = is_lecture
        if style is not UNSET:
            field_dict["style"] = style
        if order is not UNSET:
            field_dict["order"] = order
        if tags is not UNSET:
            field_dict["tags"] = tags
        if patbas is not UNSET:
            field_dict["patbas"] = patbas
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

        if not isinstance(self.name, Unset):
            files.append(("name", (None, str(self.name).encode(), "text/plain")))

        if not isinstance(self.parent_module, Unset):
            files.append(("parent_module", (None, str(self.parent_module).encode(), "text/plain")))

        if not isinstance(self.download, Unset):
            files.append(("download", (None, str(self.download).encode(), "text/plain")))

        if not isinstance(self.preview, Unset):
            files.append(("preview", (None, str(self.preview.value).encode(), "text/plain")))

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

        if not isinstance(self.order, Unset):
            files.append(("order", (None, str(self.order).encode(), "text/plain")))

        if not isinstance(self.tags, Unset):
            for tags_item_element in self.tags:
                files.append(("tags", (None, str(tags_item_element).encode(), "text/plain")))

        if not isinstance(self.patbas, Unset):
            files.append(("patbas", (None, str(self.patbas.value).encode(), "text/plain")))

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
        name = d.pop("name", UNSET)

        parent_module = d.pop("parent_module", UNSET)

        download = d.pop("download", UNSET)

        _preview = d.pop("preview", UNSET)
        preview: Union[Unset, ExercisePreviewTypes]
        if isinstance(_preview, Unset):
            preview = UNSET
        else:
            preview = ExercisePreviewTypes(_preview)

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

        order = d.pop("order", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        _patbas = d.pop("patbas", UNSET)
        patbas: Union[Unset, PatbasEnum]
        if isinstance(_patbas, Unset):
            patbas = UNSET
        else:
            patbas = PatbasEnum(_patbas)

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

        patched_exercise_request = cls(
            name=name,
            parent_module=parent_module,
            download=download,
            preview=preview,
            patbas_preview=patbas_preview,
            patbas_download=patbas_download,
            is_lecture=is_lecture,
            style=style,
            order=order,
            tags=tags,
            patbas=patbas,
            on_creation_data=on_creation_data,
            autocheck_tag=autocheck_tag,
            autodone=autodone,
            expected_duration=expected_duration,
            segel_brief=segel_brief,
        )

        patched_exercise_request.additional_properties = d
        return patched_exercise_request

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
