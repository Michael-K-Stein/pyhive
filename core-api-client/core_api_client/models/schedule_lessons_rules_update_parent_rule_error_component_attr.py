from enum import Enum


class ScheduleLessonsRulesUpdateParentRuleErrorComponentAttr(str, Enum):
    PARENT_RULE = "parent_rule"

    def __str__(self) -> str:
        return str(self.value)
