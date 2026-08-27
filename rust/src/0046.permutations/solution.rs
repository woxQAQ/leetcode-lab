// Created by woxQAQ at 2026/07/23 18:27
// leetgo: 1.4.17
// https://leetcode.cn/problems/permutations/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin

impl Solution {
    pub fn permute(mut nums: Vec<i32>) -> Vec<Vec<i32>> {
        fn dfs(nums: &mut [i32], i: usize, res: &mut Vec<Vec<i32>>) {
            if i == nums.len() {
                res.push(nums.to_vec());
                return;
            }

            for j in i..nums.len() {
                nums.swap(i, j);
                dfs(nums, i + 1, res);
                nums.swap(i, j);
            }
        }

        let mut res = Vec::new();
        dfs(&mut nums, 0, &mut res);
        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let ans: Vec<Vec<i32>> = Solution::permute(nums).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
