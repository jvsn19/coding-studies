class Solution {
    private void swap(int[] nums, int idxA, int idxB) {
        int aux = nums[idxA];
        nums[idxA] = nums[idxB];
        nums[idxB] = aux;
    }

    public int removeElement(int[] nums, int val) {
        int last = nums.length - 1;

        for (int idx = nums.length - 1; idx >= 0; --idx) {
            if (nums[idx] == val) {
                swap(nums, idx, last);
                last -= 1;
            }
        }

        return last + 1;
    }
}