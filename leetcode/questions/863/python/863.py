from collections import defaultdict
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def build_graph():
            graph = defaultdict(list)
            stack = [(root, None)]

            while stack:
                node, parent = stack.pop()

                if not node:
                    continue

                if parent:
                    graph[node.val].append(parent.val)
                    graph[parent.val].append(node.val)

                stack.append((node.left, node))
                stack.append((node.right, node))

            return graph

        graph = build_graph()

        def dfs(root):
            stack = [(root, 0)]
            marked = set()
            ans = []

            while stack:
                node, dist = stack.pop()

                if node in marked:
                    continue

                marked.add(node)

                if dist == k:
                    ans.append(node)
                    continue

                for nxt in graph[node]:
                    stack.append((nxt, dist + 1))

            return ans

        return dfs(target.val)