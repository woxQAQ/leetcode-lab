// Created by woxQAQ at 2026/07/02 13:36
// leetgo: 1.4.17
// https://leetcode.cn/problems/sliding-window-maximum/

use std::collections::VecDeque;

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin

impl Solution {
    pub fn max_sliding_window(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let k = k as usize;
        let mut ans = Vec::with_capacity(nums.len() - k + 1);
        // monotonic queue
        let mut q = VecDeque::new();
        for (i, &num) in nums.iter().enumerate() {
            while !q.is_empty() && nums[*q.back().unwrap()] <= num {
                q.pop_back();
            }
            q.push_back(i);
            // q[0] is the index of the maximum element in the current window
            // the window length is i - q[0] + 1
            // if the window length exceeds k,
            // it means the front element is out of the current window
            // so i - q[0] + 1 < k => q[0] > i - k + 1 => q[0] >= i-k
            if q[0] + k <= i {
                q.pop_front();
            }
            // after i >= k - 1, the window length is k,
            // q[0] is the index of the maximum element in the current window
            if i + 1 >= k {
                ans.push(nums[q[0]]);
            }
        }
        ans
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let k: i32 = deserialize(&read_line()?)?;
    let ans: Vec<i32> = Solution::max_sliding_window(nums, k).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
