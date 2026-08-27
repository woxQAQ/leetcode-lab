// Created by woxQAQ at 2026/07/24 00:20
// leetgo: 1.4.17
// https://leetcode.cn/problems/subsets/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin

impl Solution {
    pub fn subsets(nums: Vec<i32>) -> Vec<Vec<i32>> {
        fn dfs(i: usize, nums: &[i32], path: &mut Vec<i32>, res: &mut Vec<Vec<i32>>) {
            res.push(path.clone());
            for j in i..nums.len() {
                path.push(nums[j]);
                dfs(j + 1, nums, path, res);
                path.pop();
            }
        }

        let mut res = Vec::new();
        let mut path = Vec::new();
        dfs(0, &nums, &mut path, &mut res);
        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let ans: Vec<Vec<i32>> = Solution::subsets(nums).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
