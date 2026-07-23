// Created by woxQAQ at 2026/07/10 09:12
// leetgo: 1.4.17
// https://leetcode.cn/problems/maximum-subarray/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin

impl Solution {
    pub fn max_sub_array(nums: Vec<i32>) -> i32 {
        return max_sub_array_const(nums);
    }
}

fn max_sub_array_N(nums: Vec<i32>) -> i32 {
    let mut dp = vec![0; nums.len()];
    dp[0] = nums[0];
    for i in 1..nums.len() {
        dp[i] = nums[i] + 0.max(dp[i - 1])
    }
    return *dp.iter().max().unwrap();
}

fn max_sub_array_const(nums: Vec<i32>) -> i32 {
    let mut prev = 0;
    let mut res = i32::MIN;
    for i in 0..nums.len() {
        prev = nums[i] + prev.max(0);
        res = res.max(prev);
    }
    res
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::max_sub_array(nums).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
