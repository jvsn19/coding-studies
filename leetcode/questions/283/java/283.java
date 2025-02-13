class Solution {
    public void moveZeroes(int[] nums) {
        int nonZero = 0;

        for (int i = 0; i < nums.length; ++i) {
            int aux = nums[i];
            nums[i] = nums[nonZero];
            nums[nonZero] = aux;

            if (nums[nonZero] != 0) {
                nonZero += 1;
            }
        }
    }
}