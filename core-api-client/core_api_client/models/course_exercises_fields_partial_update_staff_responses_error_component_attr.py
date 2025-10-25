from enum import Enum


class CourseExercisesFieldsPartialUpdateStaffResponsesErrorComponentAttr(str, Enum):
    STAFF_RESPONSES = "staff_responses"

    def __str__(self) -> str:
        return str(self.value)
