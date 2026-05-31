class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        intervalA = intervals[0]
        res = []
        for i in range(1, len(intervals)):
            intervalB = intervals[i]

            # no overlap
            if intervalA[0] > intervalB[1]:
                res.append(intervalB)

            elif intervalA[1] < intervalB[0]:
                res.append(intervalA)
                intervalA = intervalB

            else:
                intervalA = [min(intervalA[0], intervalB[0]), max(intervalA[1], intervalB[1])]
        
        res.append(intervalA)
        return res