# Created by woxQAQ at 2025/08/26 17:15
# leetgo: 1.4.15
# https://leetcode.cn/problems/maximum-multiplication-score/

"""
3290. 最高乘法得分 (Medium)
给你一个大小为 4 的整数数组 `a` 和一个大小 **至少** 为 4 的整数数组 `b`。

你需要从数组 `b` 中选择四个下标 `i₀`, `i₁`, `i₂`, 和 `i₃`，并满足 `i₀ < i₁ < i₂ < i₃`。你的得分将是
`a[0] * b[i₀] + a[1] * b[i₁] + a[2] * b[i₂] + a[3] * b[i₃]` 的值。

返回你能够获得的 **最大** 得分。

**示例 1：**

**输入：** a = \[3,2,5,6\], b = \[2,-6,4,-5,-3,2,-7\]

**输出：** 26

**解释：**

选择下标 0, 1, 2 和 5。得分为 `3 * 2 + 2 * (-6) + 5 * 4 + 6 * 2 = 26`。

**示例 2：**

**输入：** a = \[-1,4,5,-2\], b = \[-5,-1,-3,-2,-4\]

**输出：**-1

**解释：**

选择下标 0, 1, 3 和 4。得分为 `(-1) * (-5) + 4 * (-1) + 5 * (-2) + (-2) * (-4) = -1`。

**提示：**

- `a.length == 4`
- `4 <= b.length <= 10⁵`
- `-10⁵ <= a[i], b[i] <= 10⁵`

"""

from functools import cache
from math import inf
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        @cache
        def dfs(i, j):
            if i < 0:
                return 0
            if j < 0:
                return -inf
            return max(dfs(i - 1, j - 1) + a[i] * b[j], dfs(i, j - 1))

        s = dfs(3, len(b) - 1)
        dfs.cache_clear()
        return s


# @lc code=end

if __name__ == "__main__":
    a: List[int] = deserialize("List[int]", read_line())
    b: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxScore(a, b)
    print("\noutput:", serialize(ans, "long"))
