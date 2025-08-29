# Created by woxQAQ at 2025/08/29 17:52
# leetgo: 1.4.15
# https://leetcode.cn/problems/1GxJYY/

from collections import defaultdict
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def beautifulBouquet(self, flowers: List[int], cnt: int) -> int:
        cnt_f = defaultdict(int)
        ans = l = 0
        for r, x in enumerate(flowers):
            cnt_f[x] += 1
            while cnt_f[x] > cnt:
                cnt_f[flowers[l]] -= 1
                l += 1
            ans += r - l + 1
        return ans % (10**9 + 7)


# @lc code=end

if __name__ == "__main__":
    flowers: List[int] = deserialize("List[int]", read_line())
    cnt: int = deserialize("int", read_line())
    ans = Solution().beautifulBouquet(flowers, cnt)
    print("\noutput:", serialize(ans, "integer"))
