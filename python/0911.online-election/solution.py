# Created by woxQAQ at 2025/08/31 03:22
# leetgo: 1.4.13
# https://leetcode.cn/problems/online-election/

from bisect import bisect, bisect_left
from typing import *
from leetgo_py import *

# @lc code=begin


class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        cache = DefaultDict(int)
        tmp = None
        self.ans = [-1] * len(times)
        for i, v in enumerate(persons):
            cache[v] += 1
            if tmp is None or cache[persons[i]] >= cache[tmp]:
                tmp = persons[i]
            self.ans[i] = tmp

    def q(self, t: int) -> int:
        return self.ans[bisect_left(self.times, t + 1) - 1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    persons: List[int] = deserialize("List[int]", constructor_params[0])
    times: List[int] = deserialize("List[int]", constructor_params[1])
    obj = TopVotedCandidate(persons, times)

    for i in range(1, len(ops)):
        match ops[i]:
            case "q":
                method_params = split_array(params[i])
                t: int = deserialize("int", method_params[0])
                ans = serialize(obj.q(t))
                output.append(ans)

    print("\noutput:", join_array(output))
