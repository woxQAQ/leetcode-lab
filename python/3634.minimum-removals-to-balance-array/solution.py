# Created by woxQAQ at 2025/08/28 02:55
# leetgo: 1.4.15
# https://leetcode.cn/problems/minimum-removals-to-balance-array/

"""
3634. 使数组平衡的最少移除数目 (Medium)
给你一个整数数组 `nums` 和一个整数 `k`。

如果一个数组的 **最大** 元素的值 **至多** 是其 **最小** 元素的 `k` 倍，则该数组被称为是 **平衡** 的
。

你可以从 `nums` 中移除 **任意** 数量的元素，但不能使其变为 **空** 数组。

返回为了使剩余数组平衡，需要移除的元素的 **最小** 数量。

**注意：** 大小为 1 的数组被认为是平衡的，因为其最大值和最小值相等，且条件总是成立。

**示例 1:**

**输入：** nums = \[2,1,5\], k = 2

**输出：** 1

**解释：**

- 移除 `nums[2] = 5` 得到 `nums = [2, 1]`。
- 现在 `max = 2`, `min = 1`，且 `max <= min * k`，因为 `2 <= 1 * 2`。因此，答案是 1。

**示例 2:**

**输入：** nums = \[1,6,2,9\], k = 3

**输出：** 2

**解释：**

- 移除 `nums[0] = 1` 和 `nums[3] = 9` 得到 `nums = [6, 2]`。
- 现在 `max = 6`, `min = 2`，且 `max <= min * k`，因为 `6 <= 2 * 3`。因此，答案是 2。

**示例 3:**

**输入：** nums = \[4,6\], k = 2

**输出：** 0

**解释：**

- 由于 `nums` 已经平衡，因为 `6 <= 4 * 2`，所以不需要移除任何元素。

**提示：**

- `1 <= nums.length <= 10⁵`
- `1 <= nums[i] <= 10⁹`
- `1 <= k <= 10⁵`

"""

from typing import *
from leetgo_py import *
from math import inf

# @lc code=begin


class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()

        l = ans = 0
        for r, num in enumerate(nums):
            while k * nums[l] < num:
                l += 1
            ans = max(ans, r - l + 1)
        return len(nums) - ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().minRemoval(nums, k)
    print("\noutput:", serialize(ans, "integer"))
