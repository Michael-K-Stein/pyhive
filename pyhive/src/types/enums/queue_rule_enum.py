from enum import Enum


class QueueRuleEnum(str, Enum):
    CHOOSE = "Choose"
    WAIT_FOR_AUTOCHECKS = "Wait For AutoChecks"
    WAIT_FOR_DONE = "Wait For Done"
    WAIT_FOR_SUBMITTED = "Wait For Submitted"

    def __str__(self) -> str:
        return str(self.value)
