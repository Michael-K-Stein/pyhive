from enum import Enum


class ManagementUsersListClassesIdInErrorComponentAttr(str, Enum):
    CLASSES_ID_IN = "classes__id__in"

    def __str__(self) -> str:
        return str(self.value)
