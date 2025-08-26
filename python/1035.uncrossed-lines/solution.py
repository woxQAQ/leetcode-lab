# Created by woxQAQ at 2025/08/26 16:55
# leetgo: 1.4.15
# https://leetcode.cn/problems/uncrossed-lines/

"""
1035. 不相交的线 (Medium)
在两条独立的水平线上按给定的顺序写下 `nums1` 和 `nums2` 中的整数。

现在，可以绘制一些连接两个数字 `nums1[i]` 和 `nums2[j]` 的直线，这些直线需要同时满足：

- `nums1[i] == nums2[j]`
- 且绘制的直线不与任何其他连线（非水平线）相交。

请注意，连线即使在端点也不能相交：每个数字只能属于一条连线。

以这种方法绘制线条，并返回可以绘制的最大连线数。

**示例 1：**

![](https://assets.leetcode.com/uploads/2019/04/26/142.png)

```
输入：nums1 = [1,4,2], nums2 = [1,2,4]
输出：2
解释：可以画出两条不交叉的线，如上图所示。
但无法画出第三条不相交的直线，因为从 nums1[1]=4 到 nums2[2]=4 的直线将与从 nums1[2]=2 到 nums2[1]=2
的直线相交。
```

**示例 2：**

```
输入：nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2]
输出：3
```

**示例 3：**

```
输入：nums1 = [1,3,7,1,7,5], nums2 = [1,9,2,5,1]
输出：2
```

**提示：**

- `1 <= nums1.length, nums2.length <= 500`
- `1 <= nums1[i], nums2[j] <= 2000`

"""

from functools import cache
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        """
        1 4 2

        1 2 4

        if nums[i] == nums[j], 尝试连线
        """

        @cache
        def dfs(i, j):
            if i < 0 or j < 0:
                return 0
            if nums1[i] == nums2[j]:
                return dfs(i - 1, j - 1) + 1
            return max(dfs(i - 1, j), dfs(i, j - 1))

        return dfs(len(nums1) - 1, len(nums2) - 1)


# @lc code=end

if __name__ == "__main__":
    nums1: List[int] = deserialize("List[int]", read_line())
    nums2: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxUncrossedLines(nums1, nums2)
    print("\noutput:", serialize(ans, "integer"))
