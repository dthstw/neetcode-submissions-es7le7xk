# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# у нас есть лист [1 2 3 4 5 6]
# мы хотим его реорганизовать в [0, 6, 1, 5, 2, 4, 3] -> принцип [0 n-1 1 n-2 2 n-3 3 ... ] - индксево
# n-1 n-2 n-3 n-4 это наш убывающий лист (реверсд) 
# таким образом нам надо просто взять наш лист + взять реверсд лист и просто засторить поочередно ноды в новом листе
# так как нам надо решить проблему with reorder (inplace) потребуется найти сначала середину листа чтобы разрезать его в нужном месте, для этого заюзаем slow and fast

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        #теперь надо понять как соединять из второго списка с конца
        # сделаем реверс второго

        prev = None
        curr = second
        while curr: 
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        first, second = head, prev
        while second:
            next_node = first.next # отвязываем первый лист
            next_node2=second.next #отвязываем второй лист

            first.next = second # присобачиваем первый элем из второго листа к первому [1, 2]
            second.next = next_node

            first = next_node
            second = next_node2

        return None
            