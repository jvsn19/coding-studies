class Solution:
    def punishmentNumber(self, n: int) -> int:
        def check_num(num_str, target, cur_sum = 0, idx = 0):
            if idx == len(num_str):
                return cur_sum == target

            for i in range(idx, len(num_str)):
                cur_num = num_str[idx: i + 1]

                if check_num(num_str, target, cur_sum + int(cur_num), i + 1):
                    return True

            return False

        ans = 0

        for num in range(n + 1):
            square = num ** 2
            if check_num(str(square), num):
                ans += square

        return ans