// Created by woxQAQ at 2026/08/04 13:23
// leetgo: 1.4.17
// https://leetcode.cn/problems/find-missing-elements/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin

use std::collections::HashSet;
impl Solution {
    pub fn find_missing_elements(nums: Vec<i32>) -> Vec<i32> {
        let min = *nums.iter().min().unwrap();
        let max = *nums.iter().max().unwrap();
        let st: HashSet<i32> = nums.into_iter().collect();
        (min + 1..max).filter(|i| !st.contains(i)).collect()
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let ans: Vec<i32> = Solution::find_missing_elements(nums).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
