import java.util.*;

class Solution {
    private int shortestPathDjikstra(int[] start, int[] end, int[][] maze) {
        int[][] steps = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        int rows = maze.length;
        int cols = maze[0].length;
        int [][] distances = new int[rows][cols];
        PriorityQueue<int []> heap = new PriorityQueue<>((a, b) -> a[2] - b[2]);
        heap.add(new int[]{start[0], start[1], 0});

        for (int[] row: distances) {
            Arrays.fill(row, Integer.MAX_VALUE);
        }

        distances[start[0]][start[1]] = 0;

        while (!heap.isEmpty()) {
            int[] node = heap.poll();
            int r = node[0], c = node[1], dist = node[2];

            if (dist > distances[r][c]) {
                continue;
            }

            if (end[0] == r && end[1] == c) {
                return dist;
            }

            for (int[] step: steps) {
                int newRow = r, newCol = c, numSteps = 0;

                do {
                    newRow += step[0];
                    newCol += step[1];
                    ++numSteps;
                } while (0 <= newRow && 0 <= newCol && newRow < rows && newCol < cols && maze[newRow][newCol] != 1);

                newRow -= step[0];
                newCol -= step[1];
                --numSteps; // Counted an extra step

                if (distances[newRow][newCol] > (dist + numSteps)) {
                    distances[newRow][newCol] = dist + numSteps;
                    heap.add(new int[] {newRow, newCol, distances[newRow][newCol]});
                }
            }
        }

        return -1;
    }

    public int shortestDistance(int[][] maze, int[] start, int[] destination) {
        return shortestPathDjikstra(start, destination, maze);
    }
}