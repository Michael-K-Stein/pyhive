from enum import Enum


class ManagementClassesLessonCreateLessonErrorComponentAttr(str, Enum):
    LESSON = "lesson"

    def __str__(self) -> str:
        return str(self.value)
