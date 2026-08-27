// Created by woxQAQ at 2026/07/25 21:44
// leetgo: 1.4.17
// https://leetcode.cn/problems/palindrome-partitioning/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin

impl Solution {
    pub fn partition(s: String) -> Vec<Vec<String>> {
        fn is_palindrome(s: &str) -> bool {
            let s = s.as_bytes();
            let n = s.len();
            for i in 0..n / 2 {
                if s[i] != s[n - 1 - i] {
                    return false;
                }
            }
            true
        }
        fn dfs(s: &str, path: &mut Vec<String>, ans: &mut Vec<Vec<String>>) {
            if s.is_empty() {
                ans.push(path.clone());
                return;
            }
            for i in 1..=s.len() {
                let substr = &s[..i];
                if is_palindrome(substr) {
                    path.push(substr.to_string());
                    dfs(&s[i..], path, ans);
                    path.pop();
                }
            }
        }

        let mut ans = vec![];
        let mut path = vec![];
        dfs(&s, &mut path, &mut ans);
        ans
    }
}

// @lc code=end

fn main() -> Result<()> {
    let s: String = deserialize(&read_line()?)?;
    let ans: Vec<Vec<String>> = Solution::partition(s).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
