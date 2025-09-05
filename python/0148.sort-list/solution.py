# Created by woxQAQ at 2025/09/05 08:43
# leetgo: 1.4.15
# https://leetcode.cn/problems/sort-list/

from typing import *
from leetgo_py import *

# @lc code=begin


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, l1: ListNode, l2: ListNode) -> Optional[ListNode]:
        t1, t2 = l1, l2
        cur = dummy = ListNode()
        while t1 and t2:
            if t1.val < t2.val:
                cur.next = t1
                t1 = t1.next
            else:
                cur.next = t2
                t2 = t2.next
            cur = cur.next
        cur.next = t1 if t1 else t2
        return dummy.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        # Split the list into two halves
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        next = slow.next
        slow.next = None
        l = self.sortList(head)
        r = self.sortList(next)
        return self.merge(l, r)


# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    ans = Solution().sortList(head)
    print("\noutput:", serialize(ans, "ListNode"))
