from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        steps = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(row, col):
            stack = [(row, col)]
            area = 0

            while stack:
                r, c = stack.pop()

                if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] != 1:
                    continue

                grid[r][c] = -1
                area += 1

                for r_inc, c_inc in steps:
                    new_r, new_c = r + r_inc, c + c_inc

                    if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 1:
                        stack.append((new_r, new_c))

            return area

        ans = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    ans = max(ans, dfs(row, col))

        return ans