# Created by woxQAQ at 2025/09/06 16:55
# leetgo: 1.4.15
# https://leetcode.cn/problems/binary-tree-level-order-traversal-ii/

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
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
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
                res.append(level)
        print(res)
        return res[::-1]


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().levelOrderBottom(root)
    print("\noutput:", serialize(ans, "integer[][]"))
