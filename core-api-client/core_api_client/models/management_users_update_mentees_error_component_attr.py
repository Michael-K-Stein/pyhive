from enum import Enum


class ManagementUsersUpdateMenteesErrorComponentAttr(str, Enum):
    MENTEES = "mentees"

    def __str__(self) -> str:
        return str(self.value)
