// Created by woxQAQ at 2026/07/26 11:25
// leetgo: 1.4.17
// https://leetcode.cn/problems/search-in-rotated-sorted-array/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin

impl Solution {
    // x = nums[mid]
    // [4,5,6,7,8,0,1,2] target = 0
    // if x > last: x 在第一段
    //   if target < last, target 在第二段
    //   if target > last, target 在第一段
    // x < last: x 在第二段
    //   if target < last, target 在第二段
    //   if target > last, target 在第一段
    // target 和 x 在同一段和普通的 lower_bound 是一样的，考虑不在同一段的情况
    // x > last > target,答案在mid右边
    // target > last > x,答案在mid左边
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let (mut l, mut r) = (0, nums.len());
        let last = *nums.last().unwrap();
        while l < r {
            let mid = (l + r) / 2;
            let x = nums[mid];
            if target > last && last >= x {
                r = mid;
            } else if x > last && last >= target {
                l = mid + 1;
            } else if x >= target {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        if nums[r] == target { r as i32 } else { -1 }
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let target: i32 = deserialize(&read_line()?)?;
    let ans: i32 = Solution::search(nums, target).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
