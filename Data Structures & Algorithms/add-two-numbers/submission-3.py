# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # carry 
        carry = 0
        head = curr = None

        # while both lists are valid
        while l1 and l2:
            added = l1.val + l2.val + carry
            carry = added // 10
            node = ListNode(added % 10)
            if not head:
                head = curr = node
            else:
                curr.next = node
                curr = curr.next
            l1 = l1.next
            l2 = l2.next

        # while l1 is valid
        while l1:
            added = l1.val + carry
            carry = added // 10
            node = ListNode(added % 10)
            if not head: 
                head = curr = node
            else:
                curr.next = node
                curr = curr.next
            l1 = l1.next

        # while l2 is valid
        while l2:
            added = l2.val + carry
            carry = added // 10
            node = ListNode(added % 10)
            if not head: 
                head = curr = node
            else:
                curr.next = node
                curr = curr.next
            l2 = l2.next
        
        # carry value
        if carry > 0:
            curr.next = ListNode(carry)
        return head