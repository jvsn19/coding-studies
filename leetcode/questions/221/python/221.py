from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        aux = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]
        ans = 0

        for row in range(1, rows + 1):
            for col in range(1, cols + 1):
                if matrix[row - 1][col - 1] == "1":
                    aux[row][col] = min(aux[row - 1][col], aux[row][col - 1], aux[row - 1][col - 1]) + 1

                ans = max(ans, aux[row][col])

        return ans * ans