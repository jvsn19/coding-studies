from typing import List
from collections import deque

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        inverted_graph = [[] for _ in range(len(graph))]
        dependency_cnt = [0 for _ in range(len(graph))]
        safe = [False for _ in range(len(graph))]
        queue = deque()

        for u, edges in enumerate(graph):
            for v in edges:
                inverted_graph[v].append(u)
                dependency_cnt[u] += 1

        for node, cnt in enumerate(dependency_cnt):
            if cnt == 0:
                safe[node] = True
                queue.append(node)

        while queue:
            node = queue.popleft()

            for nxt in inverted_graph[node]:
                dependency_cnt[nxt] -= 1

                if dependency_cnt[nxt] == 0:
                    safe[nxt] = True
                    queue.append(nxt)

        return [node for node, is_safe in enumerate(safe) if is_safe]