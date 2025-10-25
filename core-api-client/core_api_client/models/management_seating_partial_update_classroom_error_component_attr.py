from enum import Enum


class ManagementSeatingPartialUpdateClassroomErrorComponentAttr(str, Enum):
    CLASSROOM = "classroom"

    def __str__(self) -> str:
        return str(self.value)
