# Created by woxQAQ at 2025/09/05 07:30
# leetgo: 1.4.15
# https://leetcode.cn/problems/reverse-nodes-in-k-group/

from typing import *
from leetgo_py import *

# @lc code=begin


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head):
            if head is None or head.next is None:
                return head
            next = reverse(head.next)
            head.next.next = head
            head.next = None
            return next

        head_k, tail = head, head
        for _ in range(k):
            if head_k is None:
                return head
            head_k, tail = head_k.next, head_k
        tail.next = None
        reverse(head)
        next_k = self.reverseKGroup(head_k, k)
        head.next = next_k
        return tail


# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().reverseKGroup(head, k)
    print("\noutput:", serialize(ans, "ListNode"))
