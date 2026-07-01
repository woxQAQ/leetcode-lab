// Created by woxQAQ at 2026/07/02 04:46
// leetgo: 1.4.17
// https://leetcode.cn/problems/trapping-rain-water/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin

impl Solution {
    pub fn trap(height: Vec<i32>) -> i32 {
        let mut ans = 0;
        let mut prefix = 0;
        let mut suffix = 0;
        let mut left = 0;
        let mut right = height.len() - 1;
        while left < right {
            prefix = prefix.max(height[left]);
            suffix = suffix.max(height[right]);
            if prefix < suffix {
                ans += prefix - height[left];
                left += 1;
            } else {
                ans += suffix - height[right];
                right -= 1;
            }
        }
        ans
    }
}

// @lc code=end

fn main() -> Result<()> {
	let height: Vec<i32> = deserialize(&read_line()?)?;
	let ans: i32 = Solution::trap(height).into();

	println!("\noutput: {}", serialize(ans)?);
	Ok(())
}
