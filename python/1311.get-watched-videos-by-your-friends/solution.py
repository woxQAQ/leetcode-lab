# Created by woxQAQ at 2025/09/07 19:55
# leetgo: 1.4.15
# https://leetcode.cn/problems/get-watched-videos-by-your-friends/

from collections import defaultdict, deque
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def watchedVideosByFriends(
        self,
        watchedVideos: List[List[str]],
        friends: List[List[int]],
        id: int,
        level: int,
    ) -> List[str]:
        n = len(friends)
        g = [[] for _ in range(n)]
        for i, friend_list in enumerate(friends):
            for friend in friend_list:
                g[i].append(friend)
        ans = defaultdict(int)

        def bfs():
            q = deque([id])
            dis = [-1] * n
            dis[id] = 0

            nonlocal ans
            while q:
                x = q.popleft()
                for y in g[x]:
                    if dis[y] < 0:
                        q.append(y)
                        dis[y] = dis[x] + 1
                        if level == dis[y]:
                            for video in watchedVideos[y]:
                                ans[video] += 1

        bfs()

        return sorted(ans, key=lambda x: (ans[x], x))


# @lc code=end

if __name__ == "__main__":
    watchedVideos: List[List[str]] = deserialize("List[List[str]]", read_line())
    friends: List[List[int]] = deserialize("List[List[int]]", read_line())
    id: int = deserialize("int", read_line())
    level: int = deserialize("int", read_line())
    ans = Solution().watchedVideosByFriends(watchedVideos, friends, id, level)
    print("\noutput:", serialize(ans, "string[]"))
