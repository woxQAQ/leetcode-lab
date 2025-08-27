# Created by woxQAQ at 2025/08/27 23:37
# leetgo: 1.4.15
# https://leetcode.cn/problems/permutation-in-string/

"""
567. 字符串的排列 (Medium)
给你两个字符串 `s1` 和 `s2` ，写一个函数来判断 `s2` 是否包含 `s1` 的 排列。如果是，返回 `true` ；否
则，返回 `false` 。

换句话说， `s1` 的排列之一是 `s2` 的 **子串** 。

**示例 1：**

```
输入：s1 = "ab" s2 = "eidbaooo"
输出：true
解释：s2 包含 s1 的排列之一 ("ba").
```

**示例 2：**

```
输入：s1= "ab" s2 = "eidboaoo"
输出：false
```

**提示：**

- `1 <= s1.length, s2.length <= 10⁴`
- `s1` 和 `s2` 仅包含小写字母

"""

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # cnt = Counter()
        cnt_s = Counter(s1)

        for i, ch in enumerate(s2):
            cnt_s[ch] -= 1
            if cnt_s[ch] == 0:
                del cnt_s[ch]
            if i < len(s1) - 1:
                continue
            if len(cnt_s) == 0:
                return True
            out = s2[i - len(s1) + 1]
            cnt_s[out] += 1
            if cnt_s[out] == 0:
                del cnt_s[out]

        return False


# @lc code=end

if __name__ == "__main__":
    s1: str = deserialize("str", read_line())
    s2: str = deserialize("str", read_line())
    ans = Solution().checkInclusion(s1, s2)
    print("\noutput:", serialize(ans, "boolean"))
