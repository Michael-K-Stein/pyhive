from enum import Enum


class AssignmentsResponsesPartialUpdateResponseTypeErrorComponentAttr(str, Enum):
    RESPONSE_TYPE = "response_type"

    def __str__(self) -> str:
        return str(self.value)
