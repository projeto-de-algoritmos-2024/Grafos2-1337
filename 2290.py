from typing import List
import heapq

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        # dimensoes da grid
        m, n = len(grid), len(grid[0])
        
        # se a grid for 1x1, nao ha obstaculos a remover
        if m == 1 and n == 1:
            return 0

        # direcoes possiveis: baixo, direita, cima, esquerda
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        # heap: (obstaculos removidos, linha, coluna)
        heap = [(0, 0, 0)]
        heapq.heapify(heap)
        
        # conjunto para manter os nos visitados
        visited = set()
        visited.add((0, 0))

        while heap:
            obstacles, row, col = heapq.heappop(heap)
            
            # se chegou ao destino, retorna o numero de obstaculos removidos
            if row == m - 1 and col == n - 1:
                return obstacles
            
            # explora as quatro direcoes
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                
                # verifica se a nova posicao esta dentro dos limites da grid
                if 0 <= new_row < m and 0 <= new_col < n:
                    if (new_row, new_col) not in visited:
                        visited.add((new_row, new_col))
                        
                        # se houver um obstaculo, incrementa o contador
                        if grid[new_row][new_col] == 1:
                            heapq.heappush(heap, (obstacles + 1, new_row, new_col))
                        else:
                            heapq.heappush(heap, (obstacles, new_row, new_col))
        
        # se nao encontrar um caminho, retorna -1
        return -1
