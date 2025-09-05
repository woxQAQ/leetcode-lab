# Created by woxQAQ at 2025/09/05 07:57
# leetgo: 1.4.15
# https://leetcode.cn/problems/rotate-list/

from typing import *
from leetgo_py import *

# @lc code=begin


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        cur = head
        n = 1
        while cur.next:
            n += 1
            cur = cur.next

        if (add := n - k % n) == n:
            return head

        cur.next = head
        while add:
            add -= 1
            cur = cur.next
        res = cur.next
        cur.next = None
        return res


# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().rotateRight(head, k)
    print("\noutput:", serialize(ans, "ListNode"))
