// Created by woxQAQ at 2026/07/26 13:24
// leetgo: 1.4.17
// https://leetcode.cn/problems/median-of-two-sorted-arrays/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin

impl Solution {
    pub fn find_median_sorted_arrays(nums1: Vec<i32>, nums2: Vec<i32>) -> f64 {
        
    }
}

// @lc code=end

fn main() -> Result<()> {
	let nums1: Vec<i32> = deserialize(&read_line()?)?;
	let nums2: Vec<i32> = deserialize(&read_line()?)?;
	let ans: f64 = Solution::find_median_sorted_arrays(nums1, nums2).into();

	println!("\noutput: {}", serialize(ans)?);
	Ok(())
}
