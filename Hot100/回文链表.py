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

def printList(head):
    cur = head
    while cur:
        print(cur.val, end="->")
        cur = cur.next
    print("None")

    

def reverseList(head):
    pre = head
    cur = head.next
    pre.next = None
    
    while cur:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    return pre

def isPalindrome(head):
    lenA = 0
    cur = head
    while cur:
        lenA += 1
        cur = cur.next
    if lenA == 1:
        return True
    n = lenA // 2
    cur = head
    for i in range(n):
        cur = cur.next
    right = reverseList(cur)
    left = head
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    return True

nums = [1,2,6,6,2,1]
head = buildList(nums)
print(isPalindrome(head))

