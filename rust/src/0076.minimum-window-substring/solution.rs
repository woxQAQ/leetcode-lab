// Created by woxQAQ at 2026/07/03 04:56
// leetgo: 1.4.17
// https://leetcode.cn/problems/minimum-window-substring/

use std::collections::HashMap;

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin

impl Solution {
    pub fn min_window(S: String, t: String) -> String {
        // 非常简单的思路：滑动窗口，滑动过程中检查是否符合覆盖条件
        // 若满足，则更新最小值，并移动左窗口
        let mut cnt_t = [0; 128];
        let mut cnt_s = [0; 128];
        for c in t.bytes() {
            cnt_t[c as usize] += 1;
        }
        let s = S.as_bytes();
        let m = s.len();
        let (mut ansl, mut ansr) = (0, m);
        let mut l = 0;
        fn is_covered(cnt_s: &[i32], cnt_t: &[i32]) -> bool {
            for i in b'A'..=b'Z' {
                if cnt_s[i as usize] < cnt_t[i as usize] {
                    return false;
                }
            }
            for i in b'a'..=b'z' {
                if cnt_s[i as usize] < cnt_t[i as usize] {
                    return false;
                }
            }
            true
        }
        for (r, &c) in s.iter().enumerate() {
            cnt_s[c as usize] += 1;
            while is_covered(&cnt_s, &cnt_t) {
                if r - l < ansr - ansl {
                    (ansl, ansr) = (l, r);
                }
                cnt_s[s[l] as usize] -= 1;
                l += 1;
            }
        }
        if ansr < m {
            S[ansl..=ansr].to_string()
        } else {
            "".to_string()
        }
    }
}

// @lc code=end

fn main() -> Result<()> {
    let s: String = deserialize(&read_line()?)?;
    let t: String = deserialize(&read_line()?)?;
    let ans: String = Solution::min_window(s, t).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
