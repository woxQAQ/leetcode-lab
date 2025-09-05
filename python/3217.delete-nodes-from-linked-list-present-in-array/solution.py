# Created by woxQAQ at 2025/09/05 06:33
# leetgo: 1.4.15
# https://leetcode.cn/problems/delete-nodes-from-linked-list-present-in-array/

from typing import *
from leetgo_py import *

# @lc code=begin


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        s = set(nums)
        cur = dummy
        while cur.next:
            if cur.next.val in s:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    head: ListNode = deserialize("ListNode", read_line())
    ans = Solution().modifiedList(nums, head)
    print("\noutput:", serialize(ans, "ListNode"))
