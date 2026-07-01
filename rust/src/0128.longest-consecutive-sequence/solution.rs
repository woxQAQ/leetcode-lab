// Created by woxQAQ at 2026/07/02 04:15
// leetgo: 1.4.17
// https://leetcode.cn/problems/longest-consecutive-sequence/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin

impl Solution {
    pub fn longest_consecutive(nums: Vec<i32>) -> i32 {
        let m = nums.into_iter().collect::<std::collections::HashSet<_>>();
        let mut res = 0;
        for &x in &m {
            if m.contains(&(x - 1)) {
                continue;
            }
            let mut y = x + 1;
            while m.contains(&y) {
                y += 1;
            }
            res = res.max(y - x);
        }
        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::longest_consecutive(nums).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
