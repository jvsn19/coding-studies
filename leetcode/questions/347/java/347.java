import java.util.*;

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> count = new HashMap<>();
        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> Integer.compare(a[1], b[1]));

        for (int num: nums) {
            count.put(num, count.getOrDefault(num, 0) + 1);
        }

        count.forEach((key, val) -> {
            heap.offer(new int[] {key, val});
            if(heap.size() > k) {
                heap.poll();
            }
        });

        int heapSize = heap.size();
        int[] ans = new int[heap.size()];

        for (int i = 0; i < heapSize; ++i) {
            int[] pair = heap.poll();
            ans[i] = pair[0];
        }

        return ans;
    }
}