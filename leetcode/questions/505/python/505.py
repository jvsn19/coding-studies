import heapq

from typing import List

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        INF = float('inf')
        steps = ((0, 1), (0, -1), (1, 0), (-1, 0))
        rows, cols = len(maze), len(maze[0])
        heap = [(0, start)]
        distances = [[INF for _ in range(cols)] for _ in range(rows)]
        distances[start[0]][start[1]] = 0

        while heap:
            dist, (r, c) = heapq.heappop(heap)
            
            if [r, c] == destination:
                break

            if dist > distances[r][c]:
                continue

            for r_inc, c_inc in steps:
                new_r, new_c = r + r_inc, c + c_inc
                walked = 0

                while 0 <= new_r < rows and 0 <= new_c < cols and maze[new_r][new_c] != 1:
                    new_r += r_inc
                    new_c += c_inc
                    walked += 1

                new_r -= r_inc
                new_c -= c_inc

                if distances[new_r][new_c] > dist + walked:
                    distances[new_r][new_c] = dist + walked
                    heapq.heappush(heap, (dist + walked, [new_r, new_c]))

        return distances[destination[0]][destination[1]] if distances[destination[0]][destination[1]] != INF else -1