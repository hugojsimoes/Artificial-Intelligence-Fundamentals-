import numpy as np

def kmeans(pontos, k=2, iteracoes=10):
    centroides = pontos[np.random.choice(len(pontos), k, replace=False)]

    for _ in range(iteracoes):
        dist = ((pontos[:, None] - centroides)**2).sum(axis=2)
        grupos = dist.argmin(axis=1)
        novos_centroides = np.array([
            pontos[grupos == i].mean(axis=0) if (grupos == i).any() else centroides[i]
            for i in range(k)
        ])

        if np.allclose(centroides, novos_centroides):
            break
        centroides = novos_centroides

    return grupos, centroides
