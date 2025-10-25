from enum import Enum


class ManagementUsersPartialUpdateConfirmedErrorComponentAttr(str, Enum):
    CONFIRMED = "confirmed"

    def __str__(self) -> str:
        return str(self.value)
