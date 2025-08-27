# Created by woxQAQ at 2025/08/27 16:45
# leetgo: 1.4.15
# https://leetcode.cn/problems/maximum-average-subarray-i/

"""
643. 子数组最大平均数 I (Easy)
给你一个由 `n` 个元素组成的整数数组 `nums` 和一个整数 `k` 。

请你找出平均数最大且 **长度为 `k`** 的连续子数组，并输出该最大平均数。

任何误差小于 `10⁻⁵` 的答案都将被视为正确答案。

**示例 1：**

```
输入：nums = [1,12,-5,-6,50,3], k = 4
输出：12.75
解释：最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
```

**示例 2：**

```
输入：nums = [5], k = 1
输出：5.00000
```

**提示：**

- `n == nums.length`
- `1 <= k <= n <= 10⁵`
- `-10⁴ <= nums[i] <= 10⁴`

"""

from math import inf
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = -inf
        s = 0
        for i, num in enumerate(nums):
            s += num
            if i < k - 1:
                continue
            ans = max(ans, s)
            s -= nums[i - k + 1]
        return ans / k


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().findMaxAverage(nums, k)
    print("\noutput:", serialize(ans, "double"))
