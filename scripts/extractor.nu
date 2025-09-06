#!/usr/bin/env nu
# an nushell port of extractor

def main [] {
    let openai_base_url = ($env.OPENAI_BASE_URL? | default "")
    let openai_api_key = ($env.OPENAI_API_KEY? | default "")
    let openai_model = ($env.OPENAI_MODEL? | default "")

    if $openai_base_url == "" {
        print "Error: OPENAI_BASE_URL environment variable is not set"
        exit 1
    }

    if $openai_api_key == "" {
        print "Error: OPENAI_API_KEY environment variable is not set"
        exit 1
    }

    if $openai_model == "" {
        print "Error: OPENAI_MODEL environment variable is not set"
        exit 1
    }

    let datasource = ($nu.args | get 0? | default "stdin")
    let output = ($nu.args | get 1? | default "output.md")
    let timeout = ($nu.args | get 2? | default 30 | into int)

    let system_prompt = "你是一个文本处理高手，你擅长在长文本中提取出符合任务要求的内容。请你在 <text></text> 包裹的文本中完成下列任务

1. 这是一份 LeetCode 题单，请你将其中特征为 ${题号}. ${题名} 的字符串按照顺序规范化输出到一份markdown文档中
2. 忽略含有后缀 (会员题) 的题目
3. 忽略题名后的数字和一些提示
4. 保留原始文档对于每个专题的提示，保留原始文档的拓扑结构，转化为标准的markdown语法

规范化的规则是为题目增加 TODO 标识

比如，0001. 两数之和，需要转化为
- [ ] 0001. 两数之和"

    let content = match $datasource {
        "stdin" => {
            try {
                print $"Reading from stdin \(timeout: ($timeout) seconds)..."
                let input = (timeout $timeout { $in | collect })
                if ($input | is-empty) {
                    print "Error: No input received from stdin"
                    exit 1
                }
                $input
            } catch { |e|
                print $"Error reading from stdin: ($e.msg)"
                exit 1
            }
        }
        _ => {
            if not ($datasource | path exists) {
                print $"Error: Input file '($datasource)' does not exist"
                exit 1
            }
            print $"Reading from file: ($datasource)"
            open $datasource
        }
    }

    let user_prompt = $"<text> ($content) </text>"

    print "Calling OpenAI API..."
    let response = (http post -H [Authorization $"Bearer ($openai_api_key)"] $"($openai_base_url)/v1/chat/completions" {
        model: $openai_model,
        messages: [
            {role: "system", content: $system_prompt},
            {role: "user", content: $user_prompt}
        ],
        temperature: 0.7
    })

    if ($response | get -i error?) != null {
        print $"Error calling OpenAI API: ($response.error)"
        exit 1
    }

    let markdown_content = ($response.choices | first | get message.content)

    let clean_content = ($markdown_content
        | str replace -r "^```markdown" ""
        | str replace -r "```$" ""
        | str trim)

    let output_dir = ($output | path dirname)
    if $output_dir != "." and not ($output_dir | path exists) {
        mkdir $output_dir
    }

    $clean_content | save $output
    print $"Output saved to: ($output)"
}

if ($nu | version | get major) >= 0 {
    main
} else {
    print "Error: This script requires Nushell 0.78 or later"
    exit 1
}
