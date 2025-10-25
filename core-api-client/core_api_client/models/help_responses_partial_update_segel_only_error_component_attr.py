from enum import Enum


class HelpResponsesPartialUpdateSegelOnlyErrorComponentAttr(str, Enum):
    SEGEL_ONLY = "segel_only"

    def __str__(self) -> str:
        return str(self.value)
