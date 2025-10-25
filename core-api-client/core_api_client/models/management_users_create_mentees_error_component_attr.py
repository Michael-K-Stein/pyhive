from enum import Enum


class ManagementUsersCreateMenteesErrorComponentAttr(str, Enum):
    MENTEES = "mentees"

    def __str__(self) -> str:
        return str(self.value)
