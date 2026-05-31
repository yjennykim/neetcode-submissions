import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # count instances of each task
        count = Counter(tasks)

        # negate values to add to max heap
        maxHeap = [-cnt for cnt in count.values()]

        # add instances into max heap
        heapq.heapify(maxHeap)

        # initialize counter for cpu cycles + queue 
        time = 0
        q = deque()

        # heap to get next most common task, and add to queue 
        # queue to handle time, pop when time is met
        while len(maxHeap) > 0 or len(q) > 0:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
                
            # if it's time to pop
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

                
        return time






