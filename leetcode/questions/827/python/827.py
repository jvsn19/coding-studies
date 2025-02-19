from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        steps = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def get_island_size(identifier, row, col):
            stack = [(row, col)]
            size = 0

            while stack:
                r, c = stack.pop()

                if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] != 1:
                    continue

                grid[r][c] = -identifier
                size += 1

                for i_r, i_c in steps:
                    n_r, n_c = r + i_r, c + i_c
                    stack.append((n_r, n_c))

            return size


        identifier = 1
        island_size = {0: 0}
        ans = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    island_size[-identifier] = get_island_size(identifier, row, col)
                    ans = max(ans, island_size[-identifier])
                    identifier += 1

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    cur_size = 1
                    visited = set()

                    for i_r, i_c in steps:
                        n_r, n_c = row + i_r, col + i_c

                        if 0 <= n_r < rows and 0 <= n_c < cols:
                            island_id = grid[n_r][n_c]

                            if island_id in visited:
                                continue

                            visited.add(island_id)
                            cur_size += island_size[grid[n_r][n_c]]

                    ans = max(ans, cur_size)

        return ans