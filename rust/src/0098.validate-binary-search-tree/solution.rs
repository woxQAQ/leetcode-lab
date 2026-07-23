// Created by woxQAQ at 2026/07/11 10:09
// leetgo: 1.4.17
// https://leetcode.cn/problems/validate-binary-search-tree/

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
    pub fn is_valid_bst(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        fn dfs(node: &Option<Rc<RefCell<TreeNode>>>, left: i64, right: i64) -> bool {
            match node {
                Some(node) => {
                    let node = node.borrow();
                    let x = node.val as i64;
                    left < x && x < right && dfs(&node.left, left, x) && dfs(&node.right, x, right)
                }
                None => true,
            }
        }
        dfs(&root, i64::MIN, i64::MAX)
    }
}

// @lc code=end

fn main() -> Result<()> {
    let root: BinaryTree = deserialize(&read_line()?)?;
    let ans: bool = Solution::is_valid_bst(root.into()).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
