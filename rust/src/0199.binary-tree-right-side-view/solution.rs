// Created by woxQAQ at 2026/07/11 11:54
// leetgo: 1.4.17
// https://leetcode.cn/problems/binary-tree-right-side-view/

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
    pub fn right_side_view(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        match root {
            Some(root) => {
                let mut q = VecDeque::new();
                q.push_back(root);
                let mut res = vec![];
                while !q.is_empty() {
                    res.push(q.back().unwrap().borrow().val);
                    for _ in 0..q.len() {
                        let node = q.pop_front().unwrap();
                        let node = node.borrow();
                        if let Some(ref left) = node.left {
                            q.push_back(left.clone());
                        }
                        if let Some(ref right) = node.right {
                            q.push_back(right.clone());
                        }
                    }
                }
                res
            }
            None => vec![],
        }
    }
}

// @lc code=end

fn main() -> Result<()> {
    let root: BinaryTree = deserialize(&read_line()?)?;
    let ans: Vec<i32> = Solution::right_side_view(root.into()).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
