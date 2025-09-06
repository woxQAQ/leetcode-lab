# Created by woxQAQ at 2025/09/06 07:34
# leetgo: 1.4.15
# https://leetcode.cn/problems/binary-tree-right-side-view/

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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def dfs(node, depth):
            if not node:
                return
            if depth == len(ans):
                ans.append(node.val)
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return ans


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().rightSideView(root)
    print("\noutput:", serialize(ans, "integer[]"))
