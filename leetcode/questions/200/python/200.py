from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        steps = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def mark_island(row, col):
            stack = [(row, col)]

            while stack:
                r, c = stack.pop()

                if not (0 <= r < rows and 0 <= c < cols and grid[r][c] == "1"):
                    continue

                grid[r][c] = "-1"

                for r_inc, c_inc in steps:
                    new_r, new_c = r + r_inc, c + c_inc

                    if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == "1":
                        stack.append((new_r, new_c))

        cnt_islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    mark_island(r, c)
                    cnt_islands += 1

        return cnt_islands