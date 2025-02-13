class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse_word(arr, st, end):
            while st < end:
                arr[st], arr[end] = arr[end], arr[st]
                st += 1
                end -= 1

        list_s = list(reversed(s))
        list_s.append(' ')
        st = 0

        for idx, c in enumerate(list_s):
            if c == ' ':
                reverse_word(list_s, st, idx - 1)
                st = idx + 1

        st = 0
        for idx, c in enumerate(list_s):
            if c != ' ' or (st > 0 and list_s[st - 1] != ' '):
                list_s[st], list_s[idx] = list_s[idx], list_s[st]
                st += 1

        while list_s[~0] == ' ':
            list_s.pop()

        return ''.join(list_s)
