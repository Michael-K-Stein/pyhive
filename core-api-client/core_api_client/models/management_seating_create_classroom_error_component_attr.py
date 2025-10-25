from enum import Enum


class ManagementSeatingCreateClassroomErrorComponentAttr(str, Enum):
    CLASSROOM = "classroom"

    def __str__(self) -> str:
        return str(self.value)
