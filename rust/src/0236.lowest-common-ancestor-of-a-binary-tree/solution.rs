// Created by woxQAQ at 2026/07/11 17:55
// leetgo: 1.4.17
// https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/

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
    pub fn lowest_common_ancestor(
        root: Option<Rc<RefCell<TreeNode>>>,
        p: Option<Rc<RefCell<TreeNode>>>,
        q: Option<Rc<RefCell<TreeNode>>>,
    ) -> Option<Rc<RefCell<TreeNode>>> {
        let root = root?;
        if p.as_ref().map_or(false, |p| Rc::ptr_eq(&root, p))
            || q.as_ref().map_or(false, |q| Rc::ptr_eq(&root, q))
        {
            return Some(root);
        }
        let node = root.borrow();
        let l = Self::lowest_common_ancestor(node.left.clone(), p.clone(), q.clone());
        let r = Self::lowest_common_ancestor(node.right.clone(), p, q);
        drop(node);
        if l.is_some() && r.is_some() {
            return Some(root);
        }
        l.or(r)
    }
}

// @lc code=end

// Warning: this is a manual question, the generated test code may be incorrect.
fn main() -> Result<()> {
    let root: BinaryTree = deserialize(&read_line()?)?;
    let p_val: i32 = deserialize(&read_line()?)?;
    let q_val: i32 = deserialize(&read_line()?)?;

    fn find_node(root: &Option<Rc<RefCell<TreeNode>>>, val: i32) -> Option<Rc<RefCell<TreeNode>>> {
        root.as_ref().and_then(|root| {
            let node = root.borrow();
            if node.val == val {
                return Some(root.clone());
            }
            find_node(&node.left, val).or_else(|| find_node(&node.right, val))
        })
    }

    let root: Option<Rc<RefCell<TreeNode>>> = root.into();
    let p = find_node(&root, p_val);
    let q = find_node(&root, q_val);
    let ans: BinaryTree = Solution::lowest_common_ancestor(root, p, q).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
