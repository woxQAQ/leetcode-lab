// Created by woxQAQ at 2026/07/10 13:34
// leetgo: 1.4.17
// https://leetcode.cn/problems/search-a-2d-matrix-ii/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin

impl Solution {
    pub fn search_matrix(matrix: Vec<Vec<i32>>, target: i32) -> bool {
        let (mut l, mut r) = (0, matrix[0].len() - 1);
        while l < matrix.len() {
            match matrix[l][r].cmp(&target) {
                std::cmp::Ordering::Equal => return true,
                std::cmp::Ordering::Less => l += 1,
                _ => match r == 0 {
                    true => break,
                    false => r -= 1,
                },
            }
        }
        false
    }
}

// @lc code=end

// Warning: this is a manual question, the generated test code may be incorrect.
fn main() -> Result<()> {
    let matrix: Vec<Vec<i32>> = deserialize(&read_line()?)?;
    let target: i32 = deserialize(&read_line()?)?;
    let ans: bool = Solution::search_matrix(matrix, target).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
