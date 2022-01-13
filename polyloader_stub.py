#! /usr/bin/env bash
#! nix-shell -i python -p "python38.withPackages (p: with p; [ lxml ])" -v

# nix-polyloader

"""true"
SCRIPT_PATH="$(realpath -s "$BASH_SOURCE")"
if ! command -v nix-shell; then
  exec python "$SCRIPT_PATH" "$@"
else
  exec nix-shell "$SCRIPT_PATH" "$@"
fi
"true"""

# Python starts
