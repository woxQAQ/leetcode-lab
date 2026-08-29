#!/usr/bin/env nu

def is-interrupt [error: record] {
    [
        ($error | get --optional msg | default "")
        ($error | get --optional debug | default "")
        ($error | get --optional rendered | default "")
        ($error | get --optional json | default "")
    ] | str join " " | str lowercase | str contains "interrupt"
}

def read-input [prompt: string] {
    try {
        input $prompt
    } catch {|error|
        if (is-interrupt $error) {
            print $"(ansi green)Goodbye!(ansi reset)"
            exit 0
        }

        let message = $error | get --optional msg | default "Unknown input error"
        print --stderr $"(ansi red)Error: ($message)(ansi reset)"
        exit 1
    }
}

def read-input-or-cancel [prompt: string] {
    try {
        input $prompt
    } catch {|error|
        if (is-interrupt $error) {
            print ""
        } else {
            let message = $error | get --optional msg | default "Unknown input error"
            print --stderr $"(ansi red)Error: ($message)(ansi reset)"
        }

        null
    }
}

def print-command-result [result: record] {
    if not ($result.stdout | is-empty) {
        print --no-newline $result.stdout
    }
    if not ($result.stderr | is-empty) {
        print --stderr --no-newline $result.stderr
    }
}

def get-current-problem [] {
    let result = (^leetgo info last --full --format json | complete)
    if $result.exit_code != 0 {
        return null
    }

    try {
        $result.stdout | from json | first
    } catch {
        print --stderr $"(ansi red)Error: Could not parse `leetgo info` output.(ansi reset)"
        null
    }
}

def render-markdown [markdown: string] {
    if (which glow | is-empty) {
        return $markdown
    }

    let columns = (
        try {
            term size | get columns
        } catch { 80 }
    )
    let width = if $columns > 100 {
        100
    } else if $columns < 20 {
        80
    } else {
        $columns - 2
    }

    # glow disables styling when its output is captured instead of attached to a TTY.
    let result = (with-env { CLICOLOR_FORCE: "1" } {
    $markdown | ^glow --style dark --width $width - | complete
  })

    if $result.exit_code == 0 {
        $result.stdout
    } else {
        $markdown
    }
}

def render-problem [problem: record] {
    let id = $problem | get --optional frontend_id | default "?"
    let title = $problem | get --optional title | default "Unknown"
    let difficulty = $problem | get --optional difficulty | default "Unknown"
    let tags = (
        $problem
        | get --optional tags
        | default []
        | str join ", "
    )
    let ac_rate = $problem | get --optional ac_rate | default "N/A"
    let content = $problem | get --optional content | default ""

    let colored_difficulty = match $difficulty {
        Easy => $"(ansi green)($difficulty)(ansi reset)"
        Medium => $"(ansi yellow)($difficulty)(ansi reset)"
        Hard => $"(ansi red)($difficulty)(ansi reset)"
        _ => $difficulty
    }
    let tag_line = if ($tags | is-empty) {
        ""
    } else {
        $"Tags: (ansi cyan)($tags)(ansi reset)  |  "
    }
    let body = if ($content | is-empty) {
        $"(ansi yellow)No description available.(ansi reset)"
    } else {
        render-markdown $content
    }

    $"(ansi blue)━━━ ($id). ($title) ━━━(ansi reset)
Difficulty: ($colored_difficulty)  |  ($tag_line)AC Rate: ($ac_rate)

($body)"
}

def load-session [] {
    let problem = (get-current-problem)
    if $problem == null {
        {problem: null, view: "", status: "No problem selected"}
    } else {
        {
            problem: $problem
            view: (render-problem $problem)
            status: "Ready"
        }
    }
}

