from enum import Enum


class ManagementSeatingUpdateClassroomErrorComponentAttr(str, Enum):
    CLASSROOM = "classroom"

    def __str__(self) -> str:
        return str(self.value)
