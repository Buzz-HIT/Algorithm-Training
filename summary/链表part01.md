# 代码随想录算法训练营74期|链表part01 链表基本操作

| 题目     | Leetcode地址 |
| ----------- | ----------- |
| 203.移除链表元素| [力扣题目链接](https://leetcode.cn/problems/remove-linked-list-elements/description/)      |
|206.翻转链表| [力扣题目链接](https://leetcode.cn/problems/reverse-linked-list/description/)        |
|707.设计链表|[力扣题目链接](https://leetcode.cn/problems/design-linked-list/description/)

链表是一种常见的数据结构，它由一系列节点（链表结点）组成，每个节点包含两个部分：数据域和指针域。数据域存储节点的值，指针域存储下一个节点的指针。链表具有动态 Nature，可以根据需要动态地增加或删除节点。
链表的基本操作比较常见，一些复杂的操作也是由基本操作演化而来，一般来说，给链表的头部加一个哨兵节点，因为删除节点一般需要前面的节点来进行操作，所以哨兵节点可以简化很多操作。当然，要根据实际情况来判断。
下面是相关题目：
1. 203. 移除链表元素：删除链表中所有值为 val 的节点。经典的删除节点操作。
2. 707. 设计链表：设计一个链表，支持插入、删除、获取元素等操作，这道题操作思想比较简单，需要注意的是怎么实现python的类，代码如下：
```python
class MyLinkedList(object): # 707.设计链表

    def __init__(self):
        self.dummy_head = ListNode()
        self.len = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.len:
            return -1
        else:
            cur = self.dummy_head.next
            for i in range(index):
                cur = cur.next
            return cur.val
    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.dummy_head.next = ListNode(val, self.dummy_head.next)
        self.len += 1
    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        cur = self.dummy_head
        while cur.next:
            cur = cur.next
        cur.next = ListNode(val)
        self.len += 1

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0 or index > self.len:
            return
        else:
            cur = self.dummy_head
            for i in range(index):
                cur = cur.next
            cur.next = ListNode(val, cur.next)
            self.len += 1
    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.len:
            return
        else:
            cur = self.dummy_head
            for i in range(index):
                cur = cur.next
            cur.next = cur.next.next
            self.len -= 1
```
3. 206. 翻转链表：反转一个单链表。一般来说，翻转链表需要三个指针，一个指向当前节点，一个指向当前节点的前一个节点，一个指向当前节点的后一个节点。这样才不会丢失，如果觉得比较复杂的话，可以草稿纸上画一画。当然，翻转列表也有递归的写法。