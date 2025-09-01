#!/usr/bin/env nu

# Load environment variables from .env file if it exists
def load-env [] {
    let env_file = ".env"
    if ($env_file | path exists) {
        let env_content = (open $env_file | lines)
        mut env_vars = {}
        for line in $env_content {
            let line = ($line | str trim)
            if ($line != "") and not ($line | str starts-with "#") {
                let parts = ($line | split row "=")
                if ($parts | length) == 2 {
                    let key = ($parts | get 0 | str trim)
                    let value = ($parts | get 1 | str trim)
                    # Remove quotes if present
                    let value = if ($value | str starts-with "'") and ($value | str ends-with "'") {
                        $value | str substring 1..-2
                    } else if ($value | str starts-with '"') and ($value | str ends-with '"') {
                        $value | str substring 1..-2
                    } else {
                        $value
                    }
                    # Add to environment variables
                    $env_vars = ($env_vars | merge { $key: $value })
                }
            }
        }
        # Load all environment variables at once
        if ($env_vars | length) > 0 {
            load-env $env_vars
        }
    }
}

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

def main [tag?: int, --all, --output-dir: string = "dist"] {
    # Load environment variables
    load-env
    
    # Get token from environment variable
    let token = ($env.CODETOP_TOKEN? | default "")
    if $token == "" {
        print "Error: CODETOP_TOKEN environment variable is not set"
        print "Please set it in your environment or in a .env file:"
        print "CODETOP_TOKEN=your_token_here"
        exit 1
    }
    # 处理 --all flag
    if $all {
        print "正在获取所有标签的题目列表..."
        process-all-tags $output_dir $token
        return
    }

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

    # 处理单个标签
    process-single-tag $selected_tag $output_dir $token
}

# 处理单个标签的函数
def process-single-tag [tag: int, output_dir?: string, token: string] {
    let page = 1
    let url = $"https://codetop.cc/api/questions/?page=($page)&search=&ordering=-frequency&leetcode__tags=($tag)"
    mut page_count = 0
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
description: leetcode problem from codetop
label: ($tag_label)
---
($problem_meta | each { |item| $'- [ ] ($item.leetcode.question_id).($item.leetcode.title)' } | str join (char nl))"

    # 如果指定了输出目录，保存到文件
    if $output_dir != null {
        let tag_name = ($tag_label | str downcase | str replace " " "-")
        let filename = $"($output_dir)/($tag_name).md"
        ensure-output-dir $output_dir
        $template | save --force $filename
        print $"题目列表已保存到: ($filename)"
    } else {
        $template
    }
}

# 处理所有标签的函数
def process-all-tags [output_dir?: string, token: string] {
    # 确定输出目录
    let final_output_dir = if $output_dir != null {
        $output_dir
    } else {
        "dist"
    }

    ensure-output-dir $final_output_dir

    print $"输出目录: ($final_output_dir)"

    # 遍历所有标签
    let tag_keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 31, 35]
    for key in $tag_keys {
        let value = ($tag_to_label | get $"($key)")
        print $"Processing: ($value) - tag ($key)"
        process-single-tag $key $final_output_dir $token
    }

    print "所有标签的题目列表处理完成!"
}

# 确保输出目录存在的函数
def ensure-output-dir [dir: string] {
    if not ($dir | path exists) {
        mkdir $dir
        print $"创建目录: ($dir)"
    }
}
