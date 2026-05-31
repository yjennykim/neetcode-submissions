class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            interval = intervals[i]

            if newInterval[0] > interval[1]:
                res.append(interval)
            elif newInterval[1] < interval[0]:
                res.append(newInterval)
                return res + intervals[i:]
            else:
                # merge
                newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]
        
        res.append(newInterval)
        return res