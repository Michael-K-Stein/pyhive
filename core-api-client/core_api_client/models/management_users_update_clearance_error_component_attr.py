from enum import Enum


class ManagementUsersUpdateClearanceErrorComponentAttr(str, Enum):
    CLEARANCE = "clearance"

    def __str__(self) -> str:
        return str(self.value)
