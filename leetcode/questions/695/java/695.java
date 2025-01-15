import java.util.Stack;

class Solution {
    private int[][] steps = {{0, 1}, {0, -1}, {-1, 0}, {1, 0}};

    private int dfs(int row, int col, int[][] grid) {
        int area = 0;
        int rows = grid.length;
        int cols = grid[0].length;
        Stack<int[]> stack = new Stack<>();
        stack.push(new int[]{row, col});

        while(!stack.isEmpty()) {
            int[] pair = stack.pop();
            int r = pair[0];
            int c = pair[1];

            if (r < 0 || r >= rows || c < 0 || c >= cols || grid[r][c] != 1) {
                continue;
            }

            grid[r][c] = -1;
            area += 1;

            for (int[] step: steps) {
                int newRow = step[0] + r;
                int newCol = step[1] + c;

                if (0 <= newRow && newRow < rows && 0 <= newCol && newCol < cols && grid[newRow][newCol] == 1) {
                    stack.push(new int[]{newRow, newCol});
                }
            }
        }

        return area;
    }

    public int maxAreaOfIsland(int[][] grid) {
        int ans = 0;

        for (int row = 0; row < grid.length; ++row) {
            for (int col = 0; col < grid[0].length; ++col) {
                if (grid[row][col] == 1) {
                    ans = Math.max(ans, dfs(row, col, grid));
                }
            }
        }

        return ans;
    }
}