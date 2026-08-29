// Created by woxQAQ at 2026/08/27 10:17
// leetgo: 1.4.17
// https://leetcode.cn/problems/linked-list-cycle-ii/
// Warning: this is a manual question, the generated test code may be incorrect.
//
// LeetCode 官方没有本题的 Rust 模板：`Option<Box<ListNode>>` 的独占所有权
// 表达不了环。这里用 Rc<RefCell<ListNode>> 自定义节点：
// 前向边用 Rc（所有权边，构成无环骨架），回边用 Weak（关系边，不拥有），
// 所有权无环 ⇒ 没有循环引用 ⇒ 自动释放，无需手动断环。

use std::cell::RefCell;
use std::rc::{Rc, Weak};

use anyhow::Result;
use leetgo_rs::{deserialize, read_line};

struct Solution;

// @lc code=begin

type Link = Option<Rc<RefCell<ListNode>>>;

struct ListNode {
    val: i32,
    next: Link,                            // 所有权边：普通后继（强引用）
    back: Option<Weak<RefCell<ListNode>>>, // 关系边：尾节点的回边（弱引用）
}

impl ListNode {
    fn new(val: i32) -> Self {
        ListNode {
            val,
            next: None,
            back: None,
        }
    }
}

impl Solution {
    pub fn detect_cycle(head: Link) -> Link {
        // 后继 = 优先走前向边，尾节点则走回边
        fn succ(node: &Link) -> Link {
            let borrowed = node.as_ref()?.borrow();
            borrowed
                .next
                .clone()
                .or_else(|| borrowed.back.as_ref().and_then(Weak::upgrade))
        }

        // Floyd 判圈：快慢指针相遇
        let mut slow = head.clone();
        let mut fast = head.clone();
        loop {
            fast = succ(&succ(&fast));
            slow = succ(&slow);
            match (&slow, &fast) {
                (Some(s), Some(f)) if Rc::ptr_eq(s, f) => break,
                (Some(_), Some(_)) => {}
                _ => return None, // 任一方走到尽头，无环
            }
        }
        // 一个指针回到起点，与 slow 同步走，相遇处即入口
        let mut p = head;
        while !Rc::ptr_eq(p.as_ref().unwrap(), slow.as_ref().unwrap()) {
            p = succ(&p);
            slow = succ(&slow);
        }
        p
    }
}

// @lc code=end

/// 用值数组构造链表，pos >= 0 时尾节点的 back 指回第 pos 个节点成环。
fn cyclic_list(vals: &[i32], pos: i32) -> Link {
    let nodes: Vec<_> = vals
        .iter()
        .map(|&v| Rc::new(RefCell::new(ListNode::new(v))))
        .collect();
    for (i, node) in nodes.iter().enumerate() {
        let mut n = node.borrow_mut();
        if i + 1 < nodes.len() {
            n.next = Some(nodes[i + 1].clone()); // 强引用向前：所有权边
        } else if pos >= 0 {
            n.back = Some(Rc::downgrade(&nodes[pos as usize])); // 弱引用回边：关系边
        }
    }
    nodes.first().cloned()
}

fn main() -> Result<()> {
    let vals: Vec<i32> = deserialize(&read_line()?)?;
    let pos: i32 = deserialize(&read_line()?)?;

    match Solution::detect_cycle(cyclic_list(&vals, pos)) {
        Some(entrance) => println!("\noutput: {}", entrance.borrow().val),
        None => println!("\noutput: null"),
    }
    // 所有权无环，离开作用域自动释放，不需要任何手动清理
    Ok(())
}
