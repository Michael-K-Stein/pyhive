from enum import Enum


class HelpBulkRespondCreateContentsErrorComponentAttr(str, Enum):
    CONTENTS = "contents"

    def __str__(self) -> str:
        return str(self.value)
