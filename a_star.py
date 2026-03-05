import heapq

def a_star(grafo, h, inicio, fim):
    fila = [(0, inicio)]
    custos = {inicio: 0}
    pais = {inicio: None}

    while fila:
        _, atual = heapq.heappop(fila)

        if atual == fim:
            caminho = []
            while atual is not None:
                caminho.append(atual)
                atual = pais[atual]
            return list(reversed(caminho)), custos[fim]

        for vizinho, peso in grafo[atual].items():
            novo_custo = custos[atual] + peso

            if vizinho not in custos or novo_custo < custos[vizinho]:
                custos[vizinho] = novo_custo
                prioridade = novo_custo + h[vizinho]
                heapq.heappush(fila, (prioridade, vizinho))
                pais[vizinho] = atual

    return None, float("inf")
