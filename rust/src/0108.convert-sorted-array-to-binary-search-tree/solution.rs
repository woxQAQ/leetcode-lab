// Created by woxQAQ at 2026/07/11 10:02
// leetgo: 1.4.17
// https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin

// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
//
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::cell::RefCell;
use std::rc::Rc;
impl Solution {
    pub fn sorted_array_to_bst(nums: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
        fn dfs(nums: &[i32]) -> Option<Rc<RefCell<TreeNode>>> {
            if nums.is_empty() {
                return None;
            }
            let mid = nums.len() / 2;
            Some(Rc::new(RefCell::new(TreeNode {
                val: nums[mid],
                left: dfs(&nums[..mid]),
                right: dfs(&nums[mid + 1..]),
            })))
        }
        dfs(&nums)
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let ans: BinaryTree = Solution::sorted_array_to_bst(nums).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
