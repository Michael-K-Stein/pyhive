from enum import Enum


class AssignmentsResponsesCreateContentsNonFieldErrorsErrorComponentAttr(str, Enum):
    CONTENTS_NON_FIELD_ERRORS = "contents.non_field_errors"

    def __str__(self) -> str:
        return str(self.value)
