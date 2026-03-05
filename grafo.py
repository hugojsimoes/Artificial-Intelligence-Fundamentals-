grafo = {
    'A': {'B': 2, 'C': 4},
    'B': {'A': 2, 'D': 7},
    'C': {'A': 4, 'D': 1},
    'D': {'B': 7, 'C': 1}
}

# Heurística simples (estimativa de custo até o destino D)
heuristica = {
    'A': 4,
    'B': 2,
    'C': 1,
    'D': 0
}
