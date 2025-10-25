from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.exercise_preview_types import ExercisePreviewTypes
from ..models.patbas_enum import PatbasEnum
from ..models.sync_status_enum import SyncStatusEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="Exercise")


@_attrs_define
class Exercise:
    """
    Attributes:
        id (int):
        name (str):
        parent_module (int):
        parent_subject (int):
        parent_module_name (str):
        parent_subject_symbol (str):
        parent_subject_color (str):
        download (bool):
        preview (ExercisePreviewTypes): * `Disabled` - Disabled
            * `Markdown` - Markdown
            * `PDF` - Pdf
        parent_subject_name (str):
        parent_module_order (str):
        order (str):
        tags (list[str]):
        patbas (PatbasEnum):
            * `Never` - Never
            * `On Done` - Ondone
            * `Always` - Always
            * `Staff Only` - Staffonly
        sync_status (SyncStatusEnum):
            * `Creating` - Creating
            * `Deleting` - Deleting
            * `Normal` - Normal
            * `Error` - Error
        sync_message (Union[None, str]):
        segel_path (str): The path that is accessible to staff from their computers
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

    id: int
    name: str
    parent_module: int
    parent_subject: int
    parent_module_name: str
    parent_subject_symbol: str
    parent_subject_color: str
    download: bool
    preview: ExercisePreviewTypes
    parent_subject_name: str
    parent_module_order: str
    order: str
    tags: list[str]
    patbas: PatbasEnum
    sync_status: SyncStatusEnum
    sync_message: Union[None, str]
    segel_path: str
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
        id = self.id

        name = self.name

        parent_module = self.parent_module

        parent_subject = self.parent_subject

        parent_module_name = self.parent_module_name

        parent_subject_symbol = self.parent_subject_symbol

        parent_subject_color = self.parent_subject_color

        download = self.download

        preview = self.preview.value

        parent_subject_name = self.parent_subject_name

        parent_module_order = self.parent_module_order

        order = self.order

        tags = self.tags

        patbas = self.patbas.value

        sync_status = self.sync_status.value

        sync_message: Union[None, str]
        sync_message = self.sync_message

        segel_path = self.segel_path

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
                "id": id,
                "name": name,
                "parent_module": parent_module,
                "parent_subject": parent_subject,
                "parent_module_name": parent_module_name,
                "parent_subject_symbol": parent_subject_symbol,
                "parent_subject_color": parent_subject_color,
                "download": download,
                "preview": preview,
                "parent_subject_name": parent_subject_name,
                "parent_module_order": parent_module_order,
                "order": order,
                "tags": tags,
                "patbas": patbas,
                "sync_status": sync_status,
                "sync_message": sync_message,
                "segel_path": segel_path,
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

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        parent_module = d.pop("parent_module")

        parent_subject = d.pop("parent_subject")

        parent_module_name = d.pop("parent_module_name")

        parent_subject_symbol = d.pop("parent_subject_symbol")

        parent_subject_color = d.pop("parent_subject_color")

        download = d.pop("download")

        preview = ExercisePreviewTypes(d.pop("preview"))

        parent_subject_name = d.pop("parent_subject_name")

        parent_module_order = d.pop("parent_module_order")

        order = d.pop("order")

        tags = cast(list[str], d.pop("tags"))

        patbas = PatbasEnum(d.pop("patbas"))

        sync_status = SyncStatusEnum(d.pop("sync_status"))

        def _parse_sync_message(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        sync_message = _parse_sync_message(d.pop("sync_message"))

        segel_path = d.pop("segel_path")

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

        exercise = cls(
            id=id,
            name=name,
            parent_module=parent_module,
            parent_subject=parent_subject,
            parent_module_name=parent_module_name,
            parent_subject_symbol=parent_subject_symbol,
            parent_subject_color=parent_subject_color,
            download=download,
            preview=preview,
            parent_subject_name=parent_subject_name,
            parent_module_order=parent_module_order,
            order=order,
            tags=tags,
            patbas=patbas,
            sync_status=sync_status,
            sync_message=sync_message,
            segel_path=segel_path,
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

        exercise.additional_properties = d
        return exercise

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
