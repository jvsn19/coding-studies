from collections import defaultdict

class TimeMap:

    def __init__(self):
        self._store = defaultdict(list)        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self._store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self._store[key]
        l, r = 0, len(values)

        while l < r:
            m = l + ((r - l) >> 1)

            if values[m][0] <= timestamp:
                l = m + 1
            else:
                r = m

        if r <= 0:
            return ""

        return values[r - 1][1] if values[r - 1][0] <= timestamp else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)