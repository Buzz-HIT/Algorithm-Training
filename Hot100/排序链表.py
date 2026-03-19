class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head  # 递归终止条件
 
        # 使用快慢指针找到链表中点
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        slow.next = None  # 断开链表，分成两部分
 
        # 递归拆分 & 归并排序
        left = self.sortList(head)
        right = self.sortList(mid)
        
        return self.merge(left, right)  # 归并两个有序链表

    def merge(self, head1, head2):
        dummy = ListNode(0)
        cur = dummy
        while head1 and head2:
            if head1.val < head2.val:
                cur.next = head1
                head1 = head1.next
            else:
                cur.next = head2
                head2 = head2.next
            cur = cur.next
        if head1:
            cur.next = head1
        else:
            cur.next = head2
        return dummy.next
