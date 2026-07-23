// Created by woxQAQ at 2026/07/11 19:02
// leetgo: 1.4.17
// https://leetcode.cn/problems/binary-tree-maximum-path-sum/

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
    pub fn max_path_sum(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        fn dfs(root: Option<Rc<RefCell<TreeNode>>>, res: &mut i32) -> i32 {
            if let Some(root) = root {
                let root = root.borrow();
                let l = dfs(root.left.clone(), res);
                let r = dfs(root.right.clone(), res);
                *res = (*res).max(l + r + root.val);
                return 0.max(l.max(r) + root.val);
            }
            0
        }
        let mut res = i32::MIN;
        dfs(root, &mut res);
        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let root: BinaryTree = deserialize(&read_line()?)?;
    let ans: i32 = Solution::max_path_sum(root.into()).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
