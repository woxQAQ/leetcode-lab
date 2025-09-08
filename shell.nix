{
  pkgs ? import <nixpkgs> { },
}:

pkgs.mkShell {
  name = "leetcode-shell";

  buildInputs = with pkgs; [
    # Go is required for leetgo
    leetgo
    python3
  ];

  shellHook = ''
    echo "🚀 LeetCode development environment activated"
    echo ""

    exec ${pkgs.zsh}/bin/zsh
  '';
}
