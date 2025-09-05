# Created by woxQAQ at 2025/09/05 05:48
# leetgo: 1.4.15
# https://leetcode.cn/problems/remove-linked-list-elements/

from typing import *
from leetgo_py import *

# @lc code=begin


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        prev = dummy
        curr = head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return dummy.next


# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    val: int = deserialize("int", read_line())
    ans = Solution().removeElements(head, val)
    print("\noutput:", serialize(ans, "ListNode"))
