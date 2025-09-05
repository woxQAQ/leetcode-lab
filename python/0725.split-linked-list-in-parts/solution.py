# Created by woxQAQ at 2025/09/04 20:38
# leetgo: 1.4.15
# https://leetcode.cn/problems/split-linked-list-in-parts/

import re
from typing import *
from leetgo_py import *

# @lc code=begin


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:
        ans = []
        t = head
        length = 0
        while t:
            length += 1
            t = t.next
        size, remainder = divmod(length, k)
        cur = head
        idx = 0
        while cur:
            m = size + (1 if remainder > 0 else 0)
            remainder -= 1
            ans.append(cur)
            for _ in range(m - 1):
                cur = cur.next
            t = cur.next
            cur.next = None
            cur = t
            idx += 1
        if idx < k:
            ans.extend([None] * (k - idx))
        return ans


# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().splitListToParts(head, k)
    print("\noutput:", serialize(ans, "ListNode[]"))
