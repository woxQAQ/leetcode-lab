// Created by woxQAQ at 2026/08/04 17:54
// leetgo: 1.4.17
// https://leetcode.cn/problems/sort-list/

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
    fn merge_lists(
        mut l1: Option<Box<ListNode>>,
        mut l2: Option<Box<ListNode>>,
    ) -> Option<Box<ListNode>> {
        let mut dummy = ListNode::new(0);
        let mut tail = &mut dummy;
        while let (Some(n1), Some(n2)) = (&l1, &l2) {
            if n1.val < n2.val {
                let mut node = l1.take().unwrap();
                l1 = node.next.take();
                tail.next = Some(node);
            } else {
                let mut node = l2.take().unwrap();
                l2 = node.next.take();
                tail.next = Some(node);
            }
            tail = tail.next.as_mut().unwrap();
        }
        tail.next = l1.or(l2);
        dummy.next
    }
    fn list_len(l: &Option<Box<ListNode>>) -> i32 {
        let mut len = 0;
        let mut cur = l;
        while let Some(n) = cur {
            len += 1;
            cur = &n.next;
        }
        len
    }
    fn split_list_by_step(
        mut head: Option<Box<ListNode>>,
        step: i32,
    ) -> (Option<Box<ListNode>>, Option<Box<ListNode>>) {
        if step <= 0 {
            return (None, head);
        }
        let mut cur = &mut head;
        for _ in 0..step - 1 {
            match cur {
                Some(node) if node.next.is_some() => cur = &mut node.next,
                _ => return (head, None),
            }
        }
        let rest = match cur {
            Some(node) => node.next.take(),
            None => None,
        };
        (head, rest)
    }
    fn split(mut head: Option<Box<ListNode>>) -> (Option<Box<ListNode>>, Option<Box<ListNode>>) {
        let mut len = 0;
        let mut cur = &head;
        while let Some(n) = cur {
            len += 1;
            cur = &n.next;
        }
        if len < 2 {
            return (head, None);
        }
        let half = len / 2;
        let mut cur = &mut head;
        for _ in 0..half - 1 {
            cur = &mut cur.as_mut().unwrap().next;
        }
        let right = cur.as_mut().unwrap().next.take();
        (head, right)
    }
    pub fn sort_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        match head {
            None => None,
            Some(_) if head.as_ref().unwrap().next.is_none() => head,
            Some(_) => {
                let (tail, right) = Self::split(head);
                let left = Self::sort_list(tail);
                let right = Self::sort_list(right);
                Self::merge_lists(left, right)
            }
        }
    }
    // pub fn sort_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
    //     let length = Self::list_len(&head);
    //     if length < 2 {
    //         return head;
    //     }

    //     let mut dummy = Box::new(ListNode { val: 0, next: head });
    //     let mut step = 1;
    //     while step < length {
    //         let mut remaining = dummy.next.take();
    //         let mut tail = &mut dummy;
    //         while remaining.is_some() {
    //             let (head1, rest) = Self::split_list_by_step(remaining, step);
    //             let (head2, rest) = Self::split_list_by_step(rest, step);
    //             remaining = rest;
    //             tail.next = Self::merge_lists(head1, head2);
    //             while tail.next.is_some() {
    //                 tail = tail.next.as_mut().unwrap();
    //             }
    //         }
    //         step *= 2;
    //     }
    //     dummy.next
    // }
}

// @lc code=end

fn main() -> Result<()> {
    let head: LinkedList = deserialize(&read_line()?)?;
    let ans: LinkedList = Solution::sort_list(head.into()).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
