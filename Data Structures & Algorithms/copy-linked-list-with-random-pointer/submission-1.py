"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mapping = {} # holds mapping from node -> copied node

        curr, copiedHead = head, Node(-1)
        
        prev = copiedHead
        while curr:
            copiedCurr = None
            # already created by another node
            if curr in mapping:
                copiedCurr = mapping[curr]
            else:
                copiedCurr = Node(curr.val)
                # add this to mapping
                mapping[curr] = copiedCurr

            # creating random node
            if curr.random in mapping:
                copiedCurr.random = mapping[curr.random]
            else:
                copiedRandom = None if not curr.random else Node(curr.random.val)
                copiedCurr.random = copiedRandom
                mapping[curr.random] = copiedRandom
            

            # set previous node's next ptr
            prev.next = copiedCurr
            prev = copiedCurr

            # next node
            curr = curr.next
        
        return copiedHead.next