# Created by woxQAQ at 2025/09/05 07:12
# leetgo: 1.4.15
# https://leetcode.cn/problems/delete-node-in-a-linked-list/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    node: int = deserialize("int", read_line())
    deleteNode(head, node)
    ans = head
    print("\noutput:", serialize(ans, "ListNode"))
