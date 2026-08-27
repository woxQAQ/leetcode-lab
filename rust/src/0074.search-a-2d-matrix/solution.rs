// Created by woxQAQ at 2026/07/25 22:23
// leetgo: 1.4.17
// https://leetcode.cn/problems/search-a-2d-matrix/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin

impl Solution {
    pub fn search_matrix(matrix: Vec<Vec<i32>>, target: i32) -> bool {
        let (m, n) = (matrix.len() as i32, matrix[0].len() as i32);
        let (mut l, mut r) = (-1, m * n);
        while l < r - 1 {
            let mid = (l + r) / 2;
            let x = matrix[(mid / n) as usize][(mid % n) as usize];
            if x == target {
                return true;
            } else if x < target {
                l = mid;
            } else {
                r = mid;
            }
        }
        false
    }
}

// @lc code=end

fn main() -> Result<()> {
    let matrix: Vec<Vec<i32>> = deserialize(&read_line()?)?;
    let target: i32 = deserialize(&read_line()?)?;
    let ans: bool = Solution::search_matrix(matrix, target).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
