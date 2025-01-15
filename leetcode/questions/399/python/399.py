from typing import List

from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def calculate(graph, st, end):
            marked = set()
            queue = deque([(st, 1)])

            while queue:
                cur, val = queue.popleft()

                if cur == end:
                    return val

                if cur in marked:
                    continue

                marked.add(cur)

                for nxt, nxt_val in graph[cur]:
                    queue.append((nxt, nxt_val * val))

            return -1
        
        graph = defaultdict(list)

        for idx, (st, end) in enumerate(equations):
            graph[st].append((end, values[idx]))
            graph[end].append((st, 1/values[idx]))

        ans = []

        for st, end in queries:
            if st not in graph or end not in graph:
                ans.append(-1)
            else:
                ans.append(calculate(graph, st, end))

        return ans