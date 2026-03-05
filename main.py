from grafo import grafo, heuristica
from a_star import a_star
from kmeans_simples import kmeans
import numpy as np

if __name__ == '__main__':
    print("=== ROTA COM A* ===")
    caminho, custo = a_star(grafo, heuristica, 'A', 'D')
    print("Caminho:", caminho)
    print("Custo total:", custo)

    print("\n=== CLUSTERING SIMPLES ===")
    pontos = np.array([
        [1, 1],
        [1.2, 1.1],
        [4, 4],
    ])
    grupos, centroides = kmeans(pontos, k=2)
    print("Grupos:", grupos)
    print("Centroides:\n", centroides)