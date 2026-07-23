// Created by woxQAQ at 2026/07/11 09:36
// leetgo: 1.4.17
// https://leetcode.cn/problems/diameter-of-binary-tree/

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
    pub fn diameter_of_binary_tree(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut res = 0;
        fn dfs(p: &Option<Rc<RefCell<TreeNode>>>, res: &mut i32) -> i32 {
            if let Some(p) = p {
                let p = p.borrow();
                let l = dfs(&p.left, res) + 1;
                let r = dfs(&p.right, res) + 1;
                *res = (*res).max(l + r);
                return l.max(r);
            }
            -1
        }
        dfs(&root, &mut res);
        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let root: BinaryTree = deserialize(&read_line()?)?;
    let ans: i32 = Solution::diameter_of_binary_tree(root.into()).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
