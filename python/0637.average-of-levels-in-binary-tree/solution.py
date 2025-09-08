# Created by woxQAQ at 2025/09/06 19:41
# leetgo: 1.4.15
# https://leetcode.cn/problems/average-of-levels-in-binary-tree/

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
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = [root]
        res = []
        while q:
            length = len(q)
            res.append(sum(node.val for node in q) / length)
            for _ in range(length):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().averageOfLevels(root)
    print("\noutput:", serialize(ans, "double[]"))
