#!/usr/bin/env nu
def main [] {
    let current_time = (date now | format date "%Y-%m-%d %H:%M:%S")
    mut output = [$"Solution Update: ($current_time)"]

    let git_status = (git status --porcelain | lines | where { |line| not ($line | str starts-with "scripts/") })
    mut seen_problems = []

    for line in $git_status {
        let parts = ($line | split row ' ' | where { |part| $part != "" })
        let status = $parts.0
        let path = $parts.1

        if ($status == "??") or ($status == "M") or ($status == "A") {
            let path_parts = ($path | split row '/')
            if ($path_parts | length) < 2 {
                continue
            }
            let problem_folder = $path_parts.1
            let problem_parts = ($problem_folder | split row '.')
            let problem_number = $problem_parts.0
            let problem_name = if ($problem_parts | length) > 1 {
                ($problem_parts.1 | split row '-' | str join ' ')
            } else {
                ""  # Skip invalid entries
            }

            if ($problem_name == "") {
                continue
            }

            let problem_key = $"($problem_number): ($problem_name)"
            if ($problem_key in $seen_problems) {
                continue
            }
            $seen_problems = ($seen_problems | append [$problem_key])

            if $status == "??" {
                $output = ($output | append [$"Pick LeetCode.($problem_number): ($problem_name)"])
            } else if $status == "M" {
                $output = ($output | append [$"Modify Solution LeetCode.($problem_number): ($problem_name)"])
            } else if $status == "A" {
                $output = ($output | append [$"Pick LeetCode.($problem_number): ($problem_name)"])
            }
        }
    }

    $output | str join "\n"
}
