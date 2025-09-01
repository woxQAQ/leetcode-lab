#!/usr/bin/env nu

# LeetCode TUI Workflow Manager
# Provides unified interface for lpick -> IDE -> ltest -> lpush -> commit workflow

def main [] {
    clear
    print $"(ansi green)LeetCode TUI Workflow Manager(ansi reset)"
    print "========================================="
    print ""
    
    mut current_problem = (get-current-problem)
    mut last_action = ""
    mut workflow_state = if $current_problem != null { "coding" } else { "idle" }  # idle, picking, coding, testing, pushing
    
    loop {
        print $"(ansi yellow)Current Status:(ansi reset)"
        if $current_problem != null {
            print $"Problem: ($current_problem)"
        } else {
            print "No problem selected"
        }
        print $"Last action: ($last_action)"
        
        # Display workflow state with color
        if $workflow_state == "Accepted" {
            print $"Workflow state: (ansi green)($workflow_state)(ansi reset)"
        } else {
            print $"Workflow state: ($workflow_state)"
        }
        print ""
        
        print $"(ansi cyan)Main Menu:(ansi reset)"
        print "1. Pick new problem (enter problem number)"
        print "2. Test current solution (ltest)"
        print "3. Push solution (lpush)"
        print "4. Commit and push all solutions"
        print "5. View git status"
        print "6. Open IDE (code .)"
        print "7. Extract CodeTop problems"
        print "8. Exit"
        print ""
        
        let choice = (input "Enter your choice (1-8): ")
        
        match $choice {
            "1" => {
                pick-problem
                $current_problem = get-current-problem
                $workflow_state = "coding"
                $last_action = "Picked new problem"
            }
            "2" => {
                if $current_problem == null {
                    print $"(ansi red)Error: No problem selected. Please pick a problem first.(ansi reset)"
                    print ""
                    continue
                }
                test-solution
                $workflow_state = "testing"
                $last_action = "Tested solution"
            }
            "3" => {
                if $current_problem == null {
                    print $"(ansi red)Error: No problem selected. Please pick a problem first.(ansi reset)"
                    print ""
                    continue
                }
                let push_result = (push-solution)
                if $push_result == "Accepted" {
                    $workflow_state = "Accepted"
                    $last_action = "Solution Accepted! 🎉"
                } else if $push_result == "pushed" {
                    $workflow_state = "pushed"
                    $last_action = "Solution pushed (not accepted)"
                } else {
                    $workflow_state = "error"
                    $last_action = "Failed to push solution"
                }
            }
            "4" => {
                commit-all
                $workflow_state = "idle"
                $last_action = "Committed all solutions"
            }
            "5" => {
                show-git-status
                $last_action = "Viewed git status"
            }
            "6" => {
                open-ide
                $last_action = "Opened IDE"
            }
            "7" => {
                extract-codetop
                $last_action = "Extracted CodeTop problems"
            }
            "8" => {
                print $"(ansi green)Goodbye!(ansi reset)"
                exit 0
            }
            _ => {
                print $"(ansi red)Invalid choice. Please try again.(ansi reset)"
                print ""
            }
        }
        
        # Only show "Press Enter to continue" if not exiting
        if $choice != "8" {
            print ""
            print "Press Enter to continue..."
            input
            clear
        }
    }
}

# Pick a problem by direct number input
def pick-problem [] {
    print $"(ansi blue)Problem Selection...(ansi reset)"
    print "Enter the LeetCode problem number you want to solve."
    print "Examples: 1, 2, 15, 1642, etc."
    print ""
    
    let problem_number = (input "Enter LeetCode problem number: ")
    
    if ($problem_number | str trim) == "" {
        print $"(ansi red)Error: Problem number cannot be empty.(ansi reset)"
        return
    }
    
    try {
        # Run lpick with the specific problem number
        ^lpick $problem_number
        print $"(ansi green)Problem ($problem_number) picked successfully!(ansi reset)"
    } catch { |e|
        print $"(ansi red)Error picking problem ($problem_number): ($e.msg)(ansi reset)"
        print "Please check if the problem number exists."
    }
}

# Get leetgo home directory according to official logic
def get-leetgo-home [] {
    # 1. Check LEETGO_HOME environment variable
    let leetgo_home = ($env.LEETGO_HOME? | default "")
    if $leetgo_home != "" {
        return $leetgo_home
    }
    
    # 2. Default to ~/.config/leetgo
    return $"($env.HOME)/.config/leetgo"
}

