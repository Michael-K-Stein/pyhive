from enum import Enum


class ManagementUsersPartialUpdateMenteesErrorComponentAttr(str, Enum):
    MENTEES = "mentees"

    def __str__(self) -> str:
        return str(self.value)
