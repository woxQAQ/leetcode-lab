// Created by woxQAQ at 2026/08/17 21:24
// leetgo: 1.4.17
// https://leetcode.cn/problems/multiply-strings/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin

impl Solution {
    pub fn multiply(num1: String, num2: String) -> String {
        if num1 == "0" || num2 == "0" {
            return "0".to_string();
        }
        //    1 2 3
        //      5 6
        // --------
        //      1 8 ==> [0,0,6,12,18]
        //    1 2
        //    6     ==> [0,0,6,12,18]
        // --------
        //    7 3 8 ==> [0,5,10,15,0] 合并
        //    1 5   ==> [0,5,16,27,18] 逆序遍历，逢10进位
        //  1 0     ==> [0,5,16,28,8]
        //  5       ==> [0,5,18,8,8]
        // --------
        //  6 8 8 8 ==> [0,6,8,8,8] 去掉前导0
        let m = num1.len();
        let n = num2.len();
        let mut res = vec![0; m + n];
        let n1 = num1.as_bytes();
        let n2 = num2.as_bytes();
        for (i, &x) in n1.iter().enumerate().rev() {
            let d1 = (x - b'0') as u32;
            for (j, &y) in n2.iter().enumerate().rev() {
                let d2 = (y - b'0') as u32;
                res[i + j + 1] += d1 * d2;
            }
        }
        for i in (1..m + n).rev() {
            res[i - 1] += res[i] / 10;
            res[i] %= 10;
        }
        let start = if res[0] == 0 { 1 } else { 0 };
        res[start..].iter().map(|d| d.to_string()).collect()
    }
}

// @lc code=end

fn main() -> Result<()> {
    let num1: String = deserialize(&read_line()?)?;
    let num2: String = deserialize(&read_line()?)?;
    let ans: String = Solution::multiply(num1, num2).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
