// Created by woxQAQ at 2026/07/10 18:10
// leetgo: 1.4.17
// https://leetcode.cn/problems/merge-two-sorted-lists/

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
impl Solution {
    pub fn merge_two_lists(
        mut list1: Option<Box<ListNode>>,
        mut list2: Option<Box<ListNode>>,
    ) -> Option<Box<ListNode>> {
        let mut dummy = ListNode::new(0);
        let mut cur = &mut dummy;
        while let (Some(node1), Some(node2)) = (&list1, &list2) {
            if node1.val < node2.val {
                cur.next = list1.take();
                // 此处 list1 为 Some
                // cur.next = list1 也为 Some
                // 因此 cur = cur.next 也为 Some, ? 不会提前返回
                // 是为了处理 Option 的安全写法
                // 用 unwrap 也可以
                cur = cur.next.as_mut()?;
                list1 = cur.next.take();
            } else {
                cur.next = list2.take();
                cur = cur.next.as_mut()?;
                list2 = cur.next.take();
            }
        }
        cur.next = list1.or(list2);
        dummy.next
    }
}

// @lc code=end

fn main() -> Result<()> {
    let list1: LinkedList = deserialize(&read_line()?)?;
    let list2: LinkedList = deserialize(&read_line()?)?;
    let ans: LinkedList = Solution::merge_two_lists(list1.into(), list2.into()).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
