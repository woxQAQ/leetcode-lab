// Created by woxQAQ at 2026/07/11 10:26
// leetgo: 1.4.17
// https://leetcode.cn/problems/kth-smallest-element-in-a-bst/

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
    pub fn kth_smallest(root: Option<Rc<RefCell<TreeNode>>>, mut k: i32) -> i32 {
        fn dfs(node: Option<Rc<RefCell<TreeNode>>>, k: &mut i32, ans: &mut i32) {
            if node.is_none() || *k <= 0 {
                return;
            }
            if let Some(node) = node {
                let node = node.borrow();
                dfs(node.left.clone(), k, ans);
                *k -= 1;
                if *k == 0 {
                    *ans = node.val;
                }
                dfs(node.right.clone(), k, ans)
            }
        }
        let mut ans = 0;
        dfs(root, &mut k, &mut ans);
        ans
    }
}

// @lc code=end

fn main() -> Result<()> {
    let root: BinaryTree = deserialize(&read_line()?)?;
    let k: i32 = deserialize(&read_line()?)?;
    let ans: i32 = Solution::kth_smallest(root.into(), k).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
