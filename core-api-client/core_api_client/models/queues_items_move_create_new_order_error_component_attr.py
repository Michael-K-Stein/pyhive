from enum import Enum


class QueuesItemsMoveCreateNewOrderErrorComponentAttr(str, Enum):
    NEW_ORDER = "new_order"

    def __str__(self) -> str:
        return str(self.value)
