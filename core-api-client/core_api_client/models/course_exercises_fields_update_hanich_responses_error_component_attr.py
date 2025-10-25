from enum import Enum


class CourseExercisesFieldsUpdateHanichResponsesErrorComponentAttr(str, Enum):
    HANICH_RESPONSES = "hanich_responses"

    def __str__(self) -> str:
        return str(self.value)
