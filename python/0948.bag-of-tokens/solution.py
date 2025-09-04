# Created by woxQAQ at 2025/09/03 14:40
# leetgo: 1.4.13
# https://leetcode.cn/problems/bag-of-tokens/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score = 0
        l, r = 0, len(tokens) - 1
        ans = 0
        while l <= r:
            if power >= tokens[l]:
                power -= tokens[l]
                score += 1
                ans = max(ans, score)
                l += 1
            else:
                if score == 0:
                    break
                ans = max(ans, score)
                power += tokens[r]
                score -= 1
                r -= 1
        return ans


# @lc code=end

if __name__ == "__main__":
    tokens: List[int] = deserialize("List[int]", read_line())
    power: int = deserialize("int", read_line())
    ans = Solution().bagOfTokensScore(tokens, power)
    print("\noutput:", serialize(ans, "integer"))
