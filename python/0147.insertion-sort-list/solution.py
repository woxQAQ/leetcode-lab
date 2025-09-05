# Created by woxQAQ at 2025/09/05 09:48
# leetgo: 1.4.15
# https://leetcode.cn/problems/insertion-sort-list/

from typing import *
from leetgo_py import *

# @lc code=begin


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        pre = dummy
        cur = head
        while cur:
            tmp = cur.next
            while pre.next and pre.next.val < cur.val:
                pre = pre.next
            cur.next = pre.next
            pre.next = cur
            pre = dummy
            cur = tmp
        return dummy.next


# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    ans = Solution().insertionSortList(head)
    print("\noutput:", serialize(ans, "ListNode"))
