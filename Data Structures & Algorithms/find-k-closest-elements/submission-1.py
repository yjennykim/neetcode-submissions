import heapq

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        k_closest = []
        for i,num in enumerate(arr):
            dist = abs(num - x)
            heapq.heappush(k_closest, (-dist, -i))
            if len(k_closest) > k:
                heapq.heappop(k_closest)
        
        res = []
        for _ in range(len(k_closest)):
            _, i = heapq.heappop(k_closest)
            res.append(arr[-i])
        return sorted(res)
