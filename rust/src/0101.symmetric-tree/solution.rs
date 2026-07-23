// Created by woxQAQ at 2026/07/11 09:28
// leetgo: 1.4.17
// https://leetcode.cn/problems/symmetric-tree/

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
    pub fn is_symmetric(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        fn is_same_tree(
            p: &Option<Rc<RefCell<TreeNode>>>,
            q: &Option<Rc<RefCell<TreeNode>>>,
        ) -> bool {
            match (p, q) {
                (Some(p), Some(q)) => {
                    let p = p.borrow();
                    let q = q.borrow();
                    p.val == q.val
                        && is_same_tree(&p.left, &q.right)
                        && is_same_tree(&p.right, &q.left)
                }
                (None, None) => true,
                _ => false,
            }
        }
        let binding = root.unwrap();
        let root = binding.borrow();
        is_same_tree(&root.left, &root.right)
    }
}

// @lc code=end

fn main() -> Result<()> {
    let root: BinaryTree = deserialize(&read_line()?)?;
    let ans: bool = Solution::is_symmetric(root.into()).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
