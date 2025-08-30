# Created by woxQAQ at 2025/08/31 03:12
# leetgo: 1.4.13
# https://leetcode.cn/problems/snapshot-array/

from bisect import bisect_left
from collections import defaultdict
from typing import *
from leetgo_py import *

# @lc code=begin


class SnapshotArray:
    def __init__(self, length: int):
        self.cur_snap_id = 0
        self.cache = defaultdict(list)

    def set(self, index: int, val: int) -> None:
        self.cache[index].append((self.cur_snap_id, val))

    def snap(self) -> int:
        self.cur_snap_id += 1
        return self.cur_snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        if not self.cache[index]:
            return 0
        # [(1,3),(1,2),(2,3),(2,5)]
        i = bisect_left(self.cache[index], (snap_id + 1,)) - 1
        return self.cache[index][i][1] if i >= 0 else 0


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    length: int = deserialize("int", constructor_params[0])
    obj = SnapshotArray(length)

    for i in range(1, len(ops)):
        match ops[i]:
            case "set":
                method_params = split_array(params[i])
                index: int = deserialize("int", method_params[0])
                val: int = deserialize("int", method_params[1])
                obj.set(index, val)
                output.append("null")
            case "snap":
                ans = serialize(obj.snap())
                output.append(ans)
            case "get":
                method_params = split_array(params[i])
                index: int = deserialize("int", method_params[0])
                snap_id: int = deserialize("int", method_params[1])
                ans = serialize(obj.get(index, snap_id))
                output.append(ans)

    print("\noutput:", join_array(output))
