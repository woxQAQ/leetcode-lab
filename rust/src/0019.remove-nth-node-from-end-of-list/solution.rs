// Created by woxQAQ at 2026/08/27 16:28
// leetgo: 1.4.17
// https://leetcode.cn/problems/remove-nth-node-from-end-of-list/

use std::{cell::RefCell, rc::Rc};

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

type Link = Option<Rc<RefCell<Node>>>;

struct Node {
    val: i32,
    next: Link,
}

pub fn remove_nth_from_end(head: Link, n: i32) -> Link {
    let dummy = Rc::new(RefCell::new(Node { val: 0, next: head }));
    let mut fast = Some(Rc::clone(&dummy));
    let mut slow = Rc::clone(&dummy);
    for _ in 0..n {
        fast = fast.and_then(|node| node.borrow().next.clone());
    }
    while let Some(node) = fast {
        fast = node.borrow().next.clone();
        let nxt = slow.borrow().next.clone().unwrap();
        slow = nxt;
    }
    // target = slow.next.next
    let a = slow.borrow().next.as_ref().unwrap();
    let target = slow
        .borrow() // Ref<_, Node>
        .next // Option<Rc> from RefCell
        // 如果直接拿 Rc 的话会导致Refcell里的数据被 move
        // 导致内存不安全, 因此需要
        // 拿到里面数据的引用
        // 这里也可以clone拿owned的引用但没必要
        .as_ref() // Option<&Rc>
        .unwrap() // &Rc
        .borrow() // Ref<_, Node>
        .next // Option<Rc>
        // target 被赋值给 slow.next
        // 需要一个 owned 的 ref，因此 clone Rc 使引用计数+1
        .clone();
    slow.borrow_mut().next = target;
    dummy.borrow().next.clone()
}

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
    pub fn remove_nth_from_end(head: Option<Box<ListNode>>, n: i32) -> Option<Box<ListNode>> {
        let mut dummy = Some(Box::new(ListNode { val: 0, next: head }));
        let mut slow = &mut dummy;
        let mut fast = &mut dummy;
        for _ in 0..n {
            if let Some(node) = fast {
                fast = &mut node.next;
            } else {
                return None;
            }
        }
        while fast.is_some() {
            fast = fast.as_ref().unw
        }
    }
}

// @lc code=end

fn main() -> Result<()> {
    let head: LinkedList = deserialize(&read_line()?)?;
    let n: i32 = deserialize(&read_line()?)?;
    let ans: LinkedList = Solution::remove_nth_from_end(head.into(), n).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
