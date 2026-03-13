class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_linked_list(nums):
    if not nums:
        return None
    
    head = ListNode(nums[0])
    cur = head
    
    for num in nums[1:]:
        cur.next = ListNode(num)
        cur = cur.next
    
    return head

def print_linked_list(head):
    cur = head
    while cur:
        print(cur.val, end=" -> ")
        cur = cur.next
    print("None")

nums = list(map(int,input("head = ").split(',')))
head = build_linked_list(nums)
print_linked_list(head)
