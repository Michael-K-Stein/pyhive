from enum import Enum


class ManagementUsersPartialUpdateClassesErrorComponentAttr(str, Enum):
    CLASSES = "classes"

    def __str__(self) -> str:
        return str(self.value)
