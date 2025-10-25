from enum import Enum


class QueuesItemsPartialUpdateOrderErrorComponentAttr(str, Enum):
    ORDER = "order"

    def __str__(self) -> str:
        return str(self.value)
