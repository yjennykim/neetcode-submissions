import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __lt__(self, other):
        return self.val < other.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap= []
        dummy = ListNode(-1)
        prev = dummy

        for h in lists:
            heapq.heappush(minHeap, h)
        
        while minHeap:
            node = heapq.heappop(minHeap)
            prev.next = node

            if node.next:
                heapq.heappush(minHeap, node.next)
            
            prev = prev.next
        
        return dummy.next