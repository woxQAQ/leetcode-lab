# Created by woxQAQ at 2025/09/06 16:58
# leetgo: 1.4.15
# https://leetcode.cn/problems/find-bottom-left-tree-value/

from collections import deque
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
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        node = None
        while q:
            node = q.popleft()
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
        return node.val


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().findBottomLeftValue(root)
    print("\noutput:", serialize(ans, "integer"))
