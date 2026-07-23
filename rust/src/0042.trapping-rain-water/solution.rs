// Created by woxQAQ at 2026/07/02 04:46
// leetgo: 1.4.17
// https://leetcode.cn/problems/trapping-rain-water/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin

impl Solution {
    pub fn trap(height: Vec<i32>) -> i32 {
        // for location i, the trap water is min(left_max_height, right_max_height) - height[i]
        let mut ans = 0;

        // prefix[i] is the max height from 0 to i
        // suffix[i] is the max height from n-1 to i
        // we update prefix and suffix from both ends to the center
        let mut prefix = 0;
        let mut suffix = 0;
        let mut left = 0;
        let mut right = height.len() - 1;
        while left < right {
            prefix = prefix.max(height[left]);
            suffix = suffix.max(height[right]);
            // if prefix < suffix, the left_max_height = prefix
            // we don't know the right_max_height
            // but we know left_max_height = prefix < suffix <= right_max_height
            // so min(left_max_height, right_max_height) = prefix
            // we can calculate the trap water at location left
            // ans = prefix - height[left]
            //
            // on contrary, if prefix >= suffix, the right_max_height = suffix
            // we don't know the left_max_height
            // but we know left_max_height <= prefix >= suffix <= right_max_height
            // so min(left_max_height, right_max_height) = suffix
            // we can calculate the trap water at location right
            // ans = suffix - height[right]
            //
            // it's obvious that all the elements in the array will be calculated
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
