from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.store.get(key, [])
        l,r = 0, len(arr)-1

        # first value with prev <= timestamp
        while l < r: 
            m = (l + r + 1) // 2

            prev, val = arr[m]
            # potential candidate
            if prev <= timestamp:
                l = m
            else:
                # prev too big, look left
                r = m - 1
        
        if not arr or timestamp < arr[l][0]: 
            return ""
        
        return arr[l][1]

# 10