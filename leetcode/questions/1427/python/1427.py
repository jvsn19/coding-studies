class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        str_ptr = 0
        len_s = len(s)

        for direction, amount in shift:
            if direction == 0:
                str_ptr += amount
            elif direction == 1:
                str_ptr -= amount
                
            str_ptr %= len_s

        return s[str_ptr:] + s[:str_ptr]