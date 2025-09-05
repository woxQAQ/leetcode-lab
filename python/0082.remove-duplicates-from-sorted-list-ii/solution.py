# Created by woxQAQ at 2025/09/05 07:05
# leetgo: 1.4.15
# https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii/

from typing import *
from leetgo_py import *

# @lc code=begin


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode(next=head)
        while cur.next and cur.next.next:
            val = cur.next.val
            if cur.next.next.val == val:
                while cur.next and cur.next.val == val:
                    cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy.next


# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    ans = Solution().deleteDuplicates(head)
    print("\noutput:", serialize(ans, "ListNode"))
