#!/usr/bin/env nu

def main [lang?: string] {
  open leetgo.yaml --raw
  | str replace -r '(lang:)\s*(\S+)' $'$1 ($lang)'
  | save --force leetgo.yaml
}
