// Created by woxQAQ at 2026/07/11 17:00
// leetgo: 1.4.17
// https://leetcode.cn/problems/path-sum-iii/

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
    pub fn path_sum(root: Option<Rc<RefCell<TreeNode>>>, target_sum: i32) -> i32 {
        fn dfs(node: &Rc<RefCell<TreeNode>>, path: i64, target: i64) -> i32 {
            let node = node.borrow();
            let cur = path + node.val as i64;
            let mut res = if cur == target { 1 } else { 0 };
            if let Some(left) = &node.left {
                res += dfs(left, cur, target);
            }
            if let Some(right) = &node.right {
                res += dfs(right, cur, target);
            }
            res
        }
        if let Some(node) = root {
            let left = node.borrow().left.clone();
            let right = node.borrow().right.clone();
            dfs(&node, 0, target_sum as i64)
                + Self::path_sum(left, target_sum)
                + Self::path_sum(right, target_sum)
        } else {
            0
        }
    }
}

// @lc code=end

fn main() -> Result<()> {
    let root: BinaryTree = deserialize(&read_line()?)?;
    let target_sum: i32 = deserialize(&read_line()?)?;
    let ans: i32 = Solution::path_sum(root.into(), target_sum).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
