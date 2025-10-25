from enum import Enum


class QueuesUpdateDescriptionErrorComponentAttr(str, Enum):
    DESCRIPTION = "description"

    def __str__(self) -> str:
        return str(self.value)
