from enum import Enum

class ActionType(Enum):
    MOVE = "move"
    SHOOT = "shoot"
    PASS = "pass"

class Action:
    def __init__(self, action_type, value=None):
        self.action_type = action_type  # Tipo da ação
        self.value = value  # Dependendo da ação: (dx, dy), None ou (x, y)

    def __repr__(self):
        return f"Action({self.action_type}, {self.value})"




