// Created by woxQAQ at 2026/07/02 04:31
// leetgo: 1.4.17
// https://leetcode.cn/problems/3sum/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin

impl Solution {
    pub fn three_sum(mut nums: Vec<i32>) -> Vec<Vec<i32>> {
        nums.sort_unstable();
        let mut ans = vec![];
        for i in 0..nums.len() - 2 {
            let x = nums[i];
            let n = nums.len();
            if i > 0 && x == nums[i - 1] {
                continue;
            }
            if x + nums[i + 1] + nums[i + 2] > 0 {
                break;
            }
            if x + nums[n - 2] + nums[n - 1] < 0 {
                continue;
            }
            let mut j = i + 1;
            let mut k = n - 1;
            while j < k {
                let s = x + nums[j] + nums[k];
                if s == 0 {
                    ans.push(vec![x, nums[j], nums[k]]);
                    j += 1;
                    while j < k && nums[j] == nums[j - 1] {
                        j += 1;
                    }
                    k -= 1;
                    while j < k && nums[k] == nums[k + 1] {
                        k -= 1;
                    }
                } else if s < 0 {
                    j += 1;
                } else {
                    k -= 1;
                }
            }
        }
        ans
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let ans: Vec<Vec<i32>> = Solution::three_sum(nums).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
