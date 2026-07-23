// Created by woxQAQ at 2026/07/11 12:29
// leetgo: 1.4.17
// https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/

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
    pub fn flatten(root: &Option<Rc<RefCell<TreeNode>>>) {
        fn dfs(node: &Option<Rc<RefCell<TreeNode>>>, head: &mut Option<Rc<RefCell<TreeNode>>>) {
            if let Some(x) = node {
                let mut x = x.borrow_mut();
                dfs(&x.right, head);
                dfs(&x.left, head);
                x.left = None;
                x.right = head.take();
                *head = node.clone();
            }
        }

        dfs(root, &mut None);
    }
}

// @lc code=end

fn main() -> Result<()> {
    let root: BinaryTree = deserialize(&read_line()?)?;
    let root: Option<Rc<RefCell<TreeNode>>> = root.into();
    Solution::flatten(&root);
    let ans: BinaryTree = root.into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
