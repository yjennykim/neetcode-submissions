from collections import defaultdict
import heapq

# O(NlogN)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1
        
        heap = [] # min-heap by default
        for num, count in counts.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)

        elements = []
        while heap:
            _, val = heapq.heappop(heap)
            elements.append(val)

        return elements