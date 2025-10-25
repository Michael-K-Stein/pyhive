from enum import Enum


class ClientErrorEnum(str, Enum):
    CLIENT_ERROR = "client_error"

    def __str__(self) -> str:
        return str(self.value)
