// Created by woxQAQ at 2026/07/10 11:57
// leetgo: 1.4.17
// https://leetcode.cn/problems/first-missing-positive/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin

impl Solution {
    pub fn first_missing_positive(mut nums: Vec<i32>) -> i32 {
        // 思路：把值(1<= x <= n) 放在该出现的位置上：
        // 比如 [2,1,0]，2 应该出现在 2-1 下标处，1 应该出现 1-1 下标处
        // 变成 [1,2,?]
        // 那么，此时我们遍历这个数组，找到第一个失位的元素，即为答案。若没有
        // 则答案为 n+1
        //
        let n = nums.len();

        // 检查每个元素
        for i in 0..n {
            // 1. 把值放在该在的位置：
            // 对 1 <= nums[i] <=n
            // 他应该出现的位置是 nums[i] -1.
            // 持续交换 i 与 nums[i]-1 ([0,n-1],不可能溢出) 的元素，直到满足条件
            while 1 <= nums[i] && nums[i] as usize <= n && nums[(nums[i] - 1) as usize] != nums[i] {
                let j = (nums[i] - 1) as usize;
                nums.swap(i, j);
            }
        }
        // 2. 找到第一个失位元素
        for i in 0..n {
            if nums[i] != (i + 1) as i32 {
                return (i + 1) as _;
            }
        }
        (n + 1) as _
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::first_missing_positive(nums).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
