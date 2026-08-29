#!/usr/bin/env nu

# LeetCode TUI Workflow Manager
# Provides unified interface for lpick -> IDE -> ltest -> lpush -> commit workflow
#
# Features:
# - Problem selection by number
# - Solution testing and submission
# - Git integration for commits
# - CodeTop problem extraction
# - Error handling and user feedback

# Nushell versions expose interrupt details in different error fields.
def is-interrupt [e] {
  let details = ([
    ($e | get --optional msg | default "")
    ($e | get --optional debug | default "")
    ($e | get --optional rendered | default "")
    ($e | get --optional json | default "")
  ] | str join " " | str lowercase)

  return ($details | str contains "interrupt")
}

# Handle interrupt errors consistently
# Returns error message or exits on interrupt
def handle-interrupt [e] {
  if (is-interrupt $e) {
    print $"(ansi green)Goodbye!(ansi reset)"
    exit 0
  }

  return ($e | get --optional msg | default "Unknown error occurred")
}

# Get user input with interrupt handling
# Exits on interrupt or error
def get-input [prompt: string] {
  try {
    input $prompt
  } catch { |e|
    let error_msg = (handle-interrupt $e)
    print $"(ansi red)Error: ($error_msg)(ansi reset)"
    exit 1
  }
}

# Get user input with interrupt handling (safe version)
# Returns null on interrupt or error
def get-input-safe [prompt: string] {
  try {
    input $prompt
  } catch { |e|
    if (is-interrupt $e) {
      print ""
    } else {
      let error_msg = ($e | get --optional msg | default "Unknown error occurred")
      print $"(ansi red)Error: ($error_msg)(ansi reset)"
    }
    return null
  }
}

