# Created by woxQAQ at 2025/08/28 03:32
# leetgo: 1.4.15
# https://leetcode.cn/problems/maximum-erasure-value/

"""
1695. 删除子数组的最大得分 (Medium)
给你一个正整数数组 `nums` ，请你从中删除一个含有 **若干不同元素** 的子数组 **。** 删除子数组的 **得
分** 就是子数组各元素之 **和** 。

返回 **只删除一个** 子数组可获得的 **最大得分** 。

如果数组 `b` 是数组 `a` 的一个连续子序列，即如果它等于 `a[l],a[l+1],...,a[r]` ，那么它就是 `a` 的一
个子数组。

**示例 1：**

```
输入：nums = [4,2,4,5,6]
输出：17
解释：最优子数组是 [2,4,5,6]
```

**示例 2：**

```
输入：nums = [5,2,1,2,5,2,1,2,5]
输出：8
解释：最优子数组是 [5,2,1] 或 [1,2,5]
```

**提示：**

- `1 <= nums.length <= 10⁵`
- `1 <= nums[i] <= 10⁴`

"""

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        cnt = DefaultDict(int)
        l = ans = 0
        for r, num in enumerate(nums):
            cnt[num] += 1
            while cnt[num] > 1:
                cnt[nums[l]] -= 1
                l += 1
            ans = max(ans, sum(nums[l : r + 1]))
        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maximumUniqueSubarray(nums)
    print("\noutput:", serialize(ans, "integer"))
