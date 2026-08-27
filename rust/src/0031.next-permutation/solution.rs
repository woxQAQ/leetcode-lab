// Created by woxQAQ at 2026/07/26 21:47
// leetgo: 1.4.17
// https://leetcode.cn/problems/next-permutation/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin

impl Solution {
    pub fn next_permutation(nums: &mut Vec<i32>) {
        let n = nums.len();
        let mut i = n as isize - 2;
        while i >= 0 && nums[i as usize] >= nums[i as usize + 1] {
            i -= 1;
        }
        if i >= 0 {
            let i = i as usize;
            let mut j = n - 1;
            while nums[j] <= nums[i] {
                j -= 1;
            }
            nums.swap(i, j)
        }
        nums[(i + 1) as usize..].reverse();
    }
}

// @lc code=end

fn main() -> Result<()> {
    let mut nums: Vec<i32> = deserialize(&read_line()?)?;
    Solution::next_permutation(&mut nums);
    let ans: Vec<i32> = nums.into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
