class ListNode:
    def __init__(self,key=None, value=None):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.pre = self.head
    
    def move_to_tail(self,key):
        node = self.hashmap[key]
        node.pre.next = node.next
        node.next.pre = node.pre
        node.pre =  self.tail.pre
        node.next = self.tail
        self.tail.pre.next = node
        self.tail.pre = node
    
    def add_to_tail(self,key,value):
        node = ListNode(key,value)
        node.pre =  self.tail.pre
        node.next = self.tail
        self.tail.pre.next = node
        self.tail.pre = node
        self.hashmap[key] = node
    
    def remove_head(self):
        self.hashmap.pop(self.head.next.key)
        self.head.next = self.head.next.next
        self.head.next.pre = self.head
        

    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.move_to_tail(key)
            print(self.hashmap[key].value)
            return self.hashmap[key].value
            
        else:
            print(-1)
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.move_to_tail(key)
            self.hashmap[key].value = value
            return
        
        if len(self.hashmap) < self.capacity:
            self.add_to_tail(key,value)
        
        else:
            self.remove_head()
            self.add_to_tail(key,value)

cache = LRUCache(2)
cache.put(1, 1)
cache.put(1, 5)
cache.get(1)       # 返回  1
cache.put(3, 3)    # 该操作会使得密钥 2 作废
cache.get(2)       # 返回 -1 (未找到)
cache.put(4, 4)    # 该操作会使得密钥 1 作废
cache.get(1)       # 返回 -1 (未找到)
cache.get(3)       # 返回  3
cache.get(4)  




