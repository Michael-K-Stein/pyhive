from enum import Enum


class ScheduleLessonsListModuleIdErrorComponentAttr(str, Enum):
    MODULE_ID = "module__id"

    def __str__(self) -> str:
        return str(self.value)
