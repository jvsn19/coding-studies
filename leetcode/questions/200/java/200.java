import java.util.ArrayDeque;

class Solution {
    private void markIsland(char[][] grid, int row, int col) {
        int rows = grid.length, cols = grid[0].length;
        int[][] steps = {{0, 1}, {0, -1}, {-1, 0}, {1, 0}};
        ArrayDeque<int[]> stack = new ArrayDeque<>();
        stack.add(new int[]{row, col});

        while(!stack.isEmpty()) {
            int[] pair = stack.pollLast();
            int r = pair[0], c = pair[1];

            if (r < 0 || r >= rows || c < 0 || c >= cols || grid[r][c] != '1') {
                continue;
            }

            grid[r][c] = 'x';

            for (int[] step: steps) {
                int newRow = r + step[0], newCol = c + step[1];

                if (newRow >= 0 && newRow < rows && newCol >= 0 && newCol < cols && grid[newRow][newCol] == '1') {
                    stack.addFirst(new int[]{newRow, newCol});
                }
            }
        }
    }

    public int numIslands(char[][] grid) {
        int cntIslands = 0;

        for (int row = 0; row < grid.length; ++row) {
            for (int col = 0; col < grid[0].length; ++col) {
                if ( grid[row][col] == '1') {
                    cntIslands += 1;
                    markIsland(grid, row, col);
                }
            }
        }

        return cntIslands;
    }
}