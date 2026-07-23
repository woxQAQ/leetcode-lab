// Created by woxQAQ at 2026/07/02 06:38
// leetgo: 1.4.17
// https://leetcode.cn/problems/find-all-anagrams-in-a-string/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin

impl Solution {
    pub fn find_anagrams(s: String, p: String) -> Vec<i32> {
        let mut left = 0;
        let mut ans = vec![];
        let s = s.as_bytes();
        let mut cnt = [0; 26];
        for c in p.bytes() {
            cnt[(c - b'a') as usize] += 1;
        }
        for (right, &c) in s.iter().enumerate() {
            let c = (c - b'a') as usize;
            cnt[c] -= 1;
            while cnt[c] < 0 {
                cnt[(s[left] - b'a') as usize] += 1;
                left += 1;
            }
            // right - left + 1 == p.len() may cause overflow in some cases
            if right + 1 == p.len() + left {
                ans.push(left as i32);
            }
        }
        ans
    }
}

// @lc code=end

fn main() -> Result<()> {
    let s: String = deserialize(&read_line()?)?;
    let p: String = deserialize(&read_line()?)?;
    let ans: Vec<i32> = Solution::find_anagrams(s, p).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
