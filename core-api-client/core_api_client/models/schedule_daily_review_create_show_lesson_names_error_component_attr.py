from enum import Enum


class ScheduleDailyReviewCreateShowLessonNamesErrorComponentAttr(str, Enum):
    SHOW_LESSON_NAMES = "show_lesson_names"

    def __str__(self) -> str:
        return str(self.value)
