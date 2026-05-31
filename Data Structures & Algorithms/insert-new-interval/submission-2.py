class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for interval in intervals:
            prevStart, prevEnd = interval
            currStart, currEnd = newInterval

            # If the current interval ends before the new interval starts, add it to the result
            if prevEnd < currStart:
                res.append(interval)
            # If the current interval starts after the new interval ends, add the new interval and the current interval
            elif prevStart > currEnd:
                res.append(newInterval)
                newInterval = interval  # Update the new interval to the current interval
            else:
                # There is an overlap, so we merge the intervals
                newInterval = [min(prevStart, currStart), max(prevEnd, currEnd)]

        # After the loop, don't forget to append the last merged interval
        res.append(newInterval)

        return res
