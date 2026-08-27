// Created by woxQAQ at 2026/08/27 10:10
// leetgo: 1.4.17
// https://leetcode.cn/problems/reverse-linked-list/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin

// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
//
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
type Node = Option<Box<ListNode>>;
impl Solution {
    pub fn reverse_list(head: Node) -> Node {
        let mut prev = None;
        let mut cur = head;
        while let Some(mut node) = cur {
            cur = node.next.take();
            node.next = prev;
            prev = Some(node)
        }
        prev
    }
}

// @lc code=end

fn main() -> Result<()> {
    let head: LinkedList = deserialize(&read_line()?)?;
    let ans: LinkedList = Solution::reverse_list(head.into()).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
