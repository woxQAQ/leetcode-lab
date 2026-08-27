// Created by woxQAQ at 2026/08/27 10:17
// leetgo: 1.4.17
// https://leetcode.cn/problems/linked-list-cycle-ii/
// Warning: this is a manual question, the generated test code may be incorrect.
//
// LeetCode 官方没有本题的 Rust 模板：`Option<Box<ListNode>>` 的独占所有权
// 表达不了环。这里改用 Rc<RefCell<ListNode>> 自定义节点，本地可真实成环。

use std::cell::RefCell;
use std::rc::Rc;

use anyhow::Result;
use leetgo_rs::{deserialize, read_line};

struct Solution;

// @lc code=begin

type Link = Option<Rc<RefCell<ListNode>>>;

struct ListNode {
    val: i32,
    next: Link,
}

impl ListNode {
    fn new(val: i32) -> Self {
        ListNode { val, next: None }
    }
}

impl Solution {
    pub fn detect_cycle(head: Link) -> Link {
        fn next(node: &Link) -> Link {
            node.as_ref()?.borrow().next.clone()
        }

        // Floyd 判圈：快慢指针相遇
        let mut slow = head.clone();
        let mut fast = head.clone();
        loop {
            fast = next(&next(&fast));
            slow = next(&slow);
            match (&slow, &fast) {
                (Some(s), Some(f)) if Rc::ptr_eq(s, f) => break,
                (Some(_), Some(_)) => {}
                _ => return None, // 任一方走到尽头，无环
            }
        }
        // 一个指针回到起点，与 slow 同步走，相遇处即入口
        let mut p = head;
        while !Rc::ptr_eq(p.as_ref().unwrap(), slow.as_ref().unwrap()) {
            p = next(&p);
            slow = next(&slow);
        }
        p
    }
}

// @lc code=end

/// 用值数组构造链表，pos >= 0 时尾节点指回第 pos 个节点成环。
/// 返回 (head, 所有节点)，调用方用完需要自行断环（见 main）。
fn cyclic_list(vals: &[i32], pos: i32) -> (Link, Vec<Rc<RefCell<ListNode>>>) {
    let nodes: Vec<_> = vals
        .iter()
        .map(|&v| Rc::new(RefCell::new(ListNode::new(v))))
        .collect();
    for (i, node) in nodes.iter().enumerate() {
        node.borrow_mut().next = if i + 1 < nodes.len() {
            Some(nodes[i + 1].clone())
        } else if pos >= 0 {
            Some(nodes[pos as usize].clone()) // 回边：强引用成环
        } else {
            None
        };
    }
    (nodes.first().cloned(), nodes)
}

fn main() -> Result<()> {
    let vals: Vec<i32> = deserialize(&read_line()?)?;
    let pos: i32 = deserialize(&read_line()?)?;
    let (head, nodes) = cyclic_list(&vals, pos);

    match Solution::detect_cycle(head) {
        Some(entrance) => println!("\noutput: {}", entrance.borrow().val),
        None => println!("\noutput: null"),
    }

    // Rc 强引用成环会导致引用计数永远不归零（内存泄漏），
    // 进程短命无所谓；要干净释放就把尾节点的回边断开：
    if let Some(tail) = nodes.last() {
        tail.borrow_mut().next = None;
    }
    Ok(())
}
