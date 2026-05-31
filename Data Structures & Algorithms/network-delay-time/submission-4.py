import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # create adjacency list, map ( ui -> (ti, vi) )
        adjacency_list = {}
        for ui, vi, ti in times:
            if ui not in adjacency_list:
                adjacency_list[ui] = []
            adjacency_list[ui].append((ti, vi))

        # visited set
        visited = set()

        # initialize PQ = minHeap
        minHeap = []
        heapq.heappush(minHeap, (0, k))

        # initialize timer
        total_time = 0

        # while PQ is not empty
        while minHeap:
            # pop node from PQ
            time, node = heapq.heappop(minHeap)
            if node in visited:
                continue

            total_time = time # QUESTION: why accumulated time, instead of adding as I go?

            # mark node as visited, increment timer by edge ti cost
            visited.add(node)

            # for node's neighbors v
            if node in adjacency_list:
                for ti,vi in adjacency_list[node]:
                    # add v to PQ if not in visited
                    if vi not in visited:
                        heapq.heappush(minHeap, (ti + time, vi))

        # base case: return -1 if not connected graph i.e. visited size != n
        if len(visited) != n:
            return -1

        # return timer
        return total_time

