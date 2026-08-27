// Created by woxQAQ at 2026/07/25 15:48
// leetgo: 1.4.17
// https://leetcode.cn/problems/word-search/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin

impl Solution {
    pub fn exist(mut board: Vec<Vec<char>>, word: String) -> bool {
        const DIR: [(isize, isize); 4] = [(0, -1), (0, 1), (-1, 0), (1, 0)];
        fn dfs(
            board: &mut Vec<Vec<char>>,
            word: &[u8],
            x: usize,
            y: usize,
            k: usize,
            m: usize,
            n: usize,
        ) -> bool {
            if board[x][y] != word[k] as char {
                return false;
            }
            if k + 1 == word.len() {
                return true;
            }
            board[x][y] = '\0';
            for (dx, dy) in DIR {
                let (nx, ny) = (x as isize + dx, y as isize + dy);
                if nx >= 0
                    && nx < m as isize
                    && ny >= 0
                    && ny < n as isize
                    && dfs(board, word, nx as usize, ny as usize, k + 1, m, n)
                {
                    return true;
                }
            }
            board[x][y] = word[k] as char;
            false
        }
        let (m, n) = (board.len(), board[0].len());
        for i in 0..m {
            for j in 0..n {
                if dfs(&mut board, word.as_bytes(), i, j, 0, m, n) {
                    return true;
                }
            }
        }
        false
    }
}

// @lc code=end

fn main() -> Result<()> {
    let board: Vec<Vec<char>> = deserialize(&read_line()?)?;
    let word: String = deserialize(&read_line()?)?;
    let ans: bool = Solution::exist(board, word).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
