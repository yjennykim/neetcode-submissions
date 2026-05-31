# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = None
        head = None

        while list1 and list2:
            if list1.val <= list2.val:
                if head is None:
                    curr = list1
                    head = curr
                else:
                    curr.next = list1
                    curr = curr.next
                
                list1 = list1.next
                
            else:
                if head is None:
                    curr = list2
                    head = curr
                else:
                    curr.next = list2
                    curr = curr.next

                list2 = list2.next
                
        if list1:
            if not head:
                head = list1
            else:
                curr.next = list1
        
        if list2:            
            if not head:
                head = list2
            else:
                curr.next = list2
        
        
        return head
