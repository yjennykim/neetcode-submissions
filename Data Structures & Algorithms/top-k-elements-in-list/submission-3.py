from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1
        
        heap = [] # min-heap by default, multiply by -1 for max
        for num, count in counts.items():
            heapq.heappush(heap, (-count, num))

        elements = []
        for i in range(k):
            _, val = heapq.heappop(heap)
            elements.append(val)
        return elements