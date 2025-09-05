# Created by woxQAQ at 2025/09/05 08:12
# leetgo: 1.4.15
# https://leetcode.cn/problems/swapping-nodes-in-a-linked-list/

from typing import *
from leetgo_py import *

# @lc code=begin


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        tar = None

        def dfs(head):
            nonlocal tar
            if not head:
                return 0
            depth = dfs(head.next) + 1
            if depth == k:
                tar = head
            return depth

        dfs(head)
        cur = head
        while k > 1:
            cur = cur.next
            k -= 1
        tar.val, cur.val = cur.val, tar.val
        return head


# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().swapNodes(head, k)
    print("\noutput:", serialize(ans, "ListNode"))
