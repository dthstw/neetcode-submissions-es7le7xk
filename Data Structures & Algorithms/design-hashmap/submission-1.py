class LinkedList():
    def __init__(self, key, val, next=None):
        self.key = key
        self.val = val
        self.next = next


class MyHashMap:

    def __init__(self):
        self.arr = [LinkedList(None, None) for _ in range(1000)]

    def put(self, key: int, value: int) -> None:
        index = key % 1000
        cur = self.arr[index]
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        cur.next = LinkedList(key, value)

    def get(self, key: int) -> int:
        index = key % 1000
        cur = self.arr[index]
        while cur.next:
            if cur.next.key == key:
                return cur.next.val
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        index = key % 1000
        cur = self.arr[index]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next
        return

        

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)