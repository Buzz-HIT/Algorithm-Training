class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def buildList(nums):
    if len(nums) == 0:
        return None
    dummyHead = Node()
    head = Node(nums[0])
    cur = head
    for i in nums[1:]:
        cur.next = Node(i)
        cur = cur.next
    dummyHead.next = head
    return dummyHead

def deleteList(head, n):
    slowIndex = head
    fastIndex = head

    for i in range(n):
        if fastIndex == None:
            return head
        fastIndex = fastIndex.next
    while fastIndex.next:
        slowIndex = slowIndex.next
        fastIndex = fastIndex.next
    slowIndex.next = slowIndex.next.next
    return head.next