def pick-problem [] {
    print $"(ansi blue)Pick a problem(ansi reset)"
    let raw_number = (read-input-or-cancel "Problem number (blank to cancel): ")
    if $raw_number == null {
        return "cancelled"
    }

    let raw_number = $raw_number | str trim
    if ($raw_number | is-empty) {
        return "cancelled"
    }
    if not ($raw_number =~ '^\d+$') {
        print $"(ansi red)Error: Enter a positive problem number.(ansi reset)"
        return "failed"
    }

    let problem_number = $raw_number | into int
    if $problem_number < 1 {
        print $"(ansi red)Error: Enter a positive problem number.(ansi reset)"
        return "failed"
    }

    let result = (^leetgo pick ($problem_number | into string) | complete)
    print-command-result $result

    if $result.exit_code != 0 {
        print $"(ansi red)Could not pick problem ($problem_number).(ansi reset)"
        return "failed"
    }

    print $"(ansi green)Problem ($problem_number) picked.(ansi reset)"
    "picked"
}

def test-solution [] {
    let result = (^leetgo test last --local | complete)
    print-command-result $result

    if $result.exit_code == 0 {
        print $"(ansi green)Local tests passed.(ansi reset)"
        true
    } else {
        print $"(ansi yellow)Local tests failed.(ansi reset)"
        false
    }
}

def submit-solution [] {
    print $"(ansi blue)Submitting solution...(ansi reset)"

    # leetgo polls indefinitely while a submission remains pending.
    let job_id = (job spawn {
    ^leetgo submit last | complete | job send 0
  })
    let result = (try {
    job recv --timeout 2min
  } catch {|error|
    try { job kill $job_id }
    if (is-interrupt $error) {
      print $"(ansi green)Goodbye!(ansi reset)"
      exit 0
    }
    if $error.details.code != "nu::shell::job::recv_timeout" {
      error make $error.details
    }
    null
  })

    if $result == null {
        print $"(ansi red)Submission timed out after 2 minutes.(ansi reset)"
        return "timeout"
    }

    print-command-result $result

    if ($result.stdout | str contains "Accepted") {
        print $"(ansi green)Solution accepted! 🎉(ansi reset)"
        "accepted"
    } else if not ($result.stdout | str trim | is-empty) {
        print $"(ansi yellow)Submission was not accepted.(ansi reset)"
        "rejected"
    } else {
        print $"(ansi red)Could not submit the solution.(ansi reset)"
        "error"
    }
}

def main [] {
    if (which leetgo | is-empty) {
        print --stderr $"(ansi red)Error: `leetgo` is not available in PATH.(ansi reset)"
        exit 1
    }

    let has_glow = which glow | is-not-empty
    mut session = (load-session)

    loop {
        clear
        print $"(ansi green)LeetCode Workflow(ansi reset)"
        print "================="

        if not $has_glow {
            print $"(ansi dark_gray)Tip: install glow for formatted problem descriptions.(ansi reset)"
        }

        print $"Status: ($session.status)"
        if $session.problem != null {
            print ""
            print $session.view
        }

        print $"
(ansi cyan)Actions(ansi reset)
1. Pick a problem
2. Run local tests
3. Submit solution
4. Exit
"

        let choice = read-input "Choose an action (1-4): " | str trim
        match $choice {
            "1" => {
                match (pick-problem) {
                    "picked" => {
                        $session = load-session
                        if $session.problem == null {
                            $session.status = "Could not load the picked problem"
                        }
                    }
                    "failed" => { $session.status = "Pick failed" }
                    "cancelled" => { continue }
                }
            }
            "2" => {
                if $session.problem == null {
                    print $"(ansi red)Pick a problem first.(ansi reset)"
                } else if (test-solution) {
                    $session.status = "Local tests passed"
                } else {
                    $session.status = "Local tests failed"
                }
            }
            "3" => {
                if $session.problem == null {
                    print $"(ansi red)Pick a problem first.(ansi reset)"
                } else {
                    $session.status = (match (submit-solution) {
            "accepted" => "Accepted"
            "rejected" => "Not accepted"
            "timeout" => "Submission timed out"
            _ => "Submission failed"
          })
                }
            }
            "4" => { break }
            _ => { print $"(ansi red)Invalid action.(ansi reset)" }
        }

        print ""
        read-input "Press Enter to continue..." | ignore
    }

    print $"(ansi green)Goodbye!(ansi reset)"
}
