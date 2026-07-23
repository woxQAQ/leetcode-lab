// Created by woxQAQ at 2026/07/10 17:08
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
impl Solution {
    // 206. 反转链表
    fn reverse_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut pre = None;
        let mut cur = head;
        while let Some(mut node) = cur {
            let nxt = node.next;
            node.next = pre;
            pre = Some(node);
            cur = nxt;
        }
        pre
    }

    pub fn is_palindrome(mut head: Option<Box<ListNode>>) -> bool {
        // 1. 计算链表长度
        let mut len = 0;
        let mut cur = &head;
        while let Some(node) = cur {
            len += 1;
            cur = &node.next;
        }
        if len <= 1 {
            return true;
        }

        // 2. 移动到分割点前一个节点
        let mut cur = &mut head;
        for _ in 0..len / 2 - 1 {
            cur = &mut cur.as_mut().unwrap().next;
        }

        // 3. 切出后半段（奇数长度时跳过中间元素）
        let cur_node = cur.as_mut().unwrap();
        let second = if len % 2 == 0 {
            cur_node.next.take()
        } else {
            cur_node.next.take().and_then(|mid| mid.next)
        };

        // 4. 反转后半段，然后逐节点比较
        let mut second = Self::reverse_list(second);
        while head.is_some() && second.is_some() {
            let n1 = head.take().unwrap();
            let n2 = second.take().unwrap();
            if n1.val != n2.val {
                return false;
            }
            head = n1.next;
            second = n2.next;
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
