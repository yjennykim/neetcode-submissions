class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort()

        end = intervals[0][1]

        for i in range(1, len(intervals)):
            interval  = intervals[i]

            # if overlap (next meeting starts before previous one ends)
            if interval[0] < end:
                end = min(interval[1], end)
                res += 1
            else:
                end = interval[1]

        return res
