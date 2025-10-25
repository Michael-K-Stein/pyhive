from enum import Enum


class CourseExercisesFieldsUpdateStaffResponsesErrorComponentAttr(str, Enum):
    STAFF_RESPONSES = "staff_responses"

    def __str__(self) -> str:
        return str(self.value)
