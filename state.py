class State:
    def __init__(self, agent_pos, opponents, teammates, goal_pos):
        self.agent_pos = agent_pos  # Posição do agente (x, y)
        self.opponents = opponents  # Lista de posições dos adversários [(x1, y1), (x2, y2), ...]
        self.teammates = teammates  # Lista de posições dos aliados [(x1, y1), (x2, y2), ...]
        self.goal_pos = goal_pos  # Posição do gol (x, y)

    def __repr__(self):
        return f"Agente: {self.agent_pos}, Oponentes: {self.opponents}, Companheiros: {self.teammates}, Gol: {self.goal_pos}"
