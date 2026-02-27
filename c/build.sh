#!/bin/bash

if [ -z "$1" ]; then
    exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
src="$(cd "$(dirname "$1")" && pwd)/$(basename "$1")"
filename=$(basename "$1")
target="$SCRIPT_DIR/bin/${filename%.*}"

mkdir -p "$SCRIPT_DIR/bin"

gcc -Wall -Wextra -std=c11 -g -fsanitize=address,undefined "$src" -o "$target"
