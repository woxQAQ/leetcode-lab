# Created by woxQAQ at 2025/09/05 04:55
# leetgo: 1.4.15
# https://leetcode.cn/problems/linked-list-components/

from typing import *
from leetgo_py import *

# @lc code=begin


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        s = set(nums)
        ans = 0
        while head:
            if head.val in s:
                ans += 1
                while head and head.val in s:
                    head = head.next
            else:
                head = head.next
        return ans


# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().numComponents(head, nums)
    print("\noutput:", serialize(ans, "integer"))
