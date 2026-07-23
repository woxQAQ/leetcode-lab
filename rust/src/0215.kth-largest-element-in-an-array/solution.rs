// Created by woxQAQ at 2026/07/23 16:12
// leetgo: 1.4.17
// https://leetcode.cn/problems/kth-largest-element-in-an-array/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use rand::*;

impl Solution {
    pub fn find_kth_largest(mut nums: Vec<i32>, k: i32) -> i32 {
        let mut rng = rand::thread_rng();
        let target = k as usize - 1;
        let (mut l, mut r) = (0, nums.len());
        loop {
            let pivot = nums[rng.gen_range(l..r)];
            let (mut greeter, mut cur, mut less) = (l, l, r);
            while cur < less {
                match nums[cur].cmp(&pivot) {
                    std::cmp::Ordering::Less => {
                        less -= 1;
                        nums.swap(cur, less);
                    }
                    std::cmp::Ordering::Equal => {
                        cur += 1;
                    }
                    std::cmp::Ordering::Greater => {
                        nums.swap(greeter, cur);
                        greeter += 1;
                        cur += 1;
                    }
                }
            }
            if target < greeter {
                r = greeter;
            } else if target >= less {
                l = less;
            } else {
                return pivot;
            }
        }
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let k: i32 = deserialize(&read_line()?)?;
    let ans: i32 = Solution::find_kth_largest(nums, k).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
