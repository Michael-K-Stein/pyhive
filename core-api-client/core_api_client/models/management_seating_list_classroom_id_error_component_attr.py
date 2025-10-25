from enum import Enum


class ManagementSeatingListClassroomIdErrorComponentAttr(str, Enum):
    CLASSROOM_ID = "classroom__id"

    def __str__(self) -> str:
        return str(self.value)
