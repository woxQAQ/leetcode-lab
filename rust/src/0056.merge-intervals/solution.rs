// Created by woxQAQ at 2026/07/10 09:57
// leetgo: 1.4.17
// https://leetcode.cn/problems/merge-intervals/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin

impl Solution {
    pub fn merge(mut intervals: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        intervals.sort_unstable_by_key(|p| p[0]);
        let mut res: Vec<Vec<i32>> = vec![];
        for int in intervals {
            match res.last_mut() {
                Some(last) => match int[0] <= last[1] {
                    true => last[1] = last[1].max(int[1]),
                    false => res.push(int),
                },
                None => res.push(int),
            }
        }
        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let intervals: Vec<Vec<i32>> = deserialize(&read_line()?)?;
    let ans: Vec<Vec<i32>> = Solution::merge(intervals).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
