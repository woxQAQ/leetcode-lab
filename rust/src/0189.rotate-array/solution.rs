// Created by woxQAQ at 2026/07/10 11:32
// leetgo: 1.4.17
// https://leetcode.cn/problems/rotate-array/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin

impl Solution {
    pub fn rotate(nums: &mut Vec<i32>, k: i32) {
        let k = k as usize % nums.len();
        nums.reverse();
        nums[..k].reverse();
        nums[k..].reverse();
    }
}
// @lc code=end

fn main() -> Result<()> {
    let mut nums: Vec<i32> = deserialize(&read_line()?)?;
    let k: i32 = deserialize(&read_line()?)?;
    Solution::rotate(&mut nums, k);
    let ans: Vec<i32> = nums.into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
