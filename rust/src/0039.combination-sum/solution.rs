// Created by woxQAQ at 2026/07/25 14:39
// leetgo: 1.4.17
// https://leetcode.cn/problems/combination-sum/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin

impl Solution {
    pub fn combination_sum(mut candidates: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
        candidates.sort();
        fn dfs(
            i: usize,
            target: i32,
            candidates: &Vec<i32>,
            selected: &mut Vec<i32>,
            ans: &mut Vec<Vec<i32>>,
        ) {
            if target == 0 {
                ans.push(selected.clone());
                return;
            }
            if target < candidates[i] {
                return;
            }
            for j in i..candidates.len() {
                selected.push(candidates[j]);
                dfs(j, target - candidates[j], candidates, selected, ans);
                selected.pop();
            }
        }
        let mut ans = vec![];
        dfs(0, target, &candidates, &mut vec![], &mut ans);
        ans
    }
}

// @lc code=end

fn main() -> Result<()> {
    let candidates: Vec<i32> = deserialize(&read_line()?)?;
    let target: i32 = deserialize(&read_line()?)?;
    let ans: Vec<Vec<i32>> = Solution::combination_sum(candidates, target).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
