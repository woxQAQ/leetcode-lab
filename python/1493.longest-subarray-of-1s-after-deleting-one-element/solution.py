# Created by woxQAQ at 2025/08/28 02:33
# leetgo: 1.4.15
# https://leetcode.cn/problems/longest-subarray-of-1s-after-deleting-one-element/

"""
1493. 删掉一个元素以后全为 1 的最长子数组 (Medium)
给你一个二进制数组 `nums` ，你需要从中删掉一个元素。

请你在删掉元素的结果数组中，返回最长的且只包含 1 的非空子数组的长度。

如果不存在这样的子数组，请返回 0 。

**提示 1：**

```
输入：nums = [1,1,0,1]
输出：3
解释：删掉位置 2 的数后，[1,1,1] 包含 3 个 1 。
```

**示例 2：**

```
输入：nums = [0,1,1,1,0,1,1,0,1]
输出：5
解释：删掉位置 4 的数字后，[0,1,1,1,1,1,0,1] 的最长全 1 子数组为 [1,1,1,1,1] 。
```

**示例 3：**

```
输入：nums = [1,1,1]
输出：2
解释：你必须要删除一个元素。
```

**提示：**

- `1 <= nums.length <= 10⁵`
- `nums[i]` 要么是 `0` 要么是 `1` 。

"""

from collections import defaultdict
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        c0 = 0
        last_zero = -1
        l = ans = 0
        for r, num in enumerate(nums):
            if num == 0:
                c0 += 1
                if c0 > 0:
                    l = last_zero + 1
                last_zero = r
            ans = max(ans, r - l)
        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().longestSubarray(nums)
    print("\noutput:", serialize(ans, "integer"))
