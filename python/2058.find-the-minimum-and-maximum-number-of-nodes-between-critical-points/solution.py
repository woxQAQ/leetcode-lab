# Created by woxQAQ at 2025/09/04 20:20
# leetgo: 1.4.15
# https://leetcode.cn/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/

from typing import *
from leetgo_py import *

# @lc code=begin


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        points = []
        prev = None
        index = 1
        while head:
            if prev and head.next:
                if (
                    prev.val < head.val > head.next.val
                    or prev.val > head.val < head.next.val
                ):
                    points.append(index)
            prev = head
            head = head.next
            index += 1
        if len(points) < 2:
            return [-1, -1]
        points.sort()
        min_p = 100_000
        for i in range(1, len(points)):
            min_p = min(min_p, points[i] - points[i - 1])
        max_p = points[-1] - points[0]
        return [min_p, max_p]


# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    ans = Solution().nodesBetweenCriticalPoints(head)
    print("\noutput:", serialize(ans, "integer[]"))
