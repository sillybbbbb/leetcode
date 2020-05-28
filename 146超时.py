'''
146. LRU缓存机制
运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。

获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
写入数据 put(key, value) - 如果密钥已经存在，则变更其数据值；如果密钥不存在，则插入该组「密钥/数据值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。

 

进阶:

你是否可以在 O(1) 时间复杂度内完成这两种操作？

 

示例:

LRUCache cache = new LRUCache( 2 /* 缓存容量 */ )

cache.put(1, 1)
cache.put(2, 2)
cache.get(1)       # 返回  1
cache.put(3, 3)    # 该操作会使得密钥 2 作废
cache.get(2)       # 返回 -1 (未找到)
cache.put(4, 4)    # 该操作会使得密钥 1 作废
cache.get(1)       # 返回 -1 (未找到)
cache.get(3)       # 返回  3
cache.get(4)       # 返回  4
'''

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.now = 0
        self.dic = {}
    def get(self, key: int) -> int:
        if key not in self.dic.keys():
            print(-1)
            return -1
            
        else: 
            for k in self.dic.keys():
                if k!= key:
                    self.dic[k].use +=1
                else:
                    self.dic[k].use = 0
            print(self.dic[key].value)
            return self.dic[key].value
            

    def put(self, key: int, value: int) -> None:
        class a:
            value = 0
            use = 0
        a.value = value
        a.use = 0
        if  key in self.dic.keys():
            self.dic[key].value = value
            for k in self.dic.keys():
                if k!= key:
                    self.dic[k].use +=1
                else:
                    self.dic[k].use = 0
            return
        if self.now < self.cap:
            
            self.dic[key] = a
            self.now +=1
        
        else:
            dk = self.finddelete()
            self.dic.pop(dk)
            self.dic[key] = a
        for k in self.dic.keys():
            if k!= key:
                self.dic[k].use +=1
            else:
                self.dic[k].use = 0
    def finddelete(self):
        tmp = 0
        #rec = self.dic.keys()[0]
        for iter in self.dic.keys():
            if self.dic[iter].use >=tmp :
                rec = iter
                tmp = self.dic[iter].use
        return rec


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
