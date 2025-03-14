from bresenham import bresenham  # Biblioteca externa
from actions import Action, ActionType

def linha_livre(p1, p2, state):
    """Verifica se há adversários no caminho entre p1 e p2"""
    for x, y in bresenham(p1[0], p1[1], p2[0], p2[1]):
        if (x, y) in state.opponents:
            return False  # Caminho bloqueado por um adversário
    return True

class Agent:
    def __init__(self, pos):
        self.pos = pos  # Posição inicial do agente

    def get_valid_actions(self, state):
        """Retorna todas as ações válidas no estado atual"""
        actions = []

        # Movimento: Cima, Baixo, Esquerda, Direita
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_pos = (self.pos[0] + dx, self.pos[1] + dy)
            if self.is_valid_position(new_pos, state):
                actions.append(Action(ActionType.MOVE, (dx, dy)))

        # Chute ao gol se o caminho estiver livre
        if linha_livre(self.pos, state.goal_pos, state):
            actions.append(Action(ActionType.SHOOT))

        # Passes para colegas de time
        for teammate in state.teammates:
            if linha_livre(self.pos, teammate, state):
                actions.append(Action(ActionType.PASS, teammate))

        return actions

    def is_valid_position(self, pos, state):
        """Verifica se a posição está dentro do campo e não tem adversários"""
        return pos not in state.opponents  # Pode adicionar limites do campo aqui
