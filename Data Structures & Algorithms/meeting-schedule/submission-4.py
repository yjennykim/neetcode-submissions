"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)

        # Iterate over intervals
        for i in range(len(intervals) - 1):
            # If interval i conflicts with interval i + 1 output false
            if intervals[i].end > intervals[i + 1].start:
                return False

        return True