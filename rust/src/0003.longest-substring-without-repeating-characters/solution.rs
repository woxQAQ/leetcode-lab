// Created by woxQAQ at 2026/07/02 06:29
// leetgo: 1.4.17
// https://leetcode.cn/problems/longest-substring-without-repeating-characters/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin

impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        // slide window: iter right end, move left
        let mut left = 0;
        let mut ans = 0;
        let s = s.as_bytes();
        // cnt maintains the count of each character in the current window [left,r]
        // if any character count exceeds 1, move left end to avoid repeating characters
        let mut cnt = [0; 128];
        for (r, &c) in s.iter().enumerate() {
            let c = c as usize;
            cnt[c] += 1;
            while cnt[c] > 1 {
                let left_c = s[left] as usize;
                cnt[left_c] -= 1;
                left += 1;
            }
            ans = std::cmp::max(ans, r - left + 1);
        }
        ans as i32
    }
}

// @lc code=end

fn main() -> Result<()> {
    let s: String = deserialize(&read_line()?)?;
    let ans: i32 = Solution::length_of_longest_substring(s).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
