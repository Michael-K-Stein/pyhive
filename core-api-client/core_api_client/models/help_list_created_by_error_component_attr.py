from enum import Enum


class HelpListCreatedByErrorComponentAttr(str, Enum):
    CREATED_BY = "created_by"

    def __str__(self) -> str:
        return str(self.value)
