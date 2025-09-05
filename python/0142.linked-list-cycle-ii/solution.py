# Created by woxQAQ at 2025/09/05 09:38
# leetgo: 1.4.15
# https://leetcode.cn/problems/linked-list-cycle-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while head != slow:
                    head = head.next
                    slow = slow.next
                return head
        return None


# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    pos: int = deserialize("int", read_line())
    ans = Solution().detectCycle(head, pos)
    print("\noutput:", serialize(ans, "ListNode"))
