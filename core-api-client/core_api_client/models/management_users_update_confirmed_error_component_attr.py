from enum import Enum


class ManagementUsersUpdateConfirmedErrorComponentAttr(str, Enum):
    CONFIRMED = "confirmed"

    def __str__(self) -> str:
        return str(self.value)
