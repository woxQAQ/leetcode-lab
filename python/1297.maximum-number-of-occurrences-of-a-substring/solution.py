# Created by woxQAQ at 2025/08/27 21:48
# leetgo: 1.4.15
# https://leetcode.cn/problems/maximum-number-of-occurrences-of-a-substring/

"""
1297. 子串的最大出现次数 (Medium)
给你一个字符串 `s` ，请你返回满足以下条件且出现次数最大的 **任意** 子串的出现次数：

- 子串中不同字母的数目必须小于等于 `maxLetters` 。
- 子串的长度必须大于等于 `minSize` 且小于等于 `maxSize` 。

**示例 1：**

```
输入：s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
输出：2
解释：子串 "aab" 在原字符串中出现了 2 次。
它满足所有的要求：2 个不同的字母，长度为 3 （在 minSize 和 maxSize 范围内）。
```

**示例 2：**

```
输入：s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
输出：2
解释：子串 "aaa" 在原字符串中出现了 2 次，且它们有重叠部分。
```

**示例 3：**

```
输入：s = "aabcabcab", maxLetters = 2, minSize = 2, maxSize = 3
输出：3
```

**示例 4：**

```
输入：s = "abcde", maxLetters = 2, minSize = 3, maxSize = 3
输出：0
```

**提示：**

- `1 <= s.length <= 10^5`
- `1 <= maxLetters <= 26`
- `1 <= minSize <= maxSize <= min(26, s.length)`
- `s` 只包含小写英文字母。

"""

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        cnt = DefaultDict(int)
        cnt_subs = DefaultDict(int)
        for i, ch in enumerate(s):
            cnt[ch] += 1
            if i < minSize - 1:
                continue
            l = i - minSize + 1
            if len(cnt) <= maxLetters:
                cnt_subs[s[l : i + 1]] += 1
            out = s[l]
            cnt[out] -= 1
            if cnt[out] == 0:
                del cnt[out]
        return max(cnt_subs.values(), default=0)


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    maxLetters: int = deserialize("int", read_line())
    minSize: int = deserialize("int", read_line())
    maxSize: int = deserialize("int", read_line())
    ans = Solution().maxFreq(s, maxLetters, minSize, maxSize)
    print("\noutput:", serialize(ans, "integer"))
