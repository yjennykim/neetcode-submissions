class TimeMap:

    def __init__(self):
        self.storage = {} # maps key -> []

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.storage:
            self.storage[key] = []
        self.storage[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
       # Last timestamp <= target 
        if key not in self.storage:
            return ""
        values = self.storage[key]
        if len(values) == 0:
            return ""
        if timestamp < values[0][0]:
            return ""

        l, r = 0, len(values)-1
        while l < r:    
            m = (l + r + 1) // 2
            # Keep candidates
            if values[m][0] <= timestamp:
                l = m
            else:
                r = m - 1 

        # L is the largest timestamp <= timestamp
        return values[l][1]
