from typing import List

class Solution:
    
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        def check_availability(slot1, slot2, dur):
            early, late = sorted([slot1, slot2], key = lambda slot: slot[0])
            return (early[1] - late[0] >= dur and late[0] + dur <= late[1]), [late[0], late[0] + dur]


        slots1.sort()
        slots2.sort()
        idx1 = idx2 = 0
        len1, len2 = len(slots1), len(slots2)

        while idx1 < len1 and idx2 < len2:
            if (available := check_availability(slots1[idx1], slots2[idx2], duration))[0]:
                return available[1]
            
            if slots1[idx1][1] <= slots2[idx2][1]:
                idx1 += 1
            else:
                idx2 += 1

        return []