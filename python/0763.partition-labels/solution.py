# Created by woxQAQ at 2025/09/04 17:30
# leetgo: 1.4.15
# https://leetcode.cn/problems/partition-labels/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # 统计每个字符最远出现位置
        last = {c: i for i, c in enumerate(s)}
        l, r = 0, 0
        ans = []
        for i, c in enumerate(s):
            r = max(r, last[c])
            if i == r:
                ans.append(r - l + 1)
                l = r + 1
        return ans


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().partitionLabels(s)
    print("\noutput:", serialize(ans, "integer[]"))
