# Created by woxQAQ at 2025/09/06 15:09
# leetgo: 1.4.15
# https://leetcode.cn/problems/find-mode-in-binary-search-tree/

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
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        cnt = []
        cur = 0
        count = 0
        max_count = 0

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            nonlocal cur, count, max_count
            if node.val == cur:
                count += 1
            else:
                cur = node.val
                count = 1
            if count == max_count:
                cnt.append(cur)
            elif count > max_count:
                max_count = count
                cnt.clear()
                cnt.append(cur)
            dfs(node.right)

        dfs(root)
        return cnt


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().findMode(root)
    print("\noutput:", serialize(ans, "integer[]"))
