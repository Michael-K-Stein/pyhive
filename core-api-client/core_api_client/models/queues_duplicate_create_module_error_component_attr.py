from enum import Enum


class QueuesDuplicateCreateModuleErrorComponentAttr(str, Enum):
    MODULE = "module"

    def __str__(self) -> str:
        return str(self.value)
