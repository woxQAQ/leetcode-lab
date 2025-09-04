# Created by woxQAQ at 2025/09/04 09:54
# leetgo: 1.4.13
# https://leetcode.cn/problems/maximum-matching-of-players-with-trainers/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        # 4,7,9
        # 2,5,8,8
        ans = 0
        for t in trainers:
            if t < players[ans]:
                continue
            ans += 1
            if ans == len(players):
                break
        return ans


# @lc code=end

if __name__ == "__main__":
    players: List[int] = deserialize("List[int]", read_line())
    trainers: List[int] = deserialize("List[int]", read_line())
    ans = Solution().matchPlayersAndTrainers(players, trainers)
    print("\noutput:", serialize(ans, "integer"))
