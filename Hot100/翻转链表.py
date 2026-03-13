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

def printList(head):
    cur = head
    while cur:
        print(cur.val, end="->")
        cur = cur.next
    print("None")

def reverseList(head):
    pre = None
    cur = head
    while cur:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    return pre

# nums = [1,2,3,4,5]
# nums = [1,2]
nums = []
head = buildList(nums)
print("翻转前：")
printList(head)
head = reverseList(head)
print("翻转后：")
printList(head)