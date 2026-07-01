// Created by woxQAQ at 2026/07/02 04:01
// leetgo: 1.4.17
// https://leetcode.cn/problems/group-anagrams/

use std::collections::HashMap;

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin

impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut m: HashMap<Vec<u8>, Vec<String>> = HashMap::new();
        for s in strs {
            let mut sorted_s = s.as_bytes().to_vec();
            sorted_s.sort_unstable();
            m.entry(sorted_s).or_default().push(s);
        }
        println!("{:?}", m);
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
