# Created by woxQAQ at 2025/09/06 09:26
# leetgo: 1.4.15
# https://leetcode.cn/problems/flip-binary-tree-to-match-preorder-traversal/

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
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        ans = []

        def dfs(node, idx):
            if node is None:
                return True, idx
            if node.val != voyage[idx]:
                return False, idx
            # 先尝试正常先序
            left_success, left_idx = dfs(node.left, idx + 1)
            if left_success:
                right_success, right_idx = dfs(node.right, left_idx)
                if right_success:
                    return True, right_idx
            # 正常先序不满足，则尝试翻转后的先序
            right_success, right_idx = dfs(node.right, idx + 1)
            if right_success:
                left_success, left_idx = dfs(node.left, right_idx)
                if left_success:
                    ans.append(node.val)
                    return True, left_idx
            return False, idx

        return ans if dfs(root, 0)[0] else [-1]


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    voyage: List[int] = deserialize("List[int]", read_line())
    ans = Solution().flipMatchVoyage(root, voyage)
    print("\noutput:", serialize(ans, "integer[]"))
