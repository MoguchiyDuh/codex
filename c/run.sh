#!/bin/bash

if [ -z "$1" ]; then
    exit 1
fi

filename=$(basename "$1")
target="bin/${filename%.*}"

mkdir -p src

if gcc -Wall -Wextra -std=c11 -g -fsanitize=address,undefined "$1" -o "$target"; then
    ./"$target"
fi
