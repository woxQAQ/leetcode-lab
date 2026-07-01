// Created by woxQAQ at 2026/07/02 03:55
// leetgo: 1.4.17
// https://leetcode.cn/problems/two-sum/

use core::unreachable;
use std::collections::HashMap;

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut m = HashMap::new();
        for (i, &x) in nums.iter().enumerate() {
            if let Some(&j) = m.get(&(target - x)) {
                return vec![j as i32, i as i32];
            }
            m.insert(x, i);
        }
        unreachable!()
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let target: i32 = deserialize(&read_line()?)?;
    let ans: Vec<i32> = Solution::two_sum(nums, target).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
