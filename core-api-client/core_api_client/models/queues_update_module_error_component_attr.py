from enum import Enum


class QueuesUpdateModuleErrorComponentAttr(str, Enum):
    MODULE = "module"

    def __str__(self) -> str:
        return str(self.value)
