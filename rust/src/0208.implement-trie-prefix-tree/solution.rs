// Created by woxQAQ at 2026/07/11 10:45
// leetgo: 1.4.17
// https://leetcode.cn/problems/implement-trie-prefix-tree/

use anyhow::Result;
use leetgo_rs::*;

// @lc code=begin
//
#[derive(Default)]
struct TrieNode {
    map: [Option<Box<TrieNode>>; 26],
    is_word: bool,
}

impl TrieNode {
    fn new() -> Self {
        Self {
            map: [const { None }; 26],
            is_word: false,
        }
    }
}

#[derive(Default)]
struct Trie {
    root: TrieNode,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Trie {
    fn new() -> Self {
        Self {
            root: TrieNode::new(),
        }
    }

    fn insert(&mut self, word: String) {
        let mut cur = &mut self.root;
        for c in word.bytes() {
            let c = (c - b'a') as usize;
            if cur.map[c].is_none() {
                cur.map[c] = Some(Box::new(TrieNode::new()));
            }
            cur = cur.map[c].as_mut().unwrap().as_mut();
        }
        cur.is_word = true;
    }

    fn search(&self, word: String) -> bool {
        let mut cur = &self.root;
        for c in word.bytes() {
            let c = (c - b'a') as usize;
            if cur.map[c].is_none() {
                return false;
            }
            cur = cur.map[c].as_ref().unwrap().as_ref();
        }
        cur.is_word
    }

    fn starts_with(&self, prefix: String) -> bool {
        let mut cur = &self.root;
        for c in prefix.bytes() {
            let c = (c - b'a') as usize;
            if cur.map[c].is_none() {
                return false;
            }
            cur = cur.map[c].as_ref().unwrap().as_ref();
        }
        true
    }
}

// @lc code=end

fn main() -> Result<()> {
    let ops: Vec<String> = deserialize(&read_line()?)?;
    let params = split_array(&read_line()?)?;
    let mut output = Vec::with_capacity(ops.len());
    output.push("null".to_string());

    #[allow(unused_mut)]
    let mut obj = Trie::new();

    for i in 1..ops.len() {
        match ops[i].as_str() {
            "insert" => {
                let method_params = split_array(&params[i])?;
                let word: String = deserialize(&method_params[0])?;
                obj.insert(word);
                output.push("null".to_string());
            }
            "search" => {
                let method_params = split_array(&params[i])?;
                let word: String = deserialize(&method_params[0])?;
                let ans: bool = obj.search(word).into();
                output.push(serialize(ans)?);
            }
            "startsWith" => {
                let method_params = split_array(&params[i])?;
                let prefix: String = deserialize(&method_params[0])?;
                let ans: bool = obj.starts_with(prefix).into();
                output.push(serialize(ans)?);
            }
            _ => panic!("unknown op"),
        }
    }

    println!("\noutput: {}", join_array(output));
    Ok(())
}
