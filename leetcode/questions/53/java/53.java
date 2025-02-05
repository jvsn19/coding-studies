class Solution {
    public int maxSubArray(int[] nums) {
        int maxSum = Integer.MIN_VALUE, curSum = Integer.MIN_VALUE;
        
        for (int num: nums) {
            curSum = curSum < 0 ? num : num + curSum;
            maxSum = Math.max(curSum, maxSum);
        }

        return maxSum;
    }
}