# Created by woxQAQ at 2025/09/05 07:40
# leetgo: 1.4.15
# https://leetcode.cn/problems/swap-nodes-in-pairs/

from typing import *
from leetgo_py import *

# @lc code=begin


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        nexthead = head.next
        head.next = self.swapPairs(nexthead.next)
        nexthead.next = head
        return nexthead


# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    ans = Solution().swapPairs(head)
    print("\noutput:", serialize(ans, "ListNode"))
