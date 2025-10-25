from enum import Enum


class ManagementUsersMePartialUpdateConfirmedErrorComponentAttr(str, Enum):
    CONFIRMED = "confirmed"

    def __str__(self) -> str:
        return str(self.value)
