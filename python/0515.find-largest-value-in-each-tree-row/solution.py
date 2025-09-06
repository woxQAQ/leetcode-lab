# Created by woxQAQ at 2025/09/06 16:59
# leetgo: 1.4.15
# https://leetcode.cn/problems/find-largest-value-in-each-tree-row/

from collections import deque
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
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        q = [root]
        res = []
        while q:
            p = q
            q = []
            max_val = -inf
            for node in p:
                if not node:
                    continue
                max_val = max(max_val, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if max_val != -inf:
                res.append(max_val)
        return res


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().largestValues(root)
    print("\noutput:", serialize(ans, "integer[]"))
