from collections import defaultdict
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        INF = float('inf')
        vertical_values = defaultdict(list)
        self._min_col = INF
        self._max_col = -INF

        def dfs(root = root, row = 0, col = 0):
            if root is None:
                return

            self._min_col = min(self._min_col, col)
            self._max_col = max(self._max_col, col)

            vertical_values[col].append((row, root.val))
            dfs(root.left, row + 1, col - 1)
            dfs(root.right, row + 1, col + 1)
            
        dfs()
        ans = []

        for col in range(self._min_col, self._max_col + 1):
            ans.append([val for _, val in sorted(vertical_values[col])])
            
        return ans