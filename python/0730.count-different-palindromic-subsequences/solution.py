# Created by woxQAQ at 2025/08/24 22:36
# leetgo: 1.4.15
# https://leetcode.cn/problems/count-different-palindromic-subsequences/

from functools import cache
from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        MOD=10**9+7
        """
        1. s[i] == s[j]
            例: acbca
            1. 对于 s[i] 不在 s[i+1,j-1]
            s[1,3] 中的回文子序列为: cbc,c,b,cc
            s[1,3] 两边加上字符 a增加的回文子序列可以看做
            s[1,3]的所有的回文子序列两边加上字符a:acbca, aca, aba, acca
            以及增加 a 所产生的a 和 aa
            2. s[i+1,j-1] 中有一个字符等于 s[i]
            那么 单字符 a 就不能算为新增的答案
            3. s[i+1,j-1] 中有两个以上字符等于 s[i]
            如 abacbcaba，那么在加上两边a的同时，还需要减掉中间部分 acbca 的答案
            需要找到在 s[i+1,j-1] 中s[i]下标最小和下标最大的索引

            记 l,r 为 s[i] 在 s[i+1,j-1] 的最大索引，那么
            l > r 说明 s[i] 不在 s[i+1,j-1] 中
            l == r 说明在 s[i+1,j-1] 中有一个 s[i]

            计 count(s,c,max) 为 s中c的个数，超过max时返回max
            r = count(s[i+1,j-1], a, 2)
            dp[i][j] = dp[i+1][j-1] + (2-r)
        2. s[i] != s[j]
            那么 s[i+1,j-1] 所有的子序列与 s[i] s[j] 组合都无法构成回文串
            需要递归重新计算
            dp[i][j] = dp[i+1][j] + dp[i][j-1] + dp[i+1][j-1]
        """
        n = len(s)
        @cache
        def count(i,j,c):
            while i <= j and s[i] != c: i+=1
            while i <= j and s[j] != c: j-=1
            return i,j
        @cache
        def dfs(i,j):
            # print("dfs",i,j)
            if i > j:
                return 0
            if i == j:
                return 1
            if s[i] == s[j]:
                l,r = count(i+1,j-1,s[i])
                if l > r:
                    return dfs(i+1,j-1)*2+2
                elif l==r:
                    return dfs(i+1,j-1)*2+1
                else:
                    return dfs(i+1,j-1)*2-dfs(l+1,r-1)
            else:
                return dfs(i+1,j) + dfs(i,j-1) - dfs(i+1,j-1)
        return dfs(0,n-1) % MOD



# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().countPalindromicSubsequences(s)
    print("\noutput:", serialize(ans, "integer"))
