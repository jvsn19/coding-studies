class Solution {
    public int maximalSquare(char[][] matrix) {
        int rows = matrix.length;
        int cols = matrix[0].length;
        int[][] aux = new int[rows + 1][cols + 1];
        int len = 0;

        for (int row = 1; row <= rows; ++row) {
            for (int col = 1; col <= cols; ++col) {
                if (matrix[row - 1][col - 1] == '1') {
                    aux[row][col] = Math.min(aux[row - 1][col], Math.min(aux[row][col - 1], aux[row - 1][col - 1])) + 1;
                }
                len = Math.max(len, aux[row][col]);
            }
        }

        return len * len;
    }
}