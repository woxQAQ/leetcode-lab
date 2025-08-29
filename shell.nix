{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  name = "leetcode-shell";

  buildInputs = with pkgs; [
    # Go is required for leetgo
    leetgo
    python3
  ];

  shellHook = ''
    echo "🚀 LeetCode development environment activated"
    echo "📝 Available commands:"
    echo "   lpick <qid>    - Pick a LeetCode problem (leetgo pick <qid>)"
    echo "   ltest          - Test the last problem (leetgo test last)"
    echo "   lsubmit        - Submit the last problem (leetgo submit last)"
    echo ""

    # Install leetgo if not already installed
    if ! command -v leetgo &> /dev/null; then
      echo "📦 Installing leetgo..."
      go install github.com/j178/leetgo@latest
    fi

    # Create custom commands
    lpick() {
      if [ -z "$1" ]; then
        echo "❌ Please provide a question ID"
        echo "Usage: lpick <qid>"
        return 1
      fi
      leetgo pick "$1"
    }

    ltest() {
      leetgo test last
    }

    lsubmit() {
      leetgo submit last
    }

    # Export functions to make them available in subshells
    export -f lpick ltest lsubmit
  '';
}
