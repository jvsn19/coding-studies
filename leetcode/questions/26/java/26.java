class Solution {
    public int removeDuplicates(int[] nums) {
        int last = 1;

        for (int idx = 1; idx < nums.length; ++idx) {

            if (nums[idx] != nums[idx - 1]) {
                nums[last] = nums[idx];
                last += 1;
            }
        }

        return last;
    }
}