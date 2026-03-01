#!/bin/bash

# Compilation Model Step-by-Step Build Script
# This script demonstrates the 4 stages of C compilation.

set -e # Exit on error
echo "Starting step-by-step compilation..."
echo "-----------------------------------"

# 0. Clean up previous builds
rm -f main.i main.s main.o math_utils.i math_utils.s math_utils.o program

# 1. PREPROCESSOR (Stage 1)
# Expands macros, includes headers, and removes comments.
# Output: .i (Expanded C Source)
echo "[1/4] Preprocessing: main.c -> main.i"
gcc -E main.c -o main.i
gcc -E math_utils.c -o math_utils.i
echo "      - Macros like 'PI' and 'RADIUS' are now literal values in main.i."

# 2. COMPILER (Stage 2)
# Translates preprocessed C code into assembly language.
# Output: .s (Assembly Source)
echo "[2/4] Compiling: main.i -> main.s"
gcc -S main.i -o main.s
gcc -S math_utils.i -o math_utils.s
echo "      - Check main.s to see the 'add' function call as 'bl _add' (ARM) or 'call add' (x86)."

# 3. ASSEMBLER (Stage 3)
# Translates assembly into machine code (binary).
# Output: .o (Object File)
echo "[3/4] Assembling: main.s -> main.o"
gcc -c main.s -o main.o
gcc -c math_utils.s -o math_utils.o
echo "      - main.o contains machine code but doesn't know where 'add' is yet."
echo "      - Undefined symbols in main.o:"
nm main.o | grep " U "

# 4. LINKER (Stage 4)
# Combines object files and resolves symbol references.
# Output: executable binary
echo "[4/4] Linking: main.o + math_utils.o -> program"
gcc main.o math_utils.o -o program
echo "      - The linker matched the call in main.o to the implementation in math_utils.o."

echo "-----------------------------------"
echo "Build complete. Files generated:"
ls -F main.i main.s main.o math_utils.i math_utils.s math_utils.o program

echo ""
echo "Running the final program:"
./program
