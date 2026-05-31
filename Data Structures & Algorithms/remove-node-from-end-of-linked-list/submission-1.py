# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# space = O(1), no extra space
# runtime = O(n), since O(n/2) + O(n/2) for traversing first half twice or the full list
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
                # count how many nodes are in linked list
        slow, fast = head, head.next
        total = 1
        while fast and fast.next:
            slow = slow.next
            total += 1
            fast = fast.next.next

        if not fast:
            # odd
            total = total * 2 - 1
        elif not fast.next:
            # even
            total *= 2
        print(f"total {total}")

        # base cases
        if total < n:
            return None

        if total == 2:
            if n == 1:
                head.next = None
                return head
            if n == 2:
                tmp = head.next
                head.next = None
                head = None
            return tmp

        if total == n:
            tmp = head.next
            head.next = None
            head = None
            return tmp

        count = 0
        # determine whether to search left or right side of midpoint [1,2,3,4,5] n=2 5-2=3
        indexFromFront = total - n  # zero indexing
        print(f"index of node to remove {indexFromFront}")
        rightSideStartIndex = math.ceil(total / 2)
        print(f"index of right side {rightSideStartIndex}")

        shouldExploreLeft = indexFromFront < rightSideStartIndex
        prev = None
        if shouldExploreLeft:
            start = head
        else:
            prev = slow
            start = slow.next
            count = rightSideStartIndex
        end = indexFromFront
        print(f"shouldExploreLeft={shouldExploreLeft}, starting={start.val}, rightSideStartIndex={rightSideStartIndex}")

        # find node (start) to remove, starting from head or midpoint
        while count < end:
            prev = start
            start = start.next
            count += 1

        # adjust pointers
        prev.next = start.next
        start.next = None

        return head
            

        