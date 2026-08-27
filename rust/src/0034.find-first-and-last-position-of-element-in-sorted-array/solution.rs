// Created by woxQAQ at 2026/07/25 23:02
// leetgo: 1.4.17
// https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin

impl Solution {
    pub fn lower_bound(nums: &Vec<i32>, target: i32) -> usize {
        // 左闭右开
        // 不变量 l-1 红色
        // r 蓝色
        // 循环结束有 l = r
        let (mut l, mut r) = (0, nums.len());
        while l < r {
            let mid = (l + r) / 2;
            if nums[mid] < target {
                l = mid + 1 // [l,mid] 为红， l =mid+1
            } else {
                r = mid // [mid,r) 为蓝, r = mid
            }
        }
        return l as usize;
    }
    pub fn search_range(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let start = Self::lower_bound(&nums, target);
        if start == nums.len() || nums[start] != target {
            return vec![-1, -1];
        }
        // upper_bound(target) = lower_bound(target+1) -1
        // start = lower_bound(target)
        // => for all i >= start, value >= target
        // => for all i >= start + 1, value > target
        // end = upper_bound(target)
        // => for all i <= end, value <= target
        // => for all i <= end - 1, value < target
        let end = Self::lower_bound(&nums, target + 1) - 1;
        vec![start as i32, end as i32]
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let target: i32 = deserialize(&read_line()?)?;
    let ans: Vec<i32> = Solution::search_range(nums, target).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
