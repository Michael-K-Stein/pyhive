from enum import Enum


class QueuesItemsCreateOrderErrorComponentAttr(str, Enum):
    ORDER = "order"

    def __str__(self) -> str:
        return str(self.value)
