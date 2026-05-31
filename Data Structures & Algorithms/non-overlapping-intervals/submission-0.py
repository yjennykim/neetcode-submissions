class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])

        res = 0
        prevEnd = intervals[0][1] # prev end

        for start, end in intervals[1:]:
            # if no overlap
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(end, prevEnd)
        
        return res