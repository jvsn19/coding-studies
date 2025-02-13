from typing import List

class DisjointSet:
    def __init__(self, num_groups):
        self._num_groups = num_groups
        self._groups = [group for group in range(num_groups)]
        self._ranks = [0 for _ in range(num_groups)]

    def find(self, a):
        if self._groups[a] == a:
            return a
        self._groups[a] = self.find(self._groups[a])

        return self._groups[a]

    def is_same(self, a, b):
        return self.find(a) == self.find(b)

    def unite(self, a, b):
        if self.is_same(a, b):
            return self._num_groups

        self._num_groups -= 1
        group_a = self.find(a)
        group_b = self.find(b)

        if self._ranks[group_a] > self._ranks[group_b]:
            self._groups[group_b] = group_a
        elif self._ranks[group_a] < self._ranks[group_b]:
            self._groups[group_a] = group_b
        else:
            self._groups[group_b] = group_a
            self._ranks[group_a] += 1

        return self._num_groups

    def num_groups(self):
        return self._num_groups


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        disjoint_set = DisjointSet(n)
        logs.sort()

        for ts, a, b in logs:
            disjoint_set.unite(a, b)
            if disjoint_set.num_groups() == 1:
                return ts

        return -1