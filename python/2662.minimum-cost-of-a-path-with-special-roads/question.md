# [2662. 前往目标的最小代价][link] (Medium)

[link]: https://leetcode.cn/problems/minimum-cost-of-a-path-with-special-roads/

给你一个数组 `start` ，其中 `start = [startX, startY]` 表示你的初始位置位于二维空间上的 `(startX, st
artY)` 。另给你一个数组 `target` ，其中 `target = [targetX, targetY]` 表示你的目标位置 `(targetX, ta
rgetY)` 。

从位置 `(x1, y1)` 到空间中任一其他位置 `(x2, y2)` 的 **代价** 是 `|x2 - x1| + |y2 - y1|` 。

给你一个二维数组 `specialRoads` ，表示空间中存在的一些 **特殊路径**。其中 `specialRoads[i] = [x1ᵢ, y
1ᵢ, x2ᵢ, y2ᵢ, costᵢ]` 表示第 `i` 条特殊路径可以从 `(x1ᵢ, y1ᵢ)` 到 `(x2ᵢ, y2ᵢ)` ，但成本等于 `costᵢ` 
。你可以使用每条特殊路径任意次数。

返回从 `(startX, startY)` 到 `(targetX, targetY)` 所需的 **最小** 代价。

**示例 1：**

**输入：** start = \[1,1\], target = \[4,5\], specialRoads = \[\[1,2,3,3,2\],\[3,4,4,5,1\]\]

**输出：** 5

**解释：**

1. (1,1) 到 (1,2) 花费为 \|1 - 1\| + \|2 - 1\| = 1。
2. (1,2) 到 (3,3)。使用 `specialRoads[0]` 花费为 2。
3. (3,3) 到 (3,4) 花费为 \|3 - 3\| + \|4 - 3\| = 1。
4. (3,4) 到 (4,5)。使用 `specialRoads[1]` 花费为 1。

所以总花费是 1 + 2 + 1 + 1 = 5。

**示例 2：**

**输入：** start = \[3,2\], target = \[5,7\], specialRoads = \[\[5,7,3,2,1\],\[3,2,3,4,4\],\[3,3,5,5
,5\],\[3,4,5,6,6\]\]

**输出：**7

**解释：**

不使用任何特殊路径，直接从开始到结束位置是最优的，花费为 \|5 - 3\| + \|7 - 2\| = 7。

注意 `specialRoads[0]` 直接从 (5,7) 到 (3,2)。

**示例 3：**

**输入：** start = \[1,1\], target = \[10,4\], specialRoads = \[\[4,2,1,1,3\],\[1,2,7,4,4\],\[10,3,6
,1,2\],\[6,1,1,2,3\]\]

**输出：**8

**解释：**

1. (1,1) 到 (1,2) 花费为 \|1 - 1\| + \|2 - 1\| = 1。
2. (1,2) 到 (7,4)。使用 `specialRoads[1]` 花费为 4。
3. (7,4) 到 (10,4) 花费为 \|10 - 7\| + \|4 - 4\| = 3。

**提示：**

- `start.length == target.length == 2`
- `1 <= startX <= targetX <= 10⁵`
- `1 <= startY <= targetY <= 10⁵`
- `1 <= specialRoads.length <= 200`
- `specialRoads[i].length == 5`
- `startX <= x1ᵢ, x2ᵢ <= targetX`
- `startY <= y1ᵢ, y2ᵢ <= targetY`
- `1 <= costᵢ <= 10⁵`
