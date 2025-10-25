from enum import Enum


class ManagementUsersCreateClassesErrorComponentAttr(str, Enum):
    CLASSES = "classes"

    def __str__(self) -> str:
        return str(self.value)
