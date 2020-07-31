class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        self.capacity = capacity
        self.hash = {}
 
    def insert(self, node):
        node.next = self.head.next
        node.prev = self.head
        node.next.prev = node
        self.head.next = node
        self.size += 1    

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        return node

    def remove_tail(self):
        if self.size == 0:
            return None
        return self.remove(self.tail.prev)

    def get_node(self, key):
        node = self.hash.get(key, None)
        if not node:
            return None
        self.remove(node)
        self.insert(node)
        return node

    def get(self, key: int) -> int:
        node = self.get_node(key)
        if not node:
            return -1
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            node = self.get_node(key)
            node.val = value
        else:
            if self.size >= self.capacity:
                last = self.remove_tail()
                self.hash.pop(last.key)
            node = Node(key, value)
            self.insert(node)
            self.hash[key] = node
