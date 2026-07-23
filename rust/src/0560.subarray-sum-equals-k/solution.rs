// Created by woxQAQ at 2026/07/02 07:05
// leetgo: 1.4.17
// https://leetcode.cn/problems/subarray-sum-equals-k/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin

impl Solution {
    pub fn subarray_sum(nums: Vec<i32>, k: i32) -> i32 {
        // subarray sum between i and j
        // can be converted to prefix sum difference
        // sum[i,j] = prefix_sum[j+1] - prefix_sum[i]
        // k = prefix_sum[j+1] - prefix_sum[i]
        // commonly, prefix_sum[j+1] - k = prefix_sum[i]
        // the problem is converted to
        // find the number of pairs (i, j) such that prefix_sum[j] - k = prefix_sum[i]
        let mut prefix_sum = vec![0; nums.len() + 1];
        for (i, &num) in nums.iter().enumerate() {
            prefix_sum[i + 1] = prefix_sum[i] + num;
        }
        let mut cnt: std::collections::HashMap<&i32, i32> =
            std::collections::HashMap::with_capacity(prefix_sum.len());
        let mut ans = 0;
        // iter the prefix sum array
        // we need to know, at the index i, how many prefix sums are equal to prefix_sum[i] - k
        // so we use a hashmap to store current state of the prefix sum occurrences
        for s in &prefix_sum {
            if let Some(&c) = cnt.get(&(s - k)) {
                ans += c;
            }
            *cnt.entry(s).or_default() += 1;
        }
        ans
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let k: i32 = deserialize(&read_line()?)?;
    let ans: i32 = Solution::subarray_sum(nums, k).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
