class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def buildList(nums):
    if len(nums) == 0:
        return None
    head = ListNode(nums[0])
    cur = head
    for i in nums[1:]:
        cur.next = ListNode(i)
        cur = cur.next
    return head

def buildCircleList(head, start):
    if head == None:
        return None
    cur = head
    while cur.next:
        cur = cur.next
    cur.next = start
    return head

def hasCircle(head):
    if head == None:
        return False
    slowIndex = head
    fastIndex = head

    while fastIndex.next and fastIndex.next.next:
        slowIndex = slowIndex.next
        fastIndex = fastIndex.next.next
        if slowIndex == fastIndex:
            return True
    return False

nums = [3,2,0,-4]
head = buildList(nums)
start = head
for i in range(1):
    start = start.next
head = buildCircleList(head, None)

print(hasCircle(head))
