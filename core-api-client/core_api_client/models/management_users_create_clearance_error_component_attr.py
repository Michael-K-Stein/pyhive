from enum import Enum


class ManagementUsersCreateClearanceErrorComponentAttr(str, Enum):
    CLEARANCE = "clearance"

    def __str__(self) -> str:
        return str(self.value)
