# Created by woxQAQ at 2025/09/01 17:00
# leetgo: 1.4.13
# https://leetcode.cn/problems/minimized-maximum-of-products-distributed-to-any-store/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    quantities: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minimizedMaximum(n, quantities)
    print("\noutput:", serialize(ans, "integer"))
