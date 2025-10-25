from enum import Enum


class QueuesItemsCreateQueueRuleErrorComponentAttr(str, Enum):
    QUEUE_RULE = "queue_rule"

    def __str__(self) -> str:
        return str(self.value)
