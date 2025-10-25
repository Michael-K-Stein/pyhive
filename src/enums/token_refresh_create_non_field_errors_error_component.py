from enum import Enum


class TokenRefreshCreateNonFieldErrorsErrorComponentCode(str, Enum):
    INVALID = "invalid"
    NO_ACTIVE_ACCOUNT = "no_active_account"
    NULL = "null"

    def __str__(self) -> str:
        return str(self.value)
