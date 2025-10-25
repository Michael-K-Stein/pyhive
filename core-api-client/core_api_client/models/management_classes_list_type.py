from enum import Enum


class ManagementClassesListType(str, Enum):
    ROOM = "Room"
    STUDENT_GROUP = "Student Group"

    def __str__(self) -> str:
        return str(self.value)
