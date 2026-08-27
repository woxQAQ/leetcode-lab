// Created by woxQAQ at 2026/07/25 15:41
// leetgo: 1.4.17
// https://leetcode.cn/problems/generate-parentheses/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin

impl Solution {
    pub fn generate_parenthesis(n: i32) -> Vec<String> {
        fn dfs(l: i32, r: i32, n: i32, path: &mut String, res: &mut Vec<String>) {
            if path.len() as i32 == 2 * n {
                res.push(path.clone());
            }
            if l < n {
                path.push('(');
                dfs(l + 1, r, n, path, res);
                path.pop();
            }
            if r < l {
                path.push(')');
                dfs(l, r + 1, n, path, res);
                path.pop();
            }
        }
        let mut res = vec![];
        dfs(0, 0, n, &mut "".into(), &mut res);
        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let n: i32 = deserialize(&read_line()?)?;
    let ans: Vec<String> = Solution::generate_parenthesis(n).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
