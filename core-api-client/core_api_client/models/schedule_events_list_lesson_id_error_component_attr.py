from enum import Enum


class ScheduleEventsListLessonIdErrorComponentAttr(str, Enum):
    LESSON_ID = "lesson__id"

    def __str__(self) -> str:
        return str(self.value)
