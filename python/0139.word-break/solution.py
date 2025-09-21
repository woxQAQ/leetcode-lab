# Created by woxQAQ at 2025/09/20 17:26
# leetgo: 1.4.15
# https://leetcode.cn/problems/word-break/

from functools import cache
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # @cache
        # def dfs(i):
        #     if i == len(s):
        #         return True
        #     for word in wordDict:
        #         if s[i:].startswith(word) and dfs(i + len(word)):
        #             return True
        #     return False

        # return dfs(0)
        words = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for word in words:
                if (
                    i >= len(word)
                    and dp[i - len(word)]
                    and s[i - len(word) : i] == word
                ):
                    dp[i] = True
                    break
        return dp[-1]


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    wordDict: List[str] = deserialize("List[str]", read_line())
    ans = Solution().wordBreak(s, wordDict)
    print("\noutput:", serialize(ans, "boolean"))
