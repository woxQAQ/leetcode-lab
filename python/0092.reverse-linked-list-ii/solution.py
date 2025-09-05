# Created by woxQAQ at 2025/09/05 07:36
# leetgo: 1.4.15
# https://leetcode.cn/problems/reverse-linked-list-ii/

from typing import *
from leetgo_py import *

# @lc code=begin


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        next_ = None

        def reverseN(head, n):
            nonlocal next_
            if n == 1:
                next_ = head.next
                return head
            last = reverseN(head.next, n - 1)
            head.next.next = head
            head.next = next_
            return last

        if left == 1:
            return reverseN(head, right)
        head.next = self.reverseBetween(head.next, left - 1, right - 1)
        return head


# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    left: int = deserialize("int", read_line())
    right: int = deserialize("int", read_line())
    ans = Solution().reverseBetween(head, left, right)
    print("\noutput:", serialize(ans, "ListNode"))
