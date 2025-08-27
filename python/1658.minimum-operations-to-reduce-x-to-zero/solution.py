# Created by woxQAQ at 2025/08/28 03:48
# leetgo: 1.4.15
# https://leetcode.cn/problems/minimum-operations-to-reduce-x-to-zero/

"""
1658. 将 x 减到 0 的最小操作数 (Medium)
给你一个整数数组 `nums` 和一个整数 `x` 。每一次操作时，你应当移除数组 `nums` 最左边或最右边的元素，
然后从 `x` 中减去该元素的值。请注意，需要 **修改** 数组以供接下来的操作使用。

如果可以将 `x` **恰好** 减到 `0` ，返回 **最小操作数**；否则，返回 `-1` 。

**示例 1：**

```
输入：nums = [1,1,4,2,3], x = 5
输出：2
解释：最佳解决方案是移除后两个元素，将 x 减到 0 。
```

**示例 2：**

```
输入：nums = [5,6,7,8,9], x = 4
输出：-1
```

**示例 3：**

```
输入：nums = [3,2,20,1,1,3], x = 10
输出：5
解释：最佳解决方案是移除后三个元素和前两个元素（总共 5 次操作），将 x 减到 0 。
```

**提示：**

- `1 <= nums.length <= 10⁵`
- `1 <= nums[i] <= 10⁴`
- `1 <= x <= 10⁹`

"""

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        sums = sum(nums) - x
        if sums < 0:
            return -1
        l = 0
        ans = -1
        temp = 0
        for r, num in enumerate(nums):
            temp += num
            while temp > sums:
                temp -= nums[l]
                l += 1
            if temp == sums:
                ans = max(ans, r - l + 1)
        return -1 if ans < 0 else len(nums) - ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    x: int = deserialize("int", read_line())
    ans = Solution().minOperations(nums, x)
    print("\noutput:", serialize(ans, "integer"))
