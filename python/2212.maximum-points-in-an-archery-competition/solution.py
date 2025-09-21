# Created by woxQAQ at 2025/09/21 00:21
# leetgo: 1.4.15
# https://leetcode.cn/problems/maximum-points-in-an-archery-competition/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maximumBobPoints(
        self, numArrows: int, aliceArrows: List[int]
    ) -> List[int]:
        res = 0
        path = [0] * len(aliceArrows)
        ans = []

        def dfs(i, score, arrows):
            nonlocal res, ans
            if i == len(aliceArrows):
                if res < score:
                    res = score
                    ans = path.copy()
                    if arrows != 0:
                        ans[0] += arrows
                return
            # if arrows == 0:
            # res = max(res, score)
            # if res < score:
            #     res = score
            #     ans = path.copy()
            #     if arrows != 0:
            #         ans[0] += arrows
            if arrows > aliceArrows[i]:
                # 选 i
                path[i] = aliceArrows[i] + 1
                dfs(i + 1, score + i, arrows - aliceArrows[i] - 1)
                path[i] = 0
            # 不选 i
            dfs(i + 1, score, arrows)

        dfs(0, 0, numArrows)
        print(res)
        return ans


# @lc code=end

if __name__ == "__main__":
    numArrows: int = deserialize("int", read_line())
    aliceArrows: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maximumBobPoints(numArrows, aliceArrows)
    print("\noutput:", serialize(ans, "integer[]"))
