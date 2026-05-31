import heapq
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Define a less-than method for comparison in the heap
    def __lt__(self, other):
        return self.val < other.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Initialize the min-heap
        heap = []
        
        # Populate the heap with the head of each list
        for l in lists:
            if l:
                heapq.heappush(heap, l)
        
        # Initialize a dummy head and prev pointer
        dummy = ListNode(-1)
        prev = dummy
        
        while heap:
            # Pop the smallest item from the heap
            node = heapq.heappop(heap)
            prev.next = node  # Link the smallest node
            prev = prev.next   # Move prev pointer to next
            
            # If there is a next node in the list, push it to the heap
            if node.next:
                heapq.heappush(heap, node.next)
        
        return dummy.next
