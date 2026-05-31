"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x:x.start)

        if len(intervals) <= 1: return True
        intervalA = intervals[0]
        for i in range(1, len(intervals)):
            intervalB = intervals[i]
            if intervalB.start < intervalA.end:
                return False
            
            intervalA = intervalB
        
        return True
