class ListNode:
    def __init__(self, val = 0, next = None):
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

def buildcircleList(head, start):
    if head == None:
        return None
    cur = head
    while cur.next:
        cur = cur.next
    cur.next = start
    return head

def circleList(head):
    fastIndex = head
    slowIndex = head

    while fastIndex.next and fastIndex.next.next:
        slowIndex = slowIndex.next
        fastIndex = fastIndex.next.next
        if fastIndex == slowIndex:
            cur = head
            while cur != fastIndex:
                cur = cur.next
                fastIndex = fastIndex.next
            return cur
    return None

# nums = [3, 2, 0, -4]
nums = [1, 2]
head = buildList(nums)
start = head
for i in range(0):
    start = start.next
head = buildcircleList(head, start)

print(circleList(head).val)