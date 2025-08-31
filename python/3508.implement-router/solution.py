# Created by woxQAQ at 2025/08/31 15:01
# leetgo: 1.4.13
# https://leetcode.cn/problems/implement-router/

from bisect import bisect_left, bisect_right
from collections import defaultdict, deque
from typing import *

from leetgo_py import *

# @lc code=begin


class Router:
    def __init__(self, memoryLimit: int):
        self.queue = deque()
        self.set = set()
        self.limit = memoryLimit
        self.dest_time_map = defaultdict(deque)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)
        if packet in self.set:
            return False
        if len(self.queue) == self.limit:
            self.forwardPacket()
        self.queue.append(packet)
        self.set.add(packet)
        self.dest_time_map[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.queue:
            return []
        packet = self.queue.popleft()
        self.set.remove(packet)
        self.dest_time_map[packet[1]].popleft()
        return packet

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        times = self.dest_time_map[destination]
        i1 = bisect_left(times, startTime)
        i2 = bisect_right(times, endTime)
        return i2 - i1


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    memoryLimit: int = deserialize("int", constructor_params[0])
    obj = Router(memoryLimit)

    for i in range(1, len(ops)):
        match ops[i]:
            case "addPacket":
                method_params = split_array(params[i])
                source: int = deserialize("int", method_params[0])
                destination: int = deserialize("int", method_params[1])
                timestamp: int = deserialize("int", method_params[2])
                ans = serialize(obj.addPacket(source, destination, timestamp))
                output.append(ans)
            case "forwardPacket":
                ans = serialize(obj.forwardPacket())
                output.append(ans)
            case "getCount":
                method_params = split_array(params[i])
                destination: int = deserialize("int", method_params[0])
                startTime: int = deserialize("int", method_params[1])
                endTime: int = deserialize("int", method_params[2])
                ans = serialize(obj.getCount(destination, startTime, endTime))
                output.append(ans)

    print("\noutput:", join_array(output))
