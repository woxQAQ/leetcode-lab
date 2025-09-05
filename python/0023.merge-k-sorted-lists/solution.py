# Created by woxQAQ at 2025/09/05 08:26
# leetgo: 1.4.15
# https://leetcode.cn/problems/merge-k-sorted-lists/

from typing import *
from leetgo_py import *
from heapq import heapify, heappop, heappush
# @lc code=begin


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
ListNode.__lt__ = lambda a, b: a.val < b.val


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        h = [head for head in lists if head]
        heapify(h)
        while h:
            node = heappop(h)
            if node.next:
                heappush(h, node.next)
            cur.next = node
            cur = cur.next
        return dummy.next


# @lc code=end

if __name__ == "__main__":
    lists: List[ListNode] = deserialize("List[ListNode]", read_line())
    ans = Solution().mergeKLists(lists)
    print("\noutput:", serialize(ans, "ListNode"))
