# Created by woxQAQ at 2025/09/06 08:22
# leetgo: 1.4.15
# https://leetcode.cn/problems/smallest-string-starting-from-leaf/

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
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        ans = ""

        def dfs(node, path):
            if not node:
                return
            nonlocal ans
            path.append(chr(node.val + ord("a")))
            if not node.left and not node.right:
                tmp = "".join(path[::-1])
                if not ans or tmp < ans:
                    ans = tmp
            dfs(node.left, path)
            dfs(node.right, path)
            path.pop()

        dfs(root, [])
        return ans


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().smallestFromLeaf(root)
    print("\noutput:", serialize(ans, "string"))
