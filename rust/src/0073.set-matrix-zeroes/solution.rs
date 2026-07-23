// Created by woxQAQ at 2026/07/10 12:07
// leetgo: 1.4.17
// https://leetcode.cn/problems/set-matrix-zeroes/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin

impl Solution {
    pub fn set_zeroes(matrix: &mut Vec<Vec<i32>>) {
        let (m, n) = (matrix.len(), matrix[0].len());
        let first_raw_has_zero = matrix[0].contains(&0);
        let first_column_has_zero = matrix.iter().any(|row| row[0] == 0);
        for i in 1..m {
            for j in 1..n {
                if matrix[i][j] == 0 {
                    matrix[0][j] = 0;
                    matrix[i][0] = 0;
                }
            }
        }
        for i in 1..m {
            for j in 1..n {
                if matrix[0][j] == 0 || matrix[i][0] == 0 {
                    matrix[i][j] = 0
                }
            }
        }
        if first_column_has_zero {
            for row in matrix.iter_mut() {
                row[0] = 0
            }
        }
        if first_raw_has_zero {
            matrix[0].fill(0);
        }
    }
}

// @lc code=end

fn main() -> Result<()> {
    let mut matrix: Vec<Vec<i32>> = deserialize(&read_line()?)?;
    Solution::set_zeroes(&mut matrix);
    let ans: Vec<Vec<i32>> = matrix.into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
