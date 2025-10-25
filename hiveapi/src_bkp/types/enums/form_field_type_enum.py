from enum import Enum


class FormFieldTypeEnum(str, Enum):
    MULTIPLE = "multiple"
    MULTIRESPONSE = "multiResponse"
    NUMBER = "number"
    TEXT = "text"

    def __str__(self) -> str:
        return str(self.value)
