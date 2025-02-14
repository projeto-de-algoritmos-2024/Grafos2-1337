from heapq import heappop, heappush
from math import inf
from typing import List

class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        # cria o grafo como uma lista de adjacências
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))  # adiciona aresta de u para v com peso w
            graph[v].append((u, w))  # adiciona aresta de v para u com peso w (grafo não direcionado)

        # função para calcular as distâncias mínimas a partir de um nó de origem
        def dijkstra(source):
            dist = [inf] * n  # inicializa todas as distâncias como infinito
            dist[source] = 0  # a distância do nó de origem para ele mesmo é zero
            heap = [(0, source)]  # heap com (distância, nó)
            while heap:
                current_dist, u = heappop(heap)  # remove o nó com a menor distância
                if current_dist > dist[u]:  # ignora se a distância não for a mais atual
                    continue
                for v, weight in graph[u]:  # explora os vizinhos do nó atual
                    new_dist = current_dist + weight
                    if new_dist < dist[v]:  # se encontrar um caminho mais curto
                        dist[v] = new_dist  # atualiza a distância
                        heappush(heap, (new_dist, v))  # adiciona o vizinho na heap
            return dist  # retorna as distâncias mínimas

        # calcula as distâncias mínimas a partir do nó 0 e do nó n-1
        dist_from_start = dijkstra(0)
        dist_from_end = dijkstra(n - 1)

        # verifica se cada aresta faz parte de algum caminho mínimo
        result = []
        for u, v, w in edges:
            # verifica se o destino é alcançável e se a aresta está em um caminho mínimo
            is_critical = (
                dist_from_start[n - 1] < inf and  # destino é alcançável
                (
                    dist_from_start[u] + w + dist_from_end[v] == dist_from_start[n - 1] or  # caminho 0 -> u -> v -> n-1
                    dist_from_start[v] + w + dist_from_end[u] == dist_from_start[n - 1]  # caminho 0 -> v -> u -> n-1
                )
            )
            result.append(is_critical)  # adiciona o resultado para a aresta atual

        return result
