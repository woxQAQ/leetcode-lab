# Created by woxQAQ at 2025/08/27 22:56
# leetgo: 1.4.15
# https://leetcode.cn/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/

"""
1888. 使二进制字符串字符交替的最少反转次数 (Medium)
给你一个二进制字符串 `s` 。你可以按任意顺序执行以下两种操作任意次：

- **类型 1 ：删除** 字符串 `s` 的第一个字符并将它 **添加** 到字符串结尾。
- **类型 2 ：选择** 字符串 `s` 中任意一个字符并将该字符 **反转**，也就是如果值为 `'0'` ，则反转得到
`'1'` ，反之亦然。

请你返回使 `s` 变成 **交替** 字符串的前提下， **类型 2** 的 **最少** 操作次数 。

我们称一个字符串是 **交替** 的，需要满足任意相邻字符都不同。

- 比方说，字符串 `"010"` 和 `"1010"` 都是交替的，但是字符串 `"0100"` 不是。

**示例 1：**

```
输入：s = "111000"
输出：2
解释：执行第一种操作两次，得到 s = "100011" 。
然后对第三个和第六个字符执行第二种操作，得到 s = "101010" 。
```

**示例 2：**

```
输入：s = "010"
输出：0
解释：字符串已经是交替的。
```

**示例 3：**

```
输入：s = "1110"
输出：1
解释：对第二个字符执行第二种操作，得到 s = "1010" 。
```

**提示：**

- `1 <= s.length <= 10⁵`
- `s[i]` 要么是 `'0'` ，要么是 `'1'` 。

"""

import enum
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minFlips(self, s: str) -> int:
        """
        s = 111000
        s不断进行 操作1 s' = 011100
        再进行一次 操作1就变成 111000 == s
        这个过程所产生的所有字符串 s' 都是
        t= 111000111000(s+s) 的子串。
        本题的最优解必然是在经过m次操作1后得到的最少操作2数，即
        在 t 的长度为 len(s) 的子串中找到最少的翻转次数
        t = 11100[011100]0
        子串的形式必然为 0xxxxx 或 1xxxxx，记操作数为c
        0xxxxx => 010101
            i 为奇数，sub_target[i] = 0==(i-1) mod 2 ==> c += 1 if sub[i] = 1
            i 为偶数，sub_target[i] = 1==(i-1) mod 2 ==> c += 1 if sub[i] = 0
            ==> c += 1 if sub[i] == i mod 2
        1xxxxx => 101010
        同理可得 c += 1 if sub[i] != i mod 2
        记第一种情况的操作数为 c0,第二种情况为c1,可以得知 c0 + c1 = len(s)
        那么结果为c0和c1取最小，即 min(c0,n-c0)
        """
        ct = 0
        ans = n = len(s)
        for i in range(2 * n - 1):
            if ord(s[i % n]) % 2 != i % 2:
                ct += 1
            if i < n - 1:
                continue
            ans = min(ans, ct, n - ct)
            if ord(s[i - n + 1]) % 2 != (i - n + 1) % 2:
                ct -= 1
        return ans


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().minFlips(s)
    print("\noutput:", serialize(ans, "integer"))
