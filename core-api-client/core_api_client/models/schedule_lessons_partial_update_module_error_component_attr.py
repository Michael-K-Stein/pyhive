from enum import Enum


class ScheduleLessonsPartialUpdateModuleErrorComponentAttr(str, Enum):
    MODULE = "module"

    def __str__(self) -> str:
        return str(self.value)
