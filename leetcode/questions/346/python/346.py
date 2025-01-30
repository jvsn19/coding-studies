from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self._deque = deque()
        self._size = size
        self._total_sum = 0

    def next(self, val: int) -> float:
        if len(self._deque) == self._size:
            to_remove = self._deque.popleft()
            self._total_sum -= to_remove

        self._deque.append(val)
        self._total_sum += val

        return self._total_sum / len(self._deque)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)