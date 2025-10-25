from enum import Enum


class ActionEnum(str, Enum):
    BUILT = "Built"
    ERROR = "Error"
    FINISHED = "Finished"
    HANDLING = "Handling"
    NO_CHECK = "No Check"
    SENDING = "Sending"
    SUCCESS = "Success"

    def __str__(self) -> str:
        return str(self.value)
