import java.util.*;

class DisjointSet {
    private int[] groups;
    private int[] ranks;
    private int numGroups;

    public DisjointSet(int numGroups) {
        this.numGroups = numGroups;
        this.groups = new int[numGroups];
        this.ranks = new int[numGroups];

        for (int i = 0; i < numGroups; ++i) {
            this.groups[i] = i;
            this.ranks[i] = 0;
        }
    }

    public int find(int val) {
        if (this.groups[val] == val) {
            return val;
        }

        this.groups[val] = find(this.groups[val]);
        return this.groups[val];
    }

    public boolean same(int valA, int valB) {
        return find(valA) == find(valB);
    }

    public int unite(int valA, int valB) {
        if (same(valA, valB)) {
            return this.numGroups;
        }

        int groupA = find(valA);
        int groupB = find(valB);
        this.numGroups -= 1;

        if (this.ranks[groupA] > this.ranks[groupB]) {
            this.groups[groupB] = groupA;
        } else if (this.ranks[groupA] < this.ranks[groupB]) {
            this.groups[groupA] = groupB;
        } else {
            this.groups[groupB] = groupA;
            this.ranks[groupA] += 1;
        }

        return this.numGroups;
    }
}

class Solution {
    public int earliestAcq(int[][] logs, int n) {
        DisjointSet disjointSet = new DisjointSet(n);
        PriorityQueue<int[]> priorityQueue = new PriorityQueue<>((a, b) -> a[0] - b[0]);

        for (int[] log: logs) {
            priorityQueue.offer(log);
        }

        while(!priorityQueue.isEmpty()) {
            int[] log = priorityQueue.poll();
            int ts = log[0], a = log[1], b = log[2];
            int remain = disjointSet.unite(a, b);

            if (remain == 1) {
                return ts;
            }
        }

        return -1;
    }
}