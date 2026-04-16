# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head 
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        second = slow.next

        prev = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        slow.next = None

        first, second = head, prev

        while second: 
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

        # [0, 1, 2]
        # [6, 5, 4, 3]
        # [0, 1, 2] first.next tmp1 
        # [6, 5, 4, 3] second.next tmp2 
        # first [0] -> tmp2 -> [0, 6, 5, 4, 3]
        # second = tmp2.next -> [5, 4, 3]
