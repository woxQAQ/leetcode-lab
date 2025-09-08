# Created by woxQAQ at 2025/09/08 12:24
# leetgo: 1.4.15
# https://leetcode.cn/problems/find-all-possible-recipes-from-given-supplies/

from collections import defaultdict, deque
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def findAllRecipes(
        self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]
    ) -> List[str]:
        indeg = {recipe: 0 for recipe in recipes}
        graph = defaultdict(list)
        for recipe, ingredient in zip(recipes, ingredients):
            for ing in ingredient:
                graph[ing].append(recipe)
            indeg[recipe] += len(ingredient)
        ans = []
        q = deque(supplies)
        while q:
            supply = q.popleft()
            for recipe in graph[supply]:
                indeg[recipe] -= 1
                if indeg[recipe] == 0:
                    ans.append(recipe)
                    q.append(recipe)
        return ans


# @lc code=end

if __name__ == "__main__":
    recipes: List[str] = deserialize("List[str]", read_line())
    ingredients: List[List[str]] = deserialize("List[List[str]]", read_line())
    supplies: List[str] = deserialize("List[str]", read_line())
    ans = Solution().findAllRecipes(recipes, ingredients, supplies)
    print("\noutput:", serialize(ans, "string[]"))
