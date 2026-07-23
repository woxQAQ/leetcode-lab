// Created by woxQAQ at 2026/07/11 13:06
// leetgo: 1.4.17
// https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

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
    pub fn build_tree(preorder: Vec<i32>, inorder: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
        if preorder.is_empty() {
            return None;
        }
        let left_size = inorder.iter().position(|&x| x == preorder[0]).unwrap();
        let pre1 = preorder[1..1 + left_size].to_vec();
        let pre2 = preorder[1 + left_size..].to_vec();
        let in1 = inorder[..left_size].to_vec();
        let in2 = inorder[1 + left_size..].to_vec();
        let left = Self::build_tree(pre1, in1);
        let right = Self::build_tree(pre2, in2);
        Some(Rc::new(RefCell::new(TreeNode {
            val: preorder[0],
            left: left,
            right: right,
        })))
    }
}

// @lc code=end

fn main() -> Result<()> {
    let preorder: Vec<i32> = deserialize(&read_line()?)?;
    let inorder: Vec<i32> = deserialize(&read_line()?)?;
    let ans: BinaryTree = Solution::build_tree(preorder, inorder).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
