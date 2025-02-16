from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        levels = []

        def get_values_per_level(root, level):
            if root is None:
                return

            while len(levels) <= level:
                levels.append([])

            levels[level].append(root.val)
            get_values_per_level(root.left, level + 1)
            get_values_per_level(root.right, level + 1)

        ans = []
        get_values_per_level(root, 0)

        for level in levels:
            ans.append(sum(level) / len(level))

        return ans