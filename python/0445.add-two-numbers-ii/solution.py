# Created by woxQAQ at 2025/09/05 09:26
# leetgo: 1.4.15
# https://leetcode.cn/problems/add-two-numbers-ii/

from typing import *
from leetgo_py import *

# @lc code=begin


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        def reverse(head):
            if head is None or head.next is None:
                return head
            next_head = reverse(head.next)
            head.next.next = head
            head.next = None
            return next_head

        t1 = reverse(l1)
        t2 = reverse(l2)
        dummy = cur = ListNode()

        while t1 or t2:
            if t1:
                cur.val += t1.val
                t1 = t1.next
            if t2:
                cur.val += t2.val
                t2 = t2.next
            cur.next = ListNode(cur.val // 10)
            cur.val %= 10
            cur = cur.next

        dummy = reverse(dummy)
        if dummy.val == 0:
            dummy = dummy.next
        return dummy


# @lc code=end

if __name__ == "__main__":
    l1: ListNode = deserialize("ListNode", read_line())
    l2: ListNode = deserialize("ListNode", read_line())
    ans = Solution().addTwoNumbers(l1, l2)
    print("\noutput:", serialize(ans, "ListNode"))