# Get leetgo cache directory
def get-leetgo-cache-dir [] {
    return $"(get-leetgo-home)/cache"
}

# Get the current problem from leetgo cache
def get-current-problem [] {
    try {
        let cache_dir = (get-leetgo-cache-dir)
        let cache_file = $"($cache_dir)/state.json"
        
        if not ($cache_file | path exists) {
            print $"(ansi yellow)Warning: Leetgo cache file not found: ($cache_file)(ansi reset)"
            return null
        }
        
        let cache_data = (open $cache_file)
        let current_dir = (pwd)
        
        # Find the cache entry for current directory
        let cache_entry = ($cache_data | get --optional $current_dir)
        if $cache_entry == null {
            print $"(ansi yellow)Warning: No cache entry found for current directory: ($current_dir)(ansi reset)"
            return null
        }
        
        let last_question = ($cache_entry | get --optional "last_question")
        if $last_question == null {
            print $"(ansi yellow)Warning: No last_question found in cache(ansi reset)"
            return null
        }
        
        let frontend_id = ($last_question | get --optional "frontend_id")
        let slug = ($last_question | get --optional "slug")
        let gen = ($last_question | get --optional "gen")
        
        if ($frontend_id == null) or ($slug == null) {
            print $"(ansi yellow)Warning: Incomplete question data in cache(ansi reset)"
            return null
        }
        
        # Convert slug to readable name
        let readable_name = ($slug | split row '-' | str join ' ')
        let lang = if $gen == "python3" { "Python" } else { $gen }
        
        return $"LeetCode.($frontend_id): ($readable_name) [($lang)]"
        
    } catch { |e|
        print $"(ansi red)Error getting current problem from leetgo cache: ($e.msg)(ansi reset)"
        return null
    }
}

# Test the current solution using ltest
def test-solution [] {
    print $"(ansi blue)Testing solution...(ansi reset)"
    try {
        ^ltest
        print $"(ansi green)Solution tested successfully!(ansi reset)"
    } catch { |e|
        print $"(ansi red)Error testing solution: ($e.msg)(ansi reset)"
    }
}

# Push the solution using lpush
def push-solution [] {
    print $"(ansi blue)Pushing solution...(ansi reset)"
    try {
        let output = (^lpush)
        
        # Check if the output contains "Accepted" and format accordingly
        if ($output | str contains "Accepted") {
            # Replace "Accepted" with green version
            let colored_output = ($output | str replace "Accepted" $"(ansi green)Accepted(ansi reset)")
            print $colored_output
            print $"(ansi green)🎉 Solution Accepted!(ansi reset)"
            return "Accepted"
        } else {
            print $output
            print $"(ansi yellow)Solution pushed but not accepted(ansi reset)"
            return "pushed"
        }
    } catch { |e|
        print $"(ansi red)Error pushing solution: ($e.msg)(ansi reset)"
        return "error"
    }
}

# Commit all solutions using the Makefile
def commit-all [] {
    print $"(ansi blue)Committing all solutions...(ansi reset)"
    try {
        make commit
        print $"(ansi green)All solutions committed successfully!(ansi reset)"
    } catch { |e|
        print $"(ansi red)Error committing solutions: ($e.msg)(ansi reset)"
    }
}

# Show git status
def show-git-status [] {
    print $"(ansi blue)Git Status:(ansi reset)"
    try {
        git status
    } catch { |e|
        print $"(ansi red)Error getting git status: ($e.msg)(ansi reset)"
    }
}

# Open IDE (VS Code)
def open-ide [] {
    print $"(ansi blue)Opening IDE...(ansi reset)"
    try {
        ^code .
        print $"(ansi green)IDE opened successfully!(ansi reset)"
    } catch { |e|
        print $"(ansi red)Error opening IDE: ($e.msg)(ansi reset)"
    }
}

# Extract CodeTop problems
def extract-codetop [] {
    print $"(ansi blue)Extracting CodeTop problems...(ansi reset)"
    try {
        nu scripts/codetop-extractor.nu
        print $"(ansi green)CodeTop problems extracted successfully!(ansi reset)"
    } catch { |e|
        print $"(ansi red)Error extracting CodeTop problems: ($e.msg)(ansi reset)"
    }
}

# Main entry point
if ($nu | version | get major) >= 0 {
    main
} else {
    print "Error: This script requires Nushell 0.78 or later"
    exit 1
}