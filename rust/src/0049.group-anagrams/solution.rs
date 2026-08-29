// Created by woxQAQ at 2026/08/29 10:31
// leetgo: 1.4.17
// https://leetcode.cn/problems/group-anagrams/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin

use std::collections::HashMap;
impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut m: HashMap<_, Vec<_>> = HashMap::new();
        for str in strs {
            let mut cnt = [0u8; 26];
            for &b in str.as_bytes() {
                cnt[(b - b'a') as usize] += 1;
            }
            m.entry(cnt).or_default().push(str);
        }
        m.into_values().collect()
    }
}

// @lc code=end

fn main() -> Result<()> {
    let strs: Vec<String> = deserialize(&read_line()?)?;
    let ans: Vec<Vec<String>> = Solution::group_anagrams(strs).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
