class Solution {
    private void swap(int[] arr, int idxA, int idxB) {
        int tmp = arr[idxA];
        arr[idxA] = arr[idxB];
        arr[idxB] = tmp;
    }

    public void sortColors(int[] nums) {
        int numsLen = nums.length;
        int colorA = 0, colorB = numsLen - 1, idx = 0;

        while (idx <= colorB) {
            if (nums[idx] == 0) {
                swap(nums, idx++, colorA++);
            } else if (nums[idx] == 2) {
                swap(nums, idx, colorB--);
            } else {
                ++idx;
            }
        }
    }
}