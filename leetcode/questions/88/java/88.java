class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int nums2Limit = nums2.length;
        int nums1Limit = nums1.length - nums2Limit;
        int idx1 = nums1Limit - 1;
        int idx2 = nums2Limit - 1; 

        for (int idxMerged = nums1.length - 1; idxMerged >= 0; --idxMerged) {
            if (idx2 >= 0 && (idx1 < 0 || nums1[idx1] <= nums2[idx2])) {
                nums1[idxMerged] = nums2[idx2];
                idx2 -= 1;
            }
            else if (idx2 < 0 || nums1[idx1] > nums2[idx2]) {
                nums1[idxMerged] = nums1[idx1];
                idx1 -= 1;
            }
        }
    }
}