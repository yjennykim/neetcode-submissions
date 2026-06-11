# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
            
        head_ptr = head
        prev = None

        while head_ptr:
            temp = head_ptr.next
            head_ptr.next = prev
            prev = head_ptr
            head_ptr = temp
        
        return prev 