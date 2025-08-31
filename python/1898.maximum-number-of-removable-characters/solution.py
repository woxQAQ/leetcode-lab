# Created by woxQAQ at 2025/08/31 18:40
# leetgo: 1.4.13
# https://leetcode.cn/problems/maximum-number-of-removable-characters/

from copyreg import remove_extension
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        # "abcacb" "ab"
        l = 0
        r = len(removable) + 1

        def check(k):
            remove = set(removable[:k])
            it = (s[i] for i in range(len(s)) if i not in remove)
            return all(c in it for c in p)

        while l < r - 1:
            k = (l + r) // 2
            if check(k):
                l = k
            else:
                r = k
        return l


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    p: str = deserialize("str", read_line())
    removable: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maximumRemovals(s, p, removable)
    print("\noutput:", serialize(ans, "integer"))
