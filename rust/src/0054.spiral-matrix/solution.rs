// Created by woxQAQ at 2026/07/10 12:37
// leetgo: 1.4.17
// https://leetcode.cn/problems/spiral-matrix/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin

impl Solution {
    pub fn spiral_order(matrix: Vec<Vec<i32>>) -> Vec<i32> {
        let dirs: [(i32, i32); 4] = [(0, 1), (1, 0), (0, -1), (-1, 0)];
        let (mut m, mut n) = (matrix.len(), matrix[0].len());
        let size = m * n;
        let mut ans = Vec::with_capacity(size);
        let (mut i, mut j) = (0, -1);
        let mut di = 0;
        while ans.len() < size {
            let (dx, dy) = dirs[di];
            for _ in 0..n {
                i += dx;
                j += dy;
                ans.push(matrix[i as usize][j as usize]);
            }
            di = (di + 1) % 4;
            (m, n) = (n, m - 1)
        }
        ans
    }
}

// @lc code=end

fn main() -> Result<()> {
    let matrix: Vec<Vec<i32>> = deserialize(&read_line()?)?;
    let ans: Vec<i32> = Solution::spiral_order(matrix).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
