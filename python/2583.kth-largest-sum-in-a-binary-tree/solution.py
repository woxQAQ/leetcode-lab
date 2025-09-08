# Created by woxQAQ at 2025/09/07 09:33
# leetgo: 1.4.15
# https://leetcode.cn/problems/kth-largest-sum-in-a-binary-tree/

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
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q = [root]
        tmp = []
        while q:
            level = []
            for _ in range(len(q)):
                node = q.pop(0)
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            tmp.append(sum(level))
        if len(tmp) < k:
            return -1
        tmp.sort(reverse=True)
        return tmp[k - 1]


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().kthLargestLevelSum(root, k)
    print("\noutput:", serialize(ans, "long"))
