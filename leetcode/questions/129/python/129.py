from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self._sum = 0

        def dfs(root, cur_sum):
            if not root:
                return

            next_sum = cur_sum * 10 + root.val

            if root.left is None and root.right is None:
                self._sum += next_sum
                return

            dfs(root.left, next_sum)
            dfs(root.right, next_sum)

        dfs(root, 0)

        return self._sum