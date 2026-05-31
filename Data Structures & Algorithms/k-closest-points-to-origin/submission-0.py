import heapq 

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def getDistance(x1, x2, y1, y2):
            return math.sqrt((x1-x2)**2 + (y1-y2)**2)
        
        distances = []
        x1, y1 = [0,0]
        for i in range(len(points)):
            x2, y2 = points[i]
            distance = getDistance(x1,x2,y1,y2)
            heapq.heappush(distances, [-distance, [x2,y2]])

            # only store k closest distances.
            if len(distances) > k:
                heapq.heappop(distances)
        
        res = []
        for distance in distances:
            res.append(distance[1])
        return res # get the kth closest, the points stored there
