from enum import Enum


class ManagementUsersPartialUpdateClearanceErrorComponentAttr(str, Enum):
    CLEARANCE = "clearance"

    def __str__(self) -> str:
        return str(self.value)
