// Created by woxQAQ at 2026/07/11 09:44
// leetgo: 1.4.17
// https://leetcode.cn/problems/binary-tree-level-order-traversal/

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
use std::collections::VecDeque;
use std::rc::Rc;
impl Solution {
    pub fn level_order(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<i32>> {
        let mut q = VecDeque::new();
        if let Some(node) = root {
            q.push_back(node);
        }
        let mut res = vec![];
        while !q.is_empty() {
            let mut level = vec![];
            for _ in 0..q.len() {
                let node = q.pop_front().unwrap();
                let node = node.borrow();
                level.push(node.val);
                if let Some(left) = &node.left {
                    q.push_back(left.clone());
                }
                if let Some(right) = &node.right {
                    q.push_back(right.clone());
                }
            }
            res.push(level);
        }
        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let root: BinaryTree = deserialize(&read_line()?)?;
    let ans: Vec<Vec<i32>> = Solution::level_order(root.into()).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
