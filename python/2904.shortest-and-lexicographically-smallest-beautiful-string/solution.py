# Created by woxQAQ at 2025/08/29 01:59
# leetgo: 1.4.15
# https://leetcode.cn/problems/shortest-and-lexicographically-smallest-beautiful-string/

"""
2904. 最短且字典序最小的美丽子字符串 (Medium)
给你一个二进制字符串 `s` 和一个正整数 `k` 。

如果 `s` 的某个子字符串中 `1` 的个数恰好等于 `k` ，则称这个子字符串是一个 **美丽子字符串** 。

令 `len` 等于 **最短** 美丽子字符串的长度。

返回长度等于 `len` 且字典序 **最小** 的美丽子字符串。如果 `s` 中不含美丽子字符串，则返回一个 **空**
字符串。

对于相同长度的两个字符串 `a` 和 `b` ，如果在 `a` 和 `b` 出现不同的第一个位置上， `a` 中该位置上的字
符严格大于 `b` 中的对应字符，则认为字符串 `a` 字典序 **大于** 字符串 `b` 。

- 例如， `"abcd"` 的字典序大于 `"abcc"` ，因为两个字符串出现不同的第一个位置对应第四个字符，而 `d`
大于 `c` 。

**示例 1：**

```
输入：s = "100011001", k = 3
输出："11001"
解释：示例中共有 7 个美丽子字符串：
1. 子字符串 "100011001" 。
2. 子字符串 "100011001" 。
3. 子字符串 "100011001" 。
4. 子字符串 "100011001" 。
5. 子字符串 "100011001" 。
6. 子字符串 "100011001" 。
7. 子字符串 "100011001" 。
最短美丽子字符串的长度是 5 。
长度为 5 且字典序最小的美丽子字符串是子字符串 "11001" 。
```

**示例 2：**

```
输入：s = "1011", k = 2
输出："11"
解释：示例中共有 3 个美丽子字符串：
1. 子字符串 "1011" 。
2. 子字符串 "1011" 。
3. 子字符串 "1011" 。
最短美丽子字符串的长度是 2 。
长度为 2 且字典序最小的美丽子字符串是子字符串 "11" 。
```

**示例 3：**

```
输入：s = "000", k = 1
输出：""
解释：示例中不存在美丽子字符串。
```

**提示：**

- `1 <= s.length <= 100`
- `1 <= k <= s.length`

"""

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        if s.count("1") < k:
            return ""
        ans = s
        cnt1 = l = 0
        for r, ch in enumerate(s):
            cnt1 += int(ch)
            while cnt1 > k or s[l] == "0":
                cnt1 -= int(s[l])
                l += 1
            if cnt1 == k:
                t = s[l : r + 1]
                if len(t) < len(ans) or len(t) == len(ans) and t < ans:
                    ans = t

        return ans


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().shortestBeautifulSubstring(s, k)
    print("\noutput:", serialize(ans, "string"))
