import heapq

from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        max_num_rooms = 0
        heap_rooms = []

        for st, end in intervals:
            while len(heap_rooms) > 0 and heap_rooms[0] <= st:
                heapq.heappop(heap_rooms)
            
            heapq.heappush(heap_rooms, end)
            max_num_rooms = max(max_num_rooms, len(heap_rooms))

        return max_num_rooms