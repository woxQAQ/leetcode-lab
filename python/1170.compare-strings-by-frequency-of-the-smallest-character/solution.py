# Created by woxQAQ at 2025/08/30 04:48
# leetgo: 1.4.13
# https://leetcode.cn/problems/compare-strings-by-frequency-of-the-smallest-character/

from bisect import bisect_left
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s: str) -> int:
            max_ch = "z"
            count = 0
            for ch in s:
                if ch < max_ch:
                    max_ch = ch
                    count = 0
                if ch == max_ch:
                    count += 1
            return count

        wordsF = sorted([f(word) for word in words])
        return [len(words) - bisect_left(wordsF, f(q) + 1) for q in queries]


# @lc code=end

if __name__ == "__main__":
    queries: List[str] = deserialize("List[str]", read_line())
    words: List[str] = deserialize("List[str]", read_line())
    ans = Solution().numSmallerByFrequency(queries, words)
    print("\noutput:", serialize(ans, "integer[]"))
