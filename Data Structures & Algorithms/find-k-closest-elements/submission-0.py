import heapq

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        k_closest = []
        for i,num in enumerate(arr):
            dist = abs(num - x)
            heapq.heappush(k_closest, (dist, i))
        smallest = heapq.nsmallest(k, k_closest)
        return sorted([arr[item[1]] for item in smallest])
