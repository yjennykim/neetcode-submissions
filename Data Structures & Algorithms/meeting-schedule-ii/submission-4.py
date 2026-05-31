import heapq

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        minHeap = []
        intervals.sort(key=lambda x: x.start)

        count = 0
        minRooms = 0
        endPoints = {}
        for interval in intervals:
            heapq.heappush(minHeap, interval.start)
            heapq.heappush(minHeap, interval.end)
            if interval.end not in endPoints:
                endPoints[interval.end] = 0
            endPoints[interval.end] += 1
        
        while len(minHeap) != 0:
            point = heapq.heappop(minHeap)
            if point in endPoints:
                count -= 1
                endPoints[point] -= 1
                if endPoints[point] == 0:
                    del endPoints[point]
            else:
                count += 1
            minRooms = max(count, minRooms)
        
        return minRooms