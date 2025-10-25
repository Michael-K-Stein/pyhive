from enum import Enum


class QueuesItemsCreateSetNestedQueueIdErrorComponentAttr(str, Enum):
    SET_NESTED_QUEUE_ID = "set_nested_queue_id"

    def __str__(self) -> str:
        return str(self.value)
