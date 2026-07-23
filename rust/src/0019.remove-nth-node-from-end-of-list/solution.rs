// Created by woxQAQ at 2026/07/10 18:30
// leetgo: 1.4.17
// https://leetcode.cn/problems/remove-nth-node-from-end-of-list/

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
    /// safe 写法：数长度 + 单指针遍历，两趟 O(n)，无 unsafe
    pub fn remove_nth_from_end(head: Option<Box<ListNode>>, n: i32) -> Option<Box<ListNode>> {
        // 1. 计算链表长度
        let mut len = 0;
        let mut cur = &head;
        while let Some(node) = cur {
            len += 1;
            cur = &node.next;
        }

        // 2. 走到待删节点的前驱
        let mut dummy = Box::new(ListNode { val: 0, next: head });
        let mut cur = &mut *dummy;
        for _ in 0..len - n {
            cur = cur.next.as_mut().unwrap();
        }

        // 3. 跳过目标节点
        if let Some(target) = cur.next.take() {
            cur.next = target.next;
        }

        dummy.next
    }

    /// unsafe 写法：经典快慢指针，一趟 O(n)
    /// 原理：fast 指针先走 n 步，然后 slow 和 fast 同步前进，fast 到末尾时 slow 正好在待删节点的前驱
    pub fn remove_nth_from_end_fast(head: Option<Box<ListNode>>, n: i32) -> Option<Box<ListNode>> {
        let mut dummy = Box::new(ListNode { val: 0, next: head });

        // fast: 裸指针，只读遍历
        let mut fast: *const ListNode = &*dummy;
        for _ in 0..=n {
            // SAFETY: n <= 链表长度（题目保证），next 指针非空
            fast = unsafe { (*fast).next.as_deref()? as *const ListNode };
        }

        // slow: 可变引用，从 dummy 出发
        let mut slow: &mut ListNode = &mut *dummy;
        while !fast.is_null() {
            slow = slow.next.as_mut().unwrap();
            // SAFETY: 与 slow 同步前进，不会悬垂
            fast = unsafe { (*fast).next.as_ref() }
                .map(|n| &**n as *const ListNode)
                .unwrap_or(std::ptr::null());
        }

        // 此时 slow 指向待删节点的前驱
        if let Some(target) = slow.next.take() {
            slow.next = target.next;
        }

        dummy.next
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
