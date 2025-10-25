from enum import Enum


class CourseExercisesFieldsCreateStaffResponsesErrorComponentAttr(str, Enum):
    STAFF_RESPONSES = "staff_responses"

    def __str__(self) -> str:
        return str(self.value)
