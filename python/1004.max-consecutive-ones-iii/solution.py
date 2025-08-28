# Created by woxQAQ at 2025/08/29 01:04
# leetgo: 1.4.15
# https://leetcode.cn/problems/max-consecutive-ones-iii/

"""
1004. 最大连续1的个数 III (Medium)
给定一个二进制数组 `nums` 和一个整数 `k`，假设最多可以翻转 `k` 个 `0` ，则返回执行操作后 数组中连续
`1` 的最大个数 。

**示例 1：**

```
输入：nums = [1,1,1,0,0,0,1,1,1,1,0], K = 2
输出：6
解释：[1,1,1,0,0,1,1,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 6。
```

**示例 2：**

```
输入：nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
输出：10
解释：[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 10。
```

**提示：**

- `1 <= nums.length <= 10⁵`
- `nums[i]` 不是 `0` 就是 `1`
- `0 <= k <= nums.length`

"""

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        cnt = 0
        ans = l = 0
        for r, x in enumerate(nums):
            if x == 0:
                cnt += 1
            while cnt > k:
                if nums[l] == 0:
                    cnt -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().longestOnes(nums, k)
    print("\noutput:", serialize(ans, "integer"))
