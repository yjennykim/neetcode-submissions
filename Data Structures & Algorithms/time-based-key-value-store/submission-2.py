
class TimeMap:

    def __init__(self):
        self.storage = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.storage:
            self.storage[key] = []
        
        self.storage[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.storage: return ""
        results = self.storage[key]

        l,r = 0, len(results)-1
        closestTS = -1
        retVal = ""
        while l <= r:
            m = (l+r) // 2
            ts = results[m][0]
            if ts <= timestamp:
                closestTS = ts
                retVal = results[m][1]
                l = m + 1
            else:
                r = m - 1
        
        return retVal
        
