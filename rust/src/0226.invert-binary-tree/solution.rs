// Created by woxQAQ at 2026/07/11 09:00
// leetgo: 1.4.17
// https://leetcode.cn/problems/invert-binary-tree/

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
    pub fn invert_tree(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        if let Some(node) = &root {
            let mut node = node.borrow_mut();
            let left = node.left.take();
            node.left = node.right.take();
            node.right = left;
            Self::invert_tree(node.left.clone());
            Self::invert_tree(node.right.clone());
        }
        root
    }
}

// @lc code=end

fn main() -> Result<()> {
    let root: BinaryTree = deserialize(&read_line()?)?;
    let ans: BinaryTree = Solution::invert_tree(root.into()).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
