# Created by woxQAQ at 2025/09/05 07:23
# leetgo: 1.4.15
# https://leetcode.cn/problems/merge-in-between-linked-lists/

from typing import *
from leetgo_py import *

# @lc code=begin


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(
        self, list1: ListNode, a: int, b: int, list2: ListNode
    ) -> ListNode:
        l = 0
        cur = list1
        prev = cur
        while l != a:
            prev = cur
            cur = cur.next
            l += 1
        prev.next = list2
        while list2.next:
            list2 = list2.next
        while l != b:
            cur = cur.next
            l += 1
        list2.next = cur.next
        cur.next = None
        return list1


# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    list1: ListNode = deserialize("ListNode", read_line())
    a: int = deserialize("int", read_line())
    b: int = deserialize("int", read_line())
    list2: ListNode = deserialize("ListNode", read_line())
    ans = Solution().mergeInBetween(list1, a, b, list2)
    print("\noutput:", serialize(ans, "ListNode"))
