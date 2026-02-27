---
tags:
  - computing/data-representation
  - number-systems
  - binary
related:
  - "[[Data Representation]]"
  - "[[Boolean Algebra]]"
  - "[[00 - Computing MOC]]"
---

## Common Bases
### Binary (Base 2)
- Digits: 0, 1
- Position values(weights): ..., 8, 4, 2, 1
- Example: $1011_2$

### Octal (Base 8)
- Digits: 0, 1, 2, 3, 4, 5, 6, 7
- Position values(weights): ..., 512, 64, 8, 1
- Real-word example:
	- Unix file permissions (chmod 0755) — each octal digit represents 3 permission bits.

### Decimal (Base 10)
- Digits: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
- Position values(weights): ..., 1000, 100, 10, 1
- Example: $159_{10}$

### Hexadecimal (Base 16)
- Digits: 0-9, A-F (A=10, B=11, C=12, D=13, E=14, F=15)
- Position values(weights): ..., 4096, 256, 16, 1
- Real-world examples:
	- Memory addresses: 0x7FFFAABB
	- Colors in CSS/graphics: #FF8800 → RGB bytes
	- MAC addresses and IPv6: hardware/network identifiers
	- File headers / magic numbers: first bytes of files often shown in hex
	- Hashes / cryptography: MD5/SHA outputs

---

### Positional Value (weight) Formula
For a number $d_nd_{n-1}...d_1d_0$ in base $b$:
### $$\boxed{\text{Decimal Value} = d_n \times b^n + d_{n-1} \times b^{n-1} + \cdots + d_1 \times b^1 + d_0 \times b^0}$$
where:
- $b^n$ is a positional value(weight). e.g. $(123)_{10}$ has weights: 100, 10, 1
- $d_i$ is a digit in base $b$
- $2^n$ can be represented using $n$ bits

---
### Any Base $\to$ Decimal

#formula

### $$\boxed{\text{Decimal} = \sum_{i=0}^{n} d_i \times b^i}$$

**Example**: $(1011)_2$ to decimal:
$$1×2^3 + 0×2^2 + 1×2^1 + 1×2^0 = 8 + 0 + 2 + 1 = 11$$
**Result:** $11_{10}$

---
### Decimal $\gets$ Any Base
#### Division Method (Integer Part):
1. Divide number by target base
2. Record remainder
3. Use quotient as new number
4. Repeat until quotient = 0
5. Read remainders in **reverse order**

#formula

### $$\boxed{N_{10} = d_0 + b(d_1 + b(d_2 + \cdots))}$$

### Example:
**Decimal to Binary ($159_{10}$ → $?_2$):**

| Division Step     | Quotient | Remainder | Note     |
|-------------------|----------|-----------|----------|
| 159 ÷ 2           | 79       | 1         | LSB      |
| 79 ÷ 2            | 39       | 1         |          |
| 39 ÷ 2            | 19       | 1         |          |
| 19 ÷ 2            | 9        | 1         |          |
| 9 ÷ 2             | 4        | 1         |          |
| 4 ÷ 2             | 2        | 0         |          |
| 2 ÷ 2             | 1        | 0         |          |
| 1 ÷ 2             | 0        | 1         | MSB      |

**THEN WRITE ALL REMAINDERS FROM BOTTOM TO TOP $\uparrow$**

**left most** - the most significant bit (**msb**)
**right most** (when written in a row) - the least significant bit (**lsb**)
**Result**: 10011111₂

---

### Powers of 2
| Power | Value | Power  | Value  |
| ----- | ----- | ------ | ------ |
| $2^0$ | 1     | $2^8$  | 256    |
| $2^1$ | 2     | $2^9$  | 512    |
| $2^2$ | 4     | $2^10$ | 1 024  |
| $2^3$ | 8     | $2^11$ | 2 048  |
| $2^4$ | 16    | $2^12$ | 4 096  |
| $2^5$ | 32    | $2^13$ | 8 192  |
| $2^6$ | 64    | $2^14$ | 16 384 |
| $2^7$ | 128   | $2^15$ | 32 768 |

---
## Basic Binary Operations 
### Addition

![[bin_add.excalidraw]]

### Subtraction

![[bin_sub]]

### Multiplication

![[bin_mult.excalidraw]]

### Division

![[bin_div.excalidraw]]

---
### Float Decimal $\to$ Binary
```
Integer part (13):
13 ÷ 2 = 6 remainder 1
6  ÷ 2 = 3 remainder 0
3  ÷ 2 = 1 remainder 1
1  ÷ 2 = 0 remainder 1
13₁₀ = 1101₂

Fractional part (0.625):
0.625 × 2 = 1.25 → 1
0.25  × 2 = 0.5  → 0
0.5   × 2 = 1.0  → 1
0.625₁₀ = 0.101₂

Combined: 13.625₁₀ = 1101.101₂
```

---
### Float Decimal $\gets$ Binary
use this formula: [[Number Systems#Positional Value (weight) Formula]]



---

## See Also
- [[Data Representation]] - Two's complement, IEEE 754
- [[Boolean Algebra]] - Binary operations
- [[00 - Computing MOC]] - Computing topics overview