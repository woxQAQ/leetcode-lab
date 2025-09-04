# Created by woxQAQ at 2025/09/04 08:45
# leetgo: 1.4.13
# https://leetcode.cn/problems/minimum-number-of-moves-to-seat-everyone/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        # 1,3,5
        # 2,4,7
        #
        # 排序后一一配对得到最小值。
        # 反证法：对于 i<j
        # 设 x = students[i], y = students[j]
        # u = seats[i] v= seats[j]
        # 要证明
        # |x-u| + |y-v| <= |x-v| + |y-u|
        # ==> |x-u| - |x-v| <= |y-u| - |y-v|
        # 不妨令 u <= v,不失一般性
        #
        # 令 g(x) = |x-u| - |x-v|
        # g(x) =
        # (u-x)-(v-x) = u-v,x < u <= v
        # x-u-(v-x)=2x+v-u, u<= x < v
        # (x-u)-(x-v) = v-u, x>v
        #
        # g'(x) = 0 x<u; 2 u<=x<v; 0 x>v
        #
        # 可以看到 g 在 (-∞,+∞) 上为非减函数，那么
        #
        # g(x) <= g(y) 恒成立。因此下式成立
        # |x-u| + |y-v| <= |x-v| + |y-u|
        #
        # 所以得出结论，排序后一一配对能得到最小值
        seats.sort()
        students.sort()
        return sum(abs(seat - student) for seat, student in zip(seats, students))


# @lc code=end

if __name__ == "__main__":
    seats: List[int] = deserialize("List[int]", read_line())
    students: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minMovesToSeat(seats, students)
    print("\noutput:", serialize(ans, "integer"))
