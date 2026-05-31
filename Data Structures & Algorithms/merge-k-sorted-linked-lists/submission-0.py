import heapq
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Initialize the min-heap
        heap = []
        
        # Populate the heap with the head of each list
        for index, l in enumerate(lists):
            if l:
                heapq.heappush(heap, (l.val, index, l))
        
        # Initialize a dummy head and prev pointer
        dummy = ListNode(-1)
        prev = dummy
        
        while heap:
            # Pop the smallest item from the heap
            val, index, node = heapq.heappop(heap)
            prev.next = node  # Link the smallest node
            prev = prev.next   # Move prev pointer to next
            
            # If there is a next node in the list, push it to the heap
            if node.next:
                heapq.heappush(heap, (node.next.val, index, node.next))
        
        return dummy.next
