# [730. 统计不同回文子序列][link] (Hard)

[link]: https://leetcode.cn/problems/count-different-palindromic-subsequences/

给你一个字符串 `s` ，返回 `s` 中不同的非空回文子序列个数 。由于答案可能很大，请返回对 `10⁹ + 7` **取
余** 的结果。

字符串的子序列可以经由字符串删除 0 个或多个字符获得。

如果一个序列与它反转后的序列一致，那么它是回文序列。

如果存在某个 `i` , 满足 `aᵢ != bᵢ`，则两个序列 `a₁, a₂, ...` 和 `b₁, b₂, ...` 不同。

**示例 1：**

```
输入：s = 'bccb'
输出：6
解释：6 个不同的非空回文子字符序列分别为：'b', 'c', 'bb', 'cc', 'bcb', 'bccb'。
注意：'bcb' 虽然出现两次但仅计数一次。
```

**示例 2：**

```
输入：s = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'
输出：104860361
解释：共有 3104860382 个不同的非空回文子序列，104860361 是对 10⁹ + 7 取余后的值。
```

**提示：**

- `1 <= s.length <= 1000`
- `s[i]` 仅包含 `'a'`, `'b'`, `'c'` 或 `'d'`
