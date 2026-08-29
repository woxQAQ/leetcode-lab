// Created by woxQAQ at 2026/08/27 15:58
// leetgo: 1.4.17
// https://leetcode.cn/problems/add-two-numbers/

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
    pub fn add_two_numbers(
        l1: Option<Box<ListNode>>,
        l2: Option<Box<ListNode>>,
    ) -> Option<Box<ListNode>> {
        let mut l1 = l1;
        let mut l2 = l2;
        let mut carry = 0;
        let mut dummy = ListNode::new(0);
        let mut cur = &mut dummy;
        while l1.is_some() || l2.is_some() || carry > 0 {
            let mut sum = carry;
            if let Some(n1) = l1 {
                sum += n1.val;
                l1 = n1.next;
            }

            if let Some(n2) = l2 {
                sum += n2.val;
                l2 = n2.next;
            }
            cur.next = Some(Box::new(ListNode::new(sum % 10)));
            carry = sum / 10;
            cur = cur.next.as_mut()?;
        }
        dummy.next
    }
}

// @lc code=end

fn main() -> Result<()> {
    let l1: LinkedList = deserialize(&read_line()?)?;
    let l2: LinkedList = deserialize(&read_line()?)?;
    let ans: LinkedList = Solution::add_two_numbers(l1.into(), l2.into()).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
