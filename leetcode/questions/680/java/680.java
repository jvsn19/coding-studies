class Solution {
    private boolean check(int leftIdx, int rightIdx, boolean previouslyDeleted, String s) {
        while (leftIdx < rightIdx) {
            if (s.charAt(leftIdx) != s.charAt(rightIdx)) {
                if (previouslyDeleted) {
                    return false;
                }
                // Try to delete one character
                return check(leftIdx + 1, rightIdx, true, s) || check(leftIdx, rightIdx - 1, true, s);
            }
            ++leftIdx;
            --rightIdx;
        }
        return true;
    }

    public boolean validPalindrome(String s) {
        return check(0, s.length() - 1, false, s);
    }
}