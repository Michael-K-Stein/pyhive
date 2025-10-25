from enum import Enum


class ManagementUsersUpdateClassesErrorComponentAttr(str, Enum):
    CLASSES = "classes"

    def __str__(self) -> str:
        return str(self.value)
