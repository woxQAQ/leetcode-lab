#!/usr/bin/env nu

const tag_to_label = {
    "1": "Hash Table",
    "2": "Array",
    "3": "Sort",
    "4": "Dynamic Programming",
    "5": "Math",
    "6": "Sliding Window",
    "7": "String",
    "8": "Double Pointer",
    "9": "Bit Manipulation",
    "10": "Divide and Conquer",
    "11": "Heap",
    "12": "Queue",
    "13": "Binary Search",
    "14": "DFS",
    "15": "BFS",
    "16": "Union Find Set",
    "17": "Stack",
    "18": "Design",
    "19": "Trie",
    "20": "Memoization",
    "21": "Tree",
    "22": "BST",
    "23": "Recurison",
    "24": "Linked List",
    "25": "Geometry",
    "26": "BackTracking",
    "27": "Graph",
    "28": "Greedy",
    "31": "TopoSort",
    "35": "Random",
}

def main [tag?: int] {
    let page = 1

    # 如果没有提供tag参数，则显示交互式选择
    mut selected_tag = $tag
    if $selected_tag == null {
        # 创建标签选项列表
        let tag_options = ($tag_to_label | items { |key, value| $"($key). ($value)" })

        # 使用input list进行交互式选择
        let selected_option = ($tag_options | input list "请选择标签：")

        # 解析选择的标签编号
        $selected_tag = ($selected_option | split row ". " | first | into int)
    }

    # 验证选择的标签是否有效
    if ($tag_to_label | get --optional $"($selected_tag)") == null {
        print $"错误：无效的标签编号 ($selected_tag)"
        print "有效的标签编号有："
        $tag_to_label | items { |key, value| print $"($key). ($value)" }
        print ""
        print "查看文件开头的注释获取完整的标签列表"
        exit 1
    }

    let tag = $selected_tag
    let url = $"https://codetop.cc/api/questions/?page=($page)&search=&ordering=-frequency&leetcode__tags=($tag)"
    mut page_count = 0
    let token = "0012e89acd6812aa9f3ab8807429a36fa996049b"
    let response = http get $url -H {Authorization: $'Token ($token)'}
    let all_count = $response.count
    $page_count += $response.list | length
    mut problem_meta = ($response.list)
    while $page_count < $all_count {
        let next_page = $page + 1
        let next_url = $"https://codetop.cc/api/questions/?page=($next_page)&search=&ordering=-frequency&leetcode__tags=($tag)"
        let next_response = http get $next_url -H {Authorization: $'Token ($token)'}
        $page_count += $next_response.list | length
        $problem_meta = ($problem_meta | append $next_response.list)
    }
    let tag_label = $tag_to_label | get $"($tag)"

    let template = $"---
description: leetcode problem from codetop - ($tag_label)
---
($problem_meta | each { |item| $'- [ ] ($item.id).($item.leetcode.title)' } | str join (char nl))"

    $template
}
