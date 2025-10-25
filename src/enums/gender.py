from enum import Enum


class GenderEnum(str, Enum):
    FEMALE = "Female"
    MALE = "Male"
    NONBINARY = "NonBinary"

    def __str__(self) -> str:
        return str(self.value)
