# [1239. 串联字符串的最大长度][link] (Medium)

[link]: https://leetcode.cn/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

给定一个字符串数组 `arr`，字符串 `s` 是将 `arr` 的含有 **不同字母** 的 **子序列** 字符串 **连接** 所
得的字符串。

请返回所有可行解 `s` 中最长长度。

**子序列** 是一种可以从另一个数组派生而来的数组，通过删除某些元素或不删除元素而不改变其余元素的顺序
。

**示例 1：**

```
输入：arr = ["un","iq","ue"]
输出：4
解释：所有可能的串联组合是：
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
最大长度为 4。
```

**示例 2：**

```
输入：arr = ["cha","r","act","ers"]
输出：6
解释：可能的解答有 "chaers" 和 "acters"。
```

**示例 3：**

```
输入：arr = ["abcdefghijklmnopqrstuvwxyz"]
输出：26
```

**提示：**

- `1 <= arr.length <= 16`
- `1 <= arr[i].length <= 26`
- `arr[i]` 中只含有小写英文字母