def main [] {
  clear
  print $"(ansi green)LeetCode TUI Workflow Manager(ansi reset)"
  print "========================================="
  print ""

  # Check if leetgo is available
  if (which leetgo | is-empty) {
    print $"(ansi red)Error: leetgo command not found.(ansi reset)"
    print "Please install leetgo or ensure it's in your PATH."
    print ""
    print "Press Enter to exit..."
    get-input ""
    exit 1
  }

  # Mention the nicer rendering path once when glow is missing
  if (which glow | is-empty) {
    print $"(ansi dark_gray)Tip: install glow (github.com/charmbracelet/glow) for richer problem rendering.(ansi reset)"
    print ""
  }

  mut current_problem = (get-current-problem)
  mut current_problem_id = if $current_problem != null { $current_problem.id } else { null }
  mut current_problem_slug = if $current_problem != null { $current_problem.slug } else { null }
  mut current_problem_lang = if $current_problem != null { $current_problem.lang } else { null }
  # Cache problem content to avoid repeated fetches
  mut current_problem_content = ""
  mut last_action = ""
  mut workflow_state = if $current_problem != null { "coding" } else { "idle" }  # idle, picking, coding, testing, pushing

  loop {
    print $"(ansi yellow)Current Status:(ansi reset)"
    if $current_problem != null {
      print $"Problem: ($current_problem.display)"
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

    # Display problem content if a problem is selected (uses cache)
    if $current_problem_id != null {
      if ($current_problem_content | is-empty) {
        $current_problem_content = (fetch-problem-content $current_problem_id $current_problem_slug $current_problem_lang)
      }
      if not ($current_problem_content | is-empty) {
        print $current_problem_content
      }
    }

    print $"(ansi cyan)Main Menu:(ansi reset)"
    print "1. Pick new problem (enter problem number)"
    print "2. Test current solution"
    print "3. Push solution"
    # print "4. Commit and push all solutions"
    # print "5. View git status"
    # print "6. Extract CodeTop problems"
    # print "7. Switch Language"
    print "4. Exit"
    print ""

    let choice = (get-input "Enter your choice (1-4): ")

    match $choice {
      "1" => {
        let pick_result = (pick-problem)
        if $pick_result == "cancelled" {
          clear
          continue
        }
        if $pick_result == "picked" {
          $current_problem = get-current-problem
          if $current_problem != null {
            $current_problem_id = $current_problem.id
            $current_problem_slug = $current_problem.slug
            $current_problem_lang = $current_problem.lang
          } else {
            $current_problem_id = null
            $current_problem_slug = null
            $current_problem_lang = null
          }
          # Invalidate cache so content is re-fetched for new problem
          $current_problem_content = ""
          $workflow_state = "coding"
          $last_action = "Picked new problem"
        }
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
      # "4" => {
      #   commit-all
      #   $workflow_state = "idle"
      #   $last_action = "Committed all solutions"
      # }
      # "5" => {
      #   show-git-status
      #   $last_action = "Viewed git status"
      # }
      # "6" => {
      #   extract-codetop
      #   $last_action = "Extracted CodeTop problems"
      # }
      # "7" => {
      #   let lang = (get-input-safe "Enter language to switch: ")
      #   if not ($lang in ["python" "go" "java" "cpp"]) {
      #     print $"(ansi red)Error switch to ($lang):(ansi reset)"
      #   } else {
      #     ^nu ./scripts/switch-lang.nu $lang
      #   }
      # }
      "4" => {
        print $"(ansi green)Goodbye!(ansi reset)"
        exit 0
      }
      _ => {
        print $"(ansi red)Invalid choice. Please try again.(ansi reset)"
        print ""
      }
    }

    # Only show "Press Enter to continue" if not exiting
    if $choice != "4" {
      print ""
      get-input "Press Enter to continue..."
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

  let raw_problem_number = (get-input-safe "Enter LeetCode problem number: ")
  if $raw_problem_number == null {
    return "cancelled"
  }

  let problem_number = ($raw_problem_number | str replace -r '^0+' '')
  if ($problem_number | str trim) == "" {
    print $"(ansi red)Error: Problem number cannot be empty.(ansi reset)"
    return "invalid"
  }

  try {
    ^leetgo pick $problem_number
    print $"(ansi green)Problem ($problem_number) picked successfully!(ansi reset)"
    return "picked"
  } catch { |e|
    print $"(ansi red)Error picking problem ($problem_number):(ansi reset)"
    print $"(ansi red)Command: leetgo pick ($problem_number)(ansi reset)"
    print $"(ansi red)Error details: ($e.msg)(ansi reset)"
    if ($e | get --optional stderr) != null {
        print $"(ansi red)Stderr: ($e.stderr)(ansi reset)"
    }
    print "Please check if the problem number exists."
    return "failed"
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
# Returns a record: {display: string, id: string, slug: string, lang: string} or null
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

    let lang_display = ($gen | if $in == "python3" { "Python" } else { $in })
    let display = $"LeetCode.($frontend_id): ($slug | split row '-' | str join ' ') [($lang_display)]"

    return {
      display: $display
      id: $frontend_id
      slug: $slug
      lang: $gen
    }

  } catch { |e|
    print $"(ansi red)Error getting current problem from leetgo cache: ($e.msg)(ansi reset)"
    return null
  }
}

# Fetch problem content, preferring local question.md, falling back to leetgo info
# Result is cached in the main loop to avoid repeated reads
def fetch-problem-content [problem_id: string, slug: string, lang: string] {
  # Try local question.md first
  let padded_id = ($problem_id | fill -a right -c '0' -w 4)
  let local_path = (get-question-md-path $padded_id $slug $lang)

  if ($local_path != null) and ($local_path | path exists) {
    let result = (render-problem-from-md $local_path)
    if $result != null {
      return $result
    }
  }

  # Fallback: fetch from leetgo info
  let result = (fetch-problem-from-remote $problem_id)
  if $result != null {
    return $result
  }

  return $"(ansi blue)━━━ Problem Content ━━━(ansi reset)\n(ansi yellow)Unable to fetch problem content.(ansi reset)\n"
}

# Build path to question.md based on language and problem slug
def get-question-md-path [padded_id: string, slug: string, lang: string] {
  let base_dir = (match $lang {
    "rust" => "rust/src"
    "golang" => "go"
    "python3" => "python"
    "python" => "python"
    "cpp" => "cpp"
    "java" => "java"
    _ => { return null }
  })

  return $"($base_dir)/($padded_id).($slug)/question.md"
}

# Render markdown with glow; CLICOLOR_FORCE keeps styling even when output is piped
def render-markdown-glow [md: string] {
  let cols = (try { term size | get columns } catch { 80 })
  let width = (if $cols > 100 { 100 } else if $cols < 20 { 80 } else { $cols - 2 })

  # dark (not auto): auto drops all styling when the output is captured instead of a tty
  with-env { CLICOLOR_FORCE: "1" } {
    $md | ^glow -s dark -w $width -
  }
}

# Wrap every odd-index segment produced by splitting on a markdown marker
def wrap-pairs [text: string, marker: string, before: string, after: string] {
  let pieces = ($text | split row $marker)
  if ($pieces | length) < 2 {
    return $text
  }

  $pieces | enumerate | each {|piece|
    if ($piece.index mod 2) == 1 {
      $"($before)($piece.item)($after)"
    } else {
      $piece.item
    }
  } | str join ""
}

# Render inline markdown (code spans, bold) with ANSI
def render-inline [text: string] {
  let text = (wrap-pairs $text '`' (ansi cyan) (ansi reset))
  wrap-pairs $text '**' (ansi default_bold) (ansi reset)
}

# Minimal built-in markdown renderer, used when glow is not installed
def render-markdown-basic [md: string] {
  mut in_code = false
  mut out = []

  for line in ($md | lines) {
    if ($line | str starts-with "```") {
      if $in_code {
        $out = ($out | append $"(ansi dark_gray)╰───(ansi reset)")
        $in_code = false
      } else {
        let lang = ($line | str substring 3.. | str trim)
        let label = (if $lang == "" { "" } else { $"($lang) " })
        $out = ($out | append $"(ansi dark_gray)╭─(ansi reset)(ansi cyan_bold)($label)(ansi reset)(ansi dark_gray)────(ansi reset)")
        $in_code = true
      }
    } else if $in_code {
      $out = ($out | append $"(ansi green)($line)(ansi reset)")
    } else if ($line | str starts-with "#") {
      let hashes = ($line | str substring ..2 | str trim)
      let level = (if $hashes == "###" { 3 } else if $hashes == "##" { 2 } else { 1 })
      let text = ($line | str substring ($level).. | str trim)
      $out = ($out | append $"(ansi yellow_bold)($text)(ansi reset)")
    } else if ($line | str starts-with ">") {
      $out = ($out | append $"(ansi dark_gray)▎(ansi reset) (ansi default_italic)($line | str substring 1.. | str trim)(ansi reset)")
    } else if ($line | str starts-with "- ") {
      $out = ($out | append $"  (ansi cyan)•(ansi reset) (render-inline ($line | str substring 2..))")
    } else if (($line | parse -r '^(?<n>\d+)\. (?<rest>.*)$') | length) > 0 {
      let item = ($line | parse -r '^(?<n>\d+)\. (?<rest>.*)$' | first)
      $out = ($out | append $"  (ansi cyan)($item.n).(ansi reset) (render-inline $item.rest)")
    } else if ($line | str trim) == "" {
      $out = ($out | append "")
    } else {
      $out = ($out | append (render-inline $line))
    }
  }

  $out | str join "\n"
}

# Render markdown via glow, falling back to the built-in renderer
def render-markdown [md: string] {
  if (which glow | is-empty) {
    return (render-markdown-basic $md)
  }

  try {
    render-markdown-glow $md
  } catch {
    render-markdown-basic $md
  }
}

# Render problem content from local question.md file
def render-problem-from-md [path: string] {
  try {
    let raw = (open --raw $path)
    # question.md format:
    # # [id. title][link] (Difficulty)
    # [link]: url
    #
    # content...

    let lines = ($raw | lines)

    # Parse title line: "# [id. title][link] (Difficulty)"
    let header = ($lines | first)
    let title_match = ($header | parse '# [{id}. {title}][link] ({difficulty})')

    let title = if ($title_match | length) > 0 {
      ($title_match | get title | first)
    } else {
      "Unknown"
    }
    let difficulty = if ($title_match | length) > 0 {
      ($title_match | get difficulty | first)
    } else {
      "Unknown"
    }

    # Content starts after the [link]: line (line index 2, content from line 3)
    let content = if ($lines | length) > 2 {
      ($lines | skip 3 | str join "\n")
    } else {
      ""
    }

    let colored_difficulty = (match $difficulty {
      "Easy" => $"(ansi green)($difficulty)(ansi reset)"
      "Medium" => $"(ansi yellow)($difficulty)(ansi reset)"
      "Hard" => $"(ansi red)($difficulty)(ansi reset)"
      _ => $difficulty
    })

    let body = if ($content | is-empty) {
      $"(ansi yellow)No description available.(ansi reset)"
    } else {
      render-markdown $content
    }

    return $"(ansi blue)━━━ Problem Content ━━━(ansi reset)\n(ansi white_bold)($title)(ansi reset) - ($colored_difficulty)\n\n($body)\n"
  } catch {
    return null
  }
}

# Fetch problem content from leetgo info (network call)
def fetch-problem-from-remote [problem_id: string] {
  try {
    let info_json = (^leetgo info $problem_id --full --format json | complete)

    if $info_json.exit_code != 0 {
      return null
    }

    let info = ($info_json.stdout | from json)
    let problem = ($info | first)

    let title = ($problem | get --optional "title" | default "Unknown")
    let difficulty = ($problem | get --optional "difficulty" | default "Unknown")
    let tags = ($problem | get --optional "tags" | default [] | str join ", ")
    let ac_rate = ($problem | get --optional "ac_rate" | default "N/A")
    let content = ($problem | get --optional "content" | default "")

    let colored_difficulty = (match $difficulty {
      "Easy" => $"(ansi green)($difficulty)(ansi reset)"
      "Medium" => $"(ansi yellow)($difficulty)(ansi reset)"
      "Hard" => $"(ansi red)($difficulty)(ansi reset)"
      _ => $difficulty
    })

    let description = if ($content | is-empty) {
      $"(ansi yellow)No description available.(ansi reset)"
    } else {
      render-markdown $content
    }

    return $"(ansi blue)━━━ Problem Content ━━━(ansi reset)\n(ansi white_bold)($title)(ansi reset) - ($colored_difficulty)\nTags: (ansi cyan)($tags)(ansi reset)  |  AC Rate: ($ac_rate)\n\n($description)\n"
  } catch {
    return null
  }
}

# Test the current solution using leetgo test
def test-solution [] {
  try {
    ^leetgo test last --local
    print $"(ansi green)Solution tested successfully!(ansi reset)"
  } catch {
    print $"(ansi yellow)Test failed. Please check your solution and try again.(ansi reset)"
  }
}

# Push the solution using leetgo submit
def push-solution [] {
  print $"(ansi blue)Pushing solution...(ansi reset)"
  try {
    let output = (^leetgo submit last)
    if ($output | str contains "Accepted") {
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
    print $"(ansi red)Error pushing solution:(ansi reset)"
    print $"(ansi red)Command: leetgo submit last(ansi reset)"
    print $"(ansi red)Error details: ($e.msg)(ansi reset)"
    if ($e | get --optional stderr) != null {
      print $"(ansi red)Stderr: ($e.stderr)(ansi reset)"
    }
    return "error"
  }
}

# Commit all solutions using the Makefile
def commit-all [] {
  make commit
}

# Show git status
def show-git-status [] {
    print $"(ansi blue)Git Status:(ansi reset)"
    try {
      git status
    } catch { |e|
      print $"(ansi red)Error getting git status:(ansi reset)"
      print $"(ansi red)Command: git status(ansi reset)"
      print $"(ansi red)Error details: ($e.msg)(ansi reset)"
      if ($e | get --optional stderr) != null {
        print $"(ansi red)Stderr: ($e.stderr)(ansi reset)"
      }
    }
}

# Extract CodeTop problems
def extract-codetop [] {
  nu scripts/codetop-extractor.nu
}

# Main entry point — nu runs `main` automatically when this file is executed as a script
