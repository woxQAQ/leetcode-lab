# Created by woxQAQ at 2025/08/28 02:15
# leetgo: 1.4.15
# https://leetcode.cn/problems/maximum-length-substring-with-two-occurrences/

"""
3090. 每个字符最多出现两次的最长子字符串 (Easy)
给你一个字符串 `s` ，请找出满足每个字符最多出现两次的最长子字符串，并返回该子字符串的 **最大** 长度
。

**示例 1：**

**输入：** s = "bcbbbcba"

**输出：** 4

**解释：**

以下子字符串长度为 4，并且每个字符最多出现两次： `"bcbbbcba"`。

**示例 2：**

**输入：** s = "aaaa"

**输出：** 2

**解释：**

以下子字符串长度为 2，并且每个字符最多出现两次： `"aaaa"`。

**提示：**

- `2 <= s.length <= 100`
- `s` 仅由小写英文字母组成。

"""

from collections import defaultdict
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        cnt = defaultdict(int)
        l = ans = 0
        for r, ch in enumerate(s):
            cnt[ch] += 1
            while cnt[ch] > 2:
                cnt[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().maximumLengthSubstring(s)
    print("\noutput:", serialize(ans, "integer"))
