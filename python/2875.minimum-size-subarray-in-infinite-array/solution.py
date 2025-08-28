# Created by woxQAQ at 2025/08/29 02:24
# leetgo: 1.4.15
# https://leetcode.cn/problems/minimum-size-subarray-in-infinite-array/

"""
2875. 无限数组的最短子数组 (Medium)
给你一个下标从 **0** 开始的数组 `nums` 和一个整数 `target` 。

下标从 **0** 开始的数组 `infinite_nums` 是通过无限地将 nums 的元素追加到自己之后生成的。

请你从 `infinite_nums` 中找出满足 **元素和** 等于 `target` 的 **最短** 子数组，并返回该子数组的长度
。如果不存在满足条件的子数组，返回 `-1` 。

**示例 1：**

```
输入：nums = [1,2,3], target = 5
输出：2
解释：在这个例子中 infinite_nums = [1,2,3,1,2,3,1,2,...] 。
区间 [1,2] 内的子数组的元素和等于 target = 5 ，且长度 length = 2 。
可以证明，当元素和等于目标值 target = 5 时，2 是子数组的最短长度。
```

**示例 2：**

```
输入：nums = [1,1,1,2,3], target = 4
输出：2
解释：在这个例子中 infinite_nums = [1,1,1,2,3,1,1,1,2,3,1,1,...].
区间 [4,5] 内的子数组的元素和等于 target = 4 ，且长度 length = 2 。
可以证明，当元素和等于目标值 target = 4 时，2 是子数组的最短长度。
```

**示例 3：**

```
输入：nums = [2,4,6,8], target = 3
输出：-1
解释：在这个例子中 infinite_nums = [2,4,6,8,2,4,6,8,...] 。
可以证明，不存在元素和等于目标值 target = 3 的子数组。
```

**提示：**

- `1 <= nums.length <= 10⁵`
- `1 <= nums[i] <= 10⁵`
- `1 <= target <= 10⁹`

"""

from math import inf
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        # [1,2,3]
        # infty_nums: [1,2,3,1,2,3,1,2,3...]
        # 令 sum = sum(nums)
        # 分类讨论
        # 1. target < sum
        # 在 [1,2,3,1,2,3] 内寻找和为 target 的子数组，找不到说明不存在
        #
        # 2. target > sum
        # 如果有解，则其解一定包含若干个完整的 [1,2,3].
        # 如 target = 10: [1,2,|3],[1,2,3],[1|,2,3]
        # 去掉 中间若干个完整的 [1,2,3]，可以得到 [1,2,|3] [1|,2,3]
        # 问题转为在 [1,2,3,1,2,3] 中寻找和为 target % sum = 4 的子数组，这样，两种情况合并了
        # 问题为，在 [1,2,3,1,2,3] 中寻找和为 target % sum 的最短子数组，其长度为 ans，
        # 最终答案加上中间去掉的若干个 [1,2,3]，即 ans + (target // sum) * len(sum)
        s = sum(nums)
        rem = target % s
        l, ans = 0, inf
        temp = 0
        n = len(nums)
        for r in range(2 * n):
            temp += nums[r % n]
            while temp > rem:
                temp -= nums[l % n]
                l += 1
            if temp == rem:
                ans = min(ans, r - l + 1)
        return ans + target // s * n if ans != inf else -1


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().minSizeSubarray(nums, target)
    print("\noutput:", serialize(ans, "integer"))
