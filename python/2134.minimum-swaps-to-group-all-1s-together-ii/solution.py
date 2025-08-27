# Created by woxQAQ at 2025/08/27 21:34
# leetgo: 1.4.15
# https://leetcode.cn/problems/minimum-swaps-to-group-all-1s-together-ii/

"""
2134. 最少交换次数来组合所有的 1 II (Medium)
**交换** 定义为选中一个数组中的两个 **互不相同** 的位置并交换二者的值。

**环形** 数组是一个数组，可以认为 **第一个** 元素和 **最后一个** 元素 **相邻** 。

给你一个 **二进制环形** 数组 `nums` ，返回在 **任意位置** 将数组中的所有 `1` 聚集在一起需要的最少交
换次数。

**示例 1：**

```
输入：nums = [0,1,0,1,1,0,0]
输出：1
解释：这里列出一些能够将所有 1 聚集在一起的方案：
[0,0,1,1,1,0,0] 交换 1 次。
[0,1,1,1,0,0,0] 交换 1 次。
[1,1,0,0,0,0,1] 交换 2 次（利用数组的环形特性）。
无法在交换 0 次的情况下将数组中的所有 1 聚集在一起。
因此，需要的最少交换次数为 1 。
```

**示例 2：**

```
输入：nums = [0,1,1,1,0,0,1,1,0]
输出：2
解释：这里列出一些能够将所有 1 聚集在一起的方案：
[1,1,1,0,0,0,0,1,1] 交换 2 次（利用数组的环形特性）。
[1,1,1,1,1,0,0,0,0] 交换 2 次。
无法在交换 0 次或 1 次的情况下将数组中的所有 1 聚集在一起。
因此，需要的最少交换次数为 2 。
```

**示例 3：**

```
输入：nums = [1,1,0,0,1]
输出：0
解释：得益于数组的环形特性，所有的 1 已经聚集在一起。
因此，需要的最少交换次数为 0 。
```

**提示：**

- `1 <= nums.length <= 10⁵`
- `nums[i]` 为 `0` 或者 `1`

"""

from math import inf
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        k = sum(nums)
        if k == 0:
            return 0
        s = 0
        n = len(nums)
        ans = -inf
        for i in range(n + k - 1):
            s += nums[i % n]
            if i < k - 1:
                continue
            ans = max(ans, s)
            s -= nums[i - k + 1]
        return k - ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minSwaps(nums)
    print("\noutput:", serialize(ans, "integer"))
