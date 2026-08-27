// Created by woxQAQ at 2026/07/25 10:30
// leetgo: 1.4.17
// https://leetcode.cn/problems/letter-combinations-of-a-phone-number/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin

impl Solution {
    pub fn letter_combinations(digits: String) -> Vec<String> {
        if digits.is_empty() {
            return vec![];
        }

        const MAPPING: [&str; 8] = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"];
        fn dfs(i: usize, ans: &mut Vec<String>, path: &mut String, digits: &[u8]) {
            if i == digits.len() {
                ans.push(path.clone());
                return;
            }
            for c in MAPPING[(digits[i] - b'2') as usize].chars() {
                path.push(c);
                dfs(i + 1, ans, path, digits);
                path.pop();
            }
        }
        let digits = digits.as_bytes();
        let capacity = digits
            .iter()
            .map(|&d| MAPPING[(d - b'2') as usize].len())
            .product();
        let mut ans = Vec::with_capacity(capacity);
        let mut path = String::with_capacity(capacity);
        dfs(0, &mut ans, &mut path, digits);
        ans
    }
}

// @lc code=end

fn main() -> Result<()> {
    let digits: String = deserialize(&read_line()?)?;
    let ans: Vec<String> = Solution::letter_combinations(digits).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
