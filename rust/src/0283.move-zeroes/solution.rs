// Created by woxQAQ at 2026/07/02 04:22
// leetgo: 1.4.17
// https://leetcode.cn/problems/move-zeroes/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin

impl Solution {
    pub fn move_zeroes(nums: &mut Vec<i32>) {
        let mut i0 = 0;
        for i in 0..nums.len() {
            if nums[i] != 0 {
                nums.swap(i, i0);
                i0 += 1;
            }
        }
    }
}

// @lc code=end

fn main() -> Result<()> {
    let mut nums: Vec<i32> = deserialize(&read_line()?)?;
    Solution::move_zeroes(&mut nums);
    let ans: Vec<i32> = nums.into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
