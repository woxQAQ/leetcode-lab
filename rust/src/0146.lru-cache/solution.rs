// Created by woxQAQ at 2026/08/04 17:14
// leetgo: 1.4.17
// https://leetcode.cn/problems/lru-cache/

use anyhow::Result;
use leetgo_rs::*;

// @lc code=begin

use std::{
    cell::RefCell,
    collections::HashMap,
    rc::{Rc, Weak},
};
#[derive(Default)]
struct Node {
    key: i32,
    value: i32,
    prev: Option<Weak<RefCell<Node>>>,
    next: Option<Rc<RefCell<Node>>>,
}

impl Node {
    pub fn new(key: i32, value: i32) -> Rc<RefCell<Node>> {
        Rc::new(RefCell::new(Node {
            key,
            value,
            prev: None,
            next: None,
        }))
    }
}

struct LRUCache {
    cap: usize,
    node_store: HashMap<i32, Rc<RefCell<Node>>>,
    head: Rc<RefCell<Node>>,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl LRUCache {
    fn new(capacity: i32) -> Self {
        let head = Node::new(0, 0);
        head.borrow_mut().prev = Some(Rc::downgrade(&head));
        head.borrow_mut().next = Some(head.clone());
        LRUCache {
            cap: capacity as usize,
            node_store: HashMap::new(),
            head,
        }
    }

    fn get_node(&self, key: i32) -> Option<Rc<RefCell<Node>>> {
        if let Some(node) = self.node_store.get(&key) {
            let node = node.clone();
            Self::remove(node.clone());
            self.push_front(node.clone());
            return Some(node);
        }
        None
    }

    fn get(&self, key: i32) -> i32 {
        if let Some(node) = self.get_node(key) {
            node.borrow_mut().value
        } else {
            -1
        }
    }

    fn put(&mut self, key: i32, value: i32) {
        if let Some(node) = self.get_node(key) {
            node.borrow_mut().value = value;
            return;
        }
        let node = Node::new(key, value);
        self.push_front(node.clone());
        self.node_store.insert(key, node);
        if self.node_store.len() > self.cap {
            let back_node = self
                .head
                .borrow_mut()
                .prev
                .as_ref()
                .unwrap()
                .upgrade()
                .unwrap();
            self.node_store.remove(&back_node.borrow().key);
            Self::remove(back_node);
        }
    }

    fn push_front(&self, node: Rc<RefCell<Node>>) {
        let next = self.head.borrow_mut().next.take().unwrap();
        next.borrow_mut().prev = Some(Rc::downgrade(&node));
        node.borrow_mut().next = Some(next);
        node.borrow_mut().prev = Some(Rc::downgrade(&self.head));
        self.head.borrow_mut().next = Some(node);
    }

    fn remove(x: Rc<RefCell<Node>>) {
        let prev = x.borrow_mut().prev.take().unwrap().upgrade().unwrap();
        let next = x.borrow_mut().next.take().unwrap();
        next.borrow_mut().prev = Some(Rc::downgrade(&prev));
        prev.borrow_mut().next = Some(next);
    }
}

// @lc code=end

fn main() -> Result<()> {
    let ops: Vec<String> = deserialize(&read_line()?)?;
    let params = split_array(&read_line()?)?;
    let mut output = Vec::with_capacity(ops.len());
    output.push("null".to_string());

    let constructor_params = split_array(&params[0])?;
    let capacity: i32 = deserialize(&constructor_params[0])?;
    #[allow(unused_mut)]
    let mut obj = LRUCache::new(capacity);

    for i in 1..ops.len() {
        match ops[i].as_str() {
            "get" => {
                let method_params = split_array(&params[i])?;
                let key: i32 = deserialize(&method_params[0])?;
                let ans: i32 = obj.get(key).into();
                output.push(serialize(ans)?);
            }
            "put" => {
                let method_params = split_array(&params[i])?;
                let key: i32 = deserialize(&method_params[0])?;
                let value: i32 = deserialize(&method_params[1])?;
                obj.put(key, value);
                output.push("null".to_string());
            }
            _ => panic!("unknown op"),
        }
    }

    println!("\noutput: {}", join_array(output));
    Ok(())
}
