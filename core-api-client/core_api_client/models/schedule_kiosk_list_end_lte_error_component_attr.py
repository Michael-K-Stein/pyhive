from enum import Enum


class ScheduleKioskListEndLteErrorComponentAttr(str, Enum):
    END_LTE = "end__lte"

    def __str__(self) -> str:
        return str(self.value)
