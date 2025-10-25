from enum import Enum


class QueuesItemsPartialUpdateContinueOnRedoErrorComponentAttr(str, Enum):
    CONTINUE_ON_REDO = "continue_on_redo"

    def __str__(self) -> str:
        return str(self.value)
