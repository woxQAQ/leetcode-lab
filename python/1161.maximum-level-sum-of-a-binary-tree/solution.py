# Created by woxQAQ at 2025/09/06 19:43
# leetgo: 1.4.15
# https://leetcode.cn/problems/maximum-level-sum-of-a-binary-tree/

from math import inf
from typing import *
from leetgo_py import *

# @lc code=begin


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = [root]
        level = 0
        pre_sum = -inf
        while q:
            level_sum = 0
            for _ in range(len(q)):
                node = q.pop(0)
                level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
            if level_sum > pre_sum:
                pre_sum = level_sum
                ans = level
        return ans


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().maxLevelSum(root)
    print("\noutput:", serialize(ans, "integer"))
