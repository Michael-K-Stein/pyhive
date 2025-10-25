from enum import Enum


class ScheduleLessonsUpdateModuleErrorComponentAttr(str, Enum):
    MODULE = "module"

    def __str__(self) -> str:
        return str(self.value)
