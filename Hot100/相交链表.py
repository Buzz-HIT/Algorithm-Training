class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def build_List(nums):
    if len(nums) == 0 :
        return
    head = ListNode(nums[0])
    cur = head
    for i in nums[1:]:
        cur.next = ListNode(i)
        cur = cur.next
    return head

def getIntersectionNode(headA, headB, lenA, lenB): # A短B长
    curA = headA
    curB = headB
    for i in range(lenB - lenA):
        curB = curB.next
    while curA and curB:
        if curA == curB:
            return curA
        curA = curA.next
        curB = curB.next
    return None

def print_linked_list(head):
    cur = head
    while cur:
        print(cur.val, end=" -> ")
        cur = cur.next
    print("None")


# nums1 = [2, 6, 4]
# nums2 = [1 , 5]
# nums3 = []

nums1 = ['a1', 'a2']
nums2 = ['b1', 'b2', 'b3']
nums3 = ['c1', 'c2', 'c3']

headA = build_List(nums1)
headB = build_List(nums2)
headC = build_List(nums3)
# print_linked_list(headA)
# print_linked_list(headB)

lenA = len(nums1)
lenB = len(nums2)
curA = headA
curB = headB
while curA.next:
    curA = curA.next
curA.next = headC
while curB.next:
    curB = curB.next
curB.next = headC
if lenA > lenB:
    lenA, lenB = lenB, lenA 
    headA, headB = headB, headA


answer = getIntersectionNode(headA, headB, lenA, lenB)

if answer == None:
    print("NULL")
else:
    print(answer.val)