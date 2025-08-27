# Created by woxQAQ at 2025/08/27 16:56
# leetgo: 1.4.15
# https://leetcode.cn/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/

"""
1343. 大小为 K 且平均值大于等于阈值的子数组数目 (Medium)
给你一个整数数组 `arr` 和两个整数 `k` 和 `threshold` 。

请你返回长度为 `k` 且平均值大于等于 `threshold` 的子数组数目。

**示例 1：**

```
输入：arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
输出：3
解释：子数组 [2,5,5],[5,5,5] 和 [5,5,8] 的平均值分别为 4，5 和 6 。其他长度为 3 的子数组的平均值都小
于 4 （threshold 的值)。
```

**示例 2：**

```
输入：arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
输出：6
解释：前 6 个长度为 3 的子数组平均值都大于 5 。注意平均值不是整数。
```

**提示：**

- `1 <= arr.length <= 10⁵`
- `1 <= arr[i] <= 10⁴`
- `1 <= k <= arr.length`
- `0 <= threshold <= 10⁴`

"""

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = s = 0
        for i, num in enumerate(arr):
            s += num
            if i < k - 1:
                continue
            if s / k >= threshold:
                count += 1
            s -= arr[i - k + 1]
        return count


# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    threshold: int = deserialize("int", read_line())
    ans = Solution().numOfSubarrays(arr, k, threshold)
    print("\noutput:", serialize(ans, "integer"))
