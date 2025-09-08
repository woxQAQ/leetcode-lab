# Created by woxQAQ at 2025/09/07 10:06
# leetgo: 1.4.15
# https://leetcode.cn/problems/deepest-leaves-sum/

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
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = [root]
        while q:
            ans = 0
            for _ in range(len(q)):
                node = q.pop(0)
                ans += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if not q:
                return ans


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().deepestLeavesSum(root)
    print("\noutput:", serialize(ans, "integer"))
