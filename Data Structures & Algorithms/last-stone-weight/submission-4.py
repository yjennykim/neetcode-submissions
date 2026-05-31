import heapq # default min heap, which means smallest number is the root

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones)

        while len(stones) > 1:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)
            if y < x:
                heapq.heappush(stones, -(x-y))

        return -stones[0] if len(stones) == 1 else 0
