// Created by woxQAQ at 2026/08/27 10:17
// leetgo: 1.4.17
// https://leetcode.cn/problems/palindrome-linked-list/

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
    pub fn is_palindrome(head: Node) -> bool {
        let mut len = 0;
        let mut cur = &head;
        while let Some(node) = cur {
            len = len + 1;
            cur = &node.next;
        }
        // 拆分链表同时反转
        // 1 -> 2 -> 3 -> 2 -> 1
        // 2 -> 1 -> None + 3 -> 2 -> 1
        let mut rev: Node = None;
        let mut cur = head;
        for _ in 0..len / 2 {
            // 逻辑上保证 unwrap 一定不会有问题
            let mut node = cur.unwrap();
            cur = node.next.take();
            node.next = rev;
            rev = Some(node);
        }
        // 奇数跳过中间节点
        if len % 2 == 1 {
            cur = cur.unwrap().next;
        }
        // 逐个对比
        let mut a = rev;
        let mut b = cur;
        while let (Some(x), Some(y)) = (a, b) {
            if x.val != y.val {
                return false;
            }
            a = x.next;
            b = y.next;
        }
        true
    }
}

// @lc code=end

fn main() -> Result<()> {
    let head: LinkedList = deserialize(&read_line()?)?;
    let ans: bool = Solution::is_palindrome(head.into()).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
