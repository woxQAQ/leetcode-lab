// Created by woxQAQ at 2026/07/25 22:13
// leetgo: 1.4.17
// https://leetcode.cn/problems/search-insert-position/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin

impl Solution {
    pub fn search_insert(nums: Vec<i32>, target: i32) -> i32 {
        let mut l = -1;
        let mut r = nums.len() as i32;
        while l < r - 1 {
            let mid = (l + r) / 2;
            if nums[mid as usize] < target {
                l = mid;
            } else {
                r = mid;
            }
        }
        return r;
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let target: i32 = deserialize(&read_line()?)?;
    let ans: i32 = Solution::search_insert(nums, target).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
