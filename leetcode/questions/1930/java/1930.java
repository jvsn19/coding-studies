import java.util.HashMap;

class Solution {
    public int countPalindromicSubsequence(String s) {
        HashMap<Character, Integer> first = new HashMap<>();
        HashMap<Character, Integer> last = new HashMap<>();
        int ans = 0;

        for (int idx = 0; idx < s.length(); ++idx) {
            char c = s.charAt(idx);
            
            if (!first.containsKey(c)) {
                first.put(c, idx);
            }
            
            last.put(c, idx);
        }
        
        for (char c: first.keySet()) {
            int start = first.get(c);
            int end = last.get(c);
            int mask = 0;

            for (int idx = start + 1; idx < end; ++idx) {
                int charInt = s.charAt(idx) - 'a';

                if ((mask & (1 << charInt)) == 0) {
                    ans += 1;
                }

                mask |= (1 << charInt);
            }
        }

        return ans;
    }
}