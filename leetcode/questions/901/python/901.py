class StockSpanner:

    def __init__(self):
        self._stack = []

    def next(self, price: int) -> int:
        cnt_days = 0

        while len(self._stack) and self._stack[~0][0] <= price:
            cnt_days += self._stack.pop()[1]

        self._stack.append((price, cnt_days + 1))
        return self._stack[~0][1]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)