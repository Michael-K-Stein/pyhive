from enum import Enum


class ScheduleKioskListLessonIdErrorComponentAttr(str, Enum):
    LESSON_ID = "lesson__id"

    def __str__(self) -> str:
        return str(self.value)
