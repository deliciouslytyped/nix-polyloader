#! /usr/bin/env bash
#! nix-shell -i python -p "python38.withPackages (p: with p; [ lxml ])" -v

# This is a "multiplatform" bash/python polyglot file.
# The goal is convenience when running it as an executable, like "./whatever".
# On platforms that have the nix package manager, it will handle it's own dependencies.
# The bash loader stub is a portability hack to allow me to continue using this functionality
#  while being portable to other platforms that don't have nix-shell in scope.

# It's initially run as a bash file, and then reinvokes itself as a python file.
# It may also directly be run as a python file by passing it to the python interpreter.

# On platforms that have nix-shell, it uses it to get all it's necessary dependencies before it invokes itself.
# If it can't find nix-shell, it's assumed the dependencies already exist.

# Note the shebang works because of how this is coded:
#  https://github.com/NixOS/nix/blob/8803753666023882515404177b08f3f8bdad52a0/src/nix-build/nix-build.cc#L106

# Mechanism:
# - The # character is a comment in both sh and python (its comment nature is why it's used for the shebang)
# - The bash loader stub is quoted with python triple quotes to hide the syntax from python.
#  We need an even number of quotes to not quote it from bash. This also results in bash trying to run that
#  line as an empty command if you use """", so we do """true" to avoid an error.
# - The python is "hidden" from the bash because bash syntax is not checked in a single full pass,
#  and exec is called before it reaches invalid bash (the python code at the end).

# Tests:
# nix branch: ./polyloader.py
# non-nix branch: nix-shell --pure -p python --run ./polyloader.py

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

import lxml.etree as ET
print(ET.fromstring("<a>pls</a>").text)
