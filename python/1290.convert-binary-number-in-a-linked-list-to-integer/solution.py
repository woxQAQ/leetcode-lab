# Created by woxQAQ at 2025/09/04 20:06
# leetgo: 1.4.15
# https://leetcode.cn/problems/convert-binary-number-in-a-linked-list-to-integer/

from typing import *
from leetgo_py import *

# @lc code=begin


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        ans = 0
        while head:
            ans = ans * 2 + head.val
            head = head.next
        return ans


# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    ans = Solution().getDecimalValue(head)
    print("\noutput:", serialize(ans, "integer"))
