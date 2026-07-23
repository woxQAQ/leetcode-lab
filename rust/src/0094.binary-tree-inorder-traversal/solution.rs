// Created by woxQAQ at 2026/07/11 05:24
// leetgo: 1.4.17
// https://leetcode.cn/problems/binary-tree-inorder-traversal/

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
    pub fn inorder_traversal(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        let mut ans = vec![];
        let mut cur = root;
        // morris 遍历：线索二叉树，对非叶子节点建立前驱线索树。
        //
        // 对 Option<Rc> 进行 .clone 是为了克隆 Option 外壳
        while let Some(node) = cur.clone() {
            // borrow from RefCell to read fields of TreeNode
            let node_ref = node.borrow();
            match &node_ref.left {
                None => {
                    // 无左子树：访问当前节点，进入右子树
                    // 此时的右子树两种情况：真正的右子树或者是线索
                    ans.push(node_ref.val);
                    cur = node_ref.right.clone();
                }
                Some(left) => {
                    // 找左子树的最右节点（中序前驱）
                    //
                    // Rc::clone() 从 &Rc 中拿到独立的所有者
                    let mut pre = Rc::clone(left);
                    loop {
                        let pre_ref = pre.borrow();
                        match &pre_ref.right {
                            // 两种情况：
                            // 第一次访问：此时是没有线索的，在左子树中一直
                            // 找右节点即可
                            // 第二次访问：已建立线索，此时必然存在一个叶子节点
                            // 其右子树指向自身
                            Some(r) if !Rc::ptr_eq(r, &node) => {
                                // 此处的 r 是对 pre_ref.right 的一个引用
                                // 由于后续 pre_ref 会被丢弃，因此需要提前
                                // 将 r 变成独立的所有者
                                let r = Rc::clone(r);
                                // pre_ref 被绑定在 pre 上，而 pre 的值被覆盖
                                // 需要丢弃旧有的引用
                                drop(pre_ref);
                                pre = r;
                            }
                            _ => break,
                        }
                    }
                    // 根据前驱的右指针判断首次/二次到达
                    let mut pre_ref = pre.borrow_mut();
                    match pre_ref.right.is_none() {
                        true => {
                            // 首次：建立线索 → 进入左子树
                            pre_ref.right = Some(Rc::clone(&node));
                            cur = Some(Rc::clone(left));
                        }
                        false => {
                            // 二次：拆除线索 + 访问节点 → 进入右子树
                            pre_ref.right = None;
                            ans.push(node.borrow().val);
                            cur = node.borrow().right.clone();
                        }
                    }
                }
            }
        }
        ans
    }
}

// @lc code=end

fn main() -> Result<()> {
    let root: BinaryTree = deserialize(&read_line()?)?;
    let ans: Vec<i32> = Solution::inorder_traversal(root.into()).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
