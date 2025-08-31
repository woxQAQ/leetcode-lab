{
  pkgs ? import <nixpkgs> { },
}:

pkgs.mkShell {
  name = "leetcode-shell";

  buildInputs = with pkgs; [
    # Go is required for leetgo
    leetgo
    python3
    (writeShellScriptBin "ltest" ''
      ${pkgs.leetgo}/bin/leetgo test last
    '')
    (writeShellScriptBin "lpush" ''
      ${pkgs.leetgo}/bin/leetgo submit last
    '')
    (writeShellScriptBin "lpick" ''
      if [ -z "$1" ]; then
        echo "❌ Please provide a question ID"
        echo "Usage: lpick <qid>"
        return 1
      fi
      ${pkgs.leetgo}/bin/leetgo pick "$1"
    '')
  ];

  shellHook = ''
    echo "🚀 LeetCode development environment activated"
    echo "📝 Available commands:"
    echo "   lpick <qid>    - Pick a LeetCode problem (leetgo pick <qid>)"
    echo "   ltest          - Test the last problem (leetgo test last)"
    echo "   lpush          - Submit the last problem (leetgo submit last)"
    echo ""

    exec ${pkgs.zsh}/bin/zsh
  '';
}
