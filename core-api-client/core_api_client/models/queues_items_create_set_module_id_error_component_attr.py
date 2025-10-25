from enum import Enum


class QueuesItemsCreateSetModuleIdErrorComponentAttr(str, Enum):
    SET_MODULE_ID = "set_module_id"

    def __str__(self) -> str:
        return str(self.value)
