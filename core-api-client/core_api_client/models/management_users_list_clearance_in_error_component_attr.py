from enum import Enum


class ManagementUsersListClearanceInErrorComponentAttr(str, Enum):
    CLEARANCE_IN = "clearance__in"

    def __str__(self) -> str:
        return str(self.value)
