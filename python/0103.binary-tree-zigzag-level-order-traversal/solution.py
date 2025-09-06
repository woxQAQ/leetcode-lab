# Created by woxQAQ at 2025/09/06 16:54
# leetgo: 1.4.15
# https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/

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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = [root]
        while q:
            level = []
            for _ in range(len(q)):
                node = q.pop(0)
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level[::-1] if len(res) % 2 else level)

        return res


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().zigzagLevelOrder(root)
    print("\noutput:", serialize(ans, "integer[][]"))
