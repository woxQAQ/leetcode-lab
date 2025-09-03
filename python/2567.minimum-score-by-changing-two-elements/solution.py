# Created by woxQAQ at 2025/09/03 08:58
# leetgo: 1.4.13
# https://leetcode.cn/problems/minimum-score-by-changing-two-elements/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        # [1,3,5,7,8]
        # 设 d1 为最大的情况
        # d2 最小的情况，
        # 对于 d2, 只要nums 存在相同值，那么d2=0取到最小值
        #
        # 保证d2最小的情况下，
        # 至多两次操作只允许三种情况发生
        # 1. nums[-1],nums[-2] 改为 nums[-3]
        #   d1 = nums[-3] - nums[0]
        #   d2=0
        # 2. nums[0],nums[1] 改为 nums[2]
        #   d1 = nums[-1] - nums[2]
        #   d2 = 0
        # 3. nums[0],nums[1] 改为 nums[1]
        #   d1 = nums[-1] - nums[1]
        #   d2 = 0
        #
        # 不合法的情况：
        # nums[0],nums[1] 为什么不能改为 nums[3]?
        #
        # nums[0],nums[1] 改为 nums[3]， nums[2] 成为最小值，答案变为
        # d1=nums[-1]-nums[2]，与 改为 nums[2] 等价。往后的下标也同理
        #
        # nums[-1],num[-2] 能不能改为 nums[-2],num[-4]
        # 改为 nums[-4] 的情况和 nums[0],nums[1] 改为 nums[3] 的结果类似
        # 改为 nums[-2], d1 无法取到最小值，
        # 因为必然有 nums[-3] < nums[-2] = nums[-1]
        # nums[-3] - nums[0] 才能得到最小值
        return min(nums[-1] - nums[2], nums[-2] - nums[1], nums[-3] - nums[0])


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minimizeSum(nums)
    print("\noutput:", serialize(ans, "integer"))
