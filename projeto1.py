import heapq
from state import State
from actions import Action, ActionType
from agent import Agent

def heuristica(pos, goal):
    """Distância de Manhattan para A*"""
    return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])

def a_star(start, goal, state):
    """Implementação do algoritmo A* para encontrar o melhor caminho até o gol"""
    fila = []
    heapq.heappush(fila, (0, start))  # Fila de prioridade

    custos = {start: 0}
    caminhos = {start: None}

    while fila:
        _, atual = heapq.heappop(fila)

        if atual == goal:  # Se chegou ao gol, reconstruir caminho
            caminho = []
            while atual is not None:
                caminho.append(atual)
                atual = caminhos[atual]
            return caminho[::-1]  # Retornar caminho na ordem correta

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            novo = (atual[0] + dx, atual[1] + dy)
            if novo not in state.opponents:  # Evita adversários
                novo_custo = custos[atual] + 1
                if novo not in custos or novo_custo < custos[novo]:
                    custos[novo] = novo_custo
                    prioridade = novo_custo + heuristica(novo, goal)
                    heapq.heappush(fila, (prioridade, novo))
                    caminhos[novo] = atual
    return None  # Nenhum caminho encontrado


# Criar um estado inicial
state = State(
    agent_pos=(5, 10),
    opponents=[(3, 8), (6, 12), (4, 10)],  # Adversários bloqueando caminhos
    teammates=[(2, 5), (7, 14)],  # Colegas disponíveis
    goal_pos=(19, 7)  # Posição do gol
)

# Criar o agente na posição inicial
agente = Agent(state.agent_pos)

# Obter ações válidas
acoes_disponiveis = agente.get_valid_actions(state)
print("Ações possíveis:", acoes_disponiveis)

# Calcular o melhor caminho até o gol com A*
caminho = a_star(state.agent_pos, state.goal_pos, state)
print("Melhor caminho para o gol:", caminho)
