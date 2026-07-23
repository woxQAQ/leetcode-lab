// Created by woxQAQ at 2026/07/10 11:37
// leetgo: 1.4.17
// https://leetcode.cn/problems/product-of-array-except-self/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin

impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut suf = vec![1; n];
        for i in (0..n - 1).rev() {
            suf[i] = suf[i + 1] * nums[i + 1]
        }
        let mut pre = vec![1; n];
        for i in 1..n {
            pre[i] = pre[i - 1] * nums[i - 1]
        }
        pre.iter().zip(suf.iter()).map(|(&p, &s)| p * s).collect()
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let ans: Vec<i32> = Solution::product_except_self(nums).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
