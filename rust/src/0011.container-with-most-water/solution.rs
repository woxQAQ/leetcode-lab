// Created by woxQAQ at 2026/07/02 04:29
// leetgo: 1.4.17
// https://leetcode.cn/problems/container-with-most-water/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin

impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
        let mut l = 0;
        let mut r = height.len() - 1;
        let mut ans = 0;
        while l < r {
            ans = std::cmp::max(ans, (r - l) as i32 * (std::cmp::min(height[l], height[r])));
            if height[l] < height[r] {
                l += 1;
            } else {
                r -= 1;
            }
        }
        ans
    }
}

// @lc code=end

fn main() -> Result<()> {
    let height: Vec<i32> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::max_area(height).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
