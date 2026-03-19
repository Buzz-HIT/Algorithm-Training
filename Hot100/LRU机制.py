class DeListNode(object):
    def __init__(self, key = 0, val = 0):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        from collections import defaultdict
        self.cache = defaultdict(DeListNode)
        self.capacity = capacity
        self.size = 0
        self.head = DeListNode()
        self.tail = DeListNode()
        self.head.next = self.tail
        self.tail.pre = self.head
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self.cache.get(key, None) == None:
            return -1
        else:
            node = self.cache[key]
            self.moveToHead(node)
            return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.cache.get(key, None) == None:
            node = DeListNode(key, value)
            self.cache[key] = node
            node.next = self.head.next
            self.head.next = node
            node.pre = node.next.pre
            node.next.pre = node
            self.size += 1
            if self.size > self.capacity:
                delNode = self.deleteTail()
                del self.cache[delNode.key]
                self.size -= 1
        else:
            node = self.cache[key]
            self.moveToHead(node)
            node.val = value


    def moveToHead(self,node):
        self.deleteNode(node)
        node.next = self.head.next
        self.head.next = node
        node.next.pre = node
        node.pre = self.head

    def deleteNode(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
    
    def deleteTail(self):
        node = self.tail.pre
        node.pre.next = self.tail
        self.tail.pre = node.pre
        return node
    def printList(self):
        cur = self.head
        while cur:
            print(cur.key,cur.val,end="-")
            cur = cur.next

obj = LRUCache(2)
obj.put(1,1)
obj.put(2,2)
obj.printList()
print("")
print(obj.get(1))
obj.put(3,3)
obj.printList()