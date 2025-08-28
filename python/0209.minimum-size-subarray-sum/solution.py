# Created by woxQAQ at 2025/08/29 01:45
# leetgo: 1.4.15
# https://leetcode.cn/problems/minimum-size-subarray-sum/

"""
209. 长度最小的子数组 (Medium)
给定一个含有 `n` 个正整数的数组和一个正整数 `target` **。**

找出该数组中满足其总和大于等于 `target` 的长度最小的 **子数组** `[numsₗ, numsₗ₊₁, ..., numsᵣ₋₁, nums
ᵣ]` ，并返回其长度 **。** 如果不存在符合条件的子数组，返回 `0` 。

**示例 1：**

```
输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
```

**示例 2：**

```
输入：target = 4, nums = [1,4,4]
输出：1
```

**示例 3：**

```
输入：target = 11, nums = [1,1,1,1,1,1,1,1]
输出：0
```

**提示：**

- `1 <= target <= 10⁹`
- `1 <= nums.length <= 10⁵`
- `1 <= nums[i] <= 10⁴`

**进阶：**

- 如果你已经实现 `O(n)` 时间复杂度的解法, 请尝试设计一个 `O(n log(n))` 时间复杂度的解法。

"""

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = s = l = 0
        for r, x in enumerate(nums):
            s += x
            while s >= target:
                ans = min(ans, r - l + 1) if ans else r - l + 1
                s -= nums[l]
                l += 1
        return ans


# @lc code=end

if __name__ == "__main__":
    target: int = deserialize("int", read_line())
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minSubArrayLen(target, nums)
    print("\noutput:", serialize(ans, "integer"))
