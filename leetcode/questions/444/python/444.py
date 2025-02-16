from typing import List
from collections import deque

class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        graph = [[] for _ in range(len(nums) + 1)]
        dependencies = [0 for _ in range(len(nums) + 1)]

        for sequence in sequences:
            for i in range(1, len(sequence)):
                graph[sequence[i - 1]].append(sequence[i])
                dependencies[sequence[i]] += 1

        queue = deque([num for num, cnt_dependencies in enumerate(dependencies) if num > 0 and cnt_dependencies == 0])
        supersequence = [num for num in queue]

        while queue:
            if len(queue) > 1:
                # Multiple ways to build a supersequence
                return False

            num = queue.popleft()

            for nxt in graph[num]:
                dependencies[nxt] -= 1

                if dependencies[nxt] == 0:
                    supersequence.append(nxt)
                    queue.append(nxt)

        return nums == supersequence