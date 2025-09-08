# [1786. 从第一个节点出发到最后一个节点的受限路径数][link] (Medium)

[link]: https://leetcode.cn/problems/number-of-restricted-paths-from-first-to-last-node/

现有一个加权无向连通图。给你一个正整数 `n` ，表示图中有 `n` 个节点，并按从 `1` 到 `n` 给节点编号；另
给你一个数组 `edges` ，其中每个 `edges[i] = [uᵢ, vᵢ, weightᵢ]` 表示存在一条位于节点 `uᵢ` 和 `vᵢ` 之
间的边，这条边的权重为 `weightᵢ` 。

从节点 `start` 出发到节点 `end` 的路径是一个形如 `[z₀, z₁,z₂, ..., zₖ]` 的节点序列，满足 `z₀ = start
` 、 `zₖ = end` 且在所有符合 `0 <= i <= k-1` 的节点 `zᵢ` 和 `zᵢ₊₁` 之间存在一条边。

路径的距离定义为这条路径上所有边的权重总和。用 `distanceToLastNode(x)` 表示节点 `n` 和 `x` 之间路径
的最短距离。 **受限路径** 为满足 `distanceToLastNode(zᵢ) > distanceToLastNode(zᵢ₊₁)` 的一条路径，其
中 `0 <= i <= k-1` 。

返回从节点 `1` 出发到节点 `n` 的 **受限路径数** 。由于数字可能很大，请返回对 `10⁹ + 7` **取余** 的结
果。

**示例 1：**

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/03/07/restricted_paths_ex1.png)

```
输入：n = 5, edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]
输出：3
解释：每个圆包含黑色的节点编号和蓝色的 distanceToLastNode 值。三条受限路径分别是：
1) 1 --> 2 --> 5
2) 1 --> 2 --> 3 --> 5
3) 1 --> 3 --> 5
```

**示例 2：**

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/03/07/restricted_paths_ex22.png)

```
输入：n = 7, edges = [[1,3,1],[4,1,2],[7,3,4],[2,5,3],[5,6,1],[6,7,2],[7,5,3],[2,6,4]]
输出：1
解释：每个圆包含黑色的节点编号和蓝色的 distanceToLastNode 值。唯一一条受限路径是：1 --> 3 --> 7 。
```

**提示：**

- `1 <= n <= 2 * 10⁴`
- `n - 1 <= edges.length <= 4 * 10⁴`
- `edges[i].length == 3`
- `1 <= uᵢ, vᵢ <= n`
- `uᵢ != vᵢ`
- `1 <= weightᵢ <= 10⁵`
- 任意两个节点之间至多存在一条边
- 任意两个节点之间至少存在一条路径
