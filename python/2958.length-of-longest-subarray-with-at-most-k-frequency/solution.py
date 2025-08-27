# Created by woxQAQ at 2025/08/28 03:38
# leetgo: 1.4.15
# https://leetcode.cn/problems/length-of-longest-subarray-with-at-most-k-frequency/

"""
2958. 最多 K 个重复元素的最长子数组 (Medium)
给你一个整数数组 `nums` 和一个整数 `k` 。

一个元素 `x` 在数组中的 **频率** 指的是它在数组中的出现次数。

如果一个数组中所有元素的频率都 **小于等于** `k` ，那么我们称这个数组是 **好** 数组。

请你返回 `nums` 中 **最长好** 子数组的长度。

**子数组** 指的是一个数组中一段连续非空的元素序列。

**示例 1：**

```
输入：nums = [1,2,3,1,2,3,1,2], k = 2
输出：6
解释：最长好子数组是 [1,2,3,1,2,3] ，值 1 ，2 和 3 在子数组中的频率都没有超过 k = 2 。[2,3,1,2,3,1]
和 [3,1,2,3,1,2] 也是好子数组。
最长好子数组的长度为 6 。
```

**示例 2：**

```
输入：nums = [1,2,1,2,1,2,1,2], k = 1
输出：2
解释：最长好子数组是 [1,2] ，值 1 和 2 在子数组中的频率都没有超过 k = 1 。[2,1] 也是好子数组。
最长好子数组的长度为 2 。
```

**示例 3：**

```
输入：nums = [5,5,5,5,5,5,5], k = 4
输出：4
解释：最长好子数组是 [5,5,5,5] ，值 5 在子数组中的频率没有超过 k = 4 。
最长好子数组的长度为 4 。
```

**提示：**

- `1 <= nums.length <= 10⁵`
- `1 <= nums[i] <= 10⁹`
- `1 <= k <= nums.length`

"""

from collections import defaultdict
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = l = 0
        cnt = defaultdict(int)
        for r, num in enumerate(nums):
            cnt[num] += 1
            while cnt[num] > k:
                cnt[nums[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maxSubarrayLength(nums, k)
    print("\noutput:", serialize(ans, "integer"))
