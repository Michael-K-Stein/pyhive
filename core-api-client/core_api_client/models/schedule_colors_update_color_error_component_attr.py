from enum import Enum


class ScheduleColorsUpdateColorErrorComponentAttr(str, Enum):
    COLOR = "color"

    def __str__(self) -> str:
        return str(self.value)
