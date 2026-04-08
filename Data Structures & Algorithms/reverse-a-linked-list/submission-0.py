# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Linked list [1|val_1]->[2|val_2]->[3|val_3]->[4|val_4]
# Linked list [1|val_1]->[2|val_2]->[3|val_3]->[4|val_4]
# head.next = [1|val_1]->[2|val_2]
# head.val = val_2
# temp = head.val
# head.next = head.next.next 
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev

            prev = curr
            curr = next_node
        
        return prev