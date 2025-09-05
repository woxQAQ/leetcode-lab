# Created by woxQAQ at 2025/09/05 07:50
# leetgo: 1.4.15
# https://leetcode.cn/problems/remove-nth-node-from-end-of-list/

from typing import *
from leetgo_py import *

# @lc code=begin


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def dfs(head: Optional[ListNode]):
            if not head:
                return 0
            pos = dfs(head.next) + 1
            if pos == n + 1:
                head.next = head.next.next
            return pos

        dummy = ListNode(next=head)
        dfs(dummy)
        return dummy.next


# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    n: int = deserialize("int", read_line())
    ans = Solution().removeNthFromEnd(head, n)
    print("\noutput:", serialize(ans, "ListNode"))
