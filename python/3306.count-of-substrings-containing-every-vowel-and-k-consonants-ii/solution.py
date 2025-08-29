# Created by woxQAQ at 2025/08/29 19:36
# leetgo: 1.4.15
# https://leetcode.cn/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/

from collections import defaultdict
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def f(k):
            cnt_v = defaultdict(int)
            cnt_c = 0
            ans = l = 0
            for r, x in enumerate(word):
                if x in "aeiou":
                    cnt_v[x] += 1
                else:
                    cnt_c += 1
                while len(cnt_v) == 5 and cnt_c >= k:
                    if word[l] in "aeiou":
                        cnt_v[word[l]] -= 1
                        if cnt_v[word[l]] == 0:
                            del cnt_v[word[l]]
                    else:
                        cnt_c -= 1
                    l += 1
                ans += l
            return ans

        return f(k) - f(k + 1)


# @lc code=end

if __name__ == "__main__":
    word: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().countOfSubstrings(word, k)
    print("\noutput:", serialize(ans, "long"))
