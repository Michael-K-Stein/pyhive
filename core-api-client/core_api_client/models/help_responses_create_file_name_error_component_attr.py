from enum import Enum


class HelpResponsesCreateFileNameErrorComponentAttr(str, Enum):
    FILE_NAME = "file_name"

    def __str__(self) -> str:
        return str(self.value)
