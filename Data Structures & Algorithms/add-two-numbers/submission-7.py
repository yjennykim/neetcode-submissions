# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # carry 
        carry = 0
        dummy = curr = ListNode() # dummy node to initialize head

        # while both lists are valid
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0 
            v2 = l2.val if l2 else 0

            added = v1 + v2 + carry
        
            carry = added // 10
            node = ListNode(added % 10)

            curr.next = node
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy.next