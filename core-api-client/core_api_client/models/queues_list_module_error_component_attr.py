from enum import Enum


class QueuesListModuleErrorComponentAttr(str, Enum):
    MODULE = "module"

    def __str__(self) -> str:
        return str(self.value)
