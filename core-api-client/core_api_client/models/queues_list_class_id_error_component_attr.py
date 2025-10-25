from enum import Enum


class QueuesListClassIdErrorComponentAttr(str, Enum):
    CLASS_ID = "class__id"

    def __str__(self) -> str:
        return str(self.value)
