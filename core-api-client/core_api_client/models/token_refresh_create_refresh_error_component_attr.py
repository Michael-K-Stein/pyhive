from enum import Enum


class TokenRefreshCreateRefreshErrorComponentAttr(str, Enum):
    REFRESH = "refresh"

    def __str__(self) -> str:
        return str(self.value)
