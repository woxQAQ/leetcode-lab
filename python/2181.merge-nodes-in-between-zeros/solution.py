# Created by woxQAQ at 2025/09/04 20:26
# leetgo: 1.4.15
# https://leetcode.cn/problems/merge-nodes-in-between-zeros/

from typing import *
from leetgo_py import *

# @lc code=begin


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t = head
        cur = head.next
        while cur.next:
            if cur.val:
                t.val += cur.val
            else:
                t = t.next
                t.val = 0
            cur = cur.next
        t.next = None
        return head


# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    ans = Solution().mergeNodes(head)
    print("\noutput:", serialize(ans, "ListNode"))
