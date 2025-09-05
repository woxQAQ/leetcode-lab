# Created by woxQAQ at 2025/09/05 07:29
# leetgo: 1.4.15
# https://leetcode.cn/problems/reverse-linked-list/

from typing import *
from leetgo_py import *

# @lc code=begin


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        next = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return next


# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    ans = Solution().reverseList(head)
    print("\noutput:", serialize(ans, "ListNode"))
