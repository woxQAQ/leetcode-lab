# Created by woxQAQ at 2026/03/12 01:26
# leetgo: 1.4.16
# https://leetcode.cn/problems/subarray-sum-equals-k/
from collections import defaultdict

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre = [0] * (len(nums)+1)
        for i, x in enumerate(nums):
            pre[i+1] = pre[i] + x
        # 暴力写法
        # ans = 0
        # for i,x in enumerate(pre):
        #     for y in pre[i+1:]:
        #         if y-x == k:
        #             ans += 1
        # return ans
        
        # 哈希表优化：y-x = k => x = y-k (xi < yi)
        # 枚举 y,检查y 『之前』有多少 x满足 x = y-k 
        cnt = defaultdict(int)
        ans = 0
        for y in pre:
            # 先统计后存哈希表，体现之前
            ans += cnt[y-k]
            cnt[y] +=1
        return ans
        
        # 一次遍历(不要求写到这)
        # pre = 0
        # cnt = defaultdict(int)
        # ans = 0
        # for x in nums:
        #     cnt[pre] += 1
        #     pre += x
        #     ans += cnt[pre-k]
        # return ans
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().subarraySum(nums, k)
    print("\noutput:", serialize(ans, "integer"))
