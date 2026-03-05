#include <assert.h>
#include <stddef.h>
#include <stdio.h>

// Example 1: Members ordered inefficiently
// char (1 byte) + padding (3 bytes) + int (4 bytes) + char (1 byte) + padding
// (7 bytes) + long (8 bytes) Expected size: 24 bytes (on 64-bit systems)
struct Inefficient {
  char a; // Offset: 0
  int b;  // Offset: 4 (3 bytes of padding after 'a')
  char c; // Offset: 8
  long d; // Offset: 16 (7 bytes of padding after 'c')
};

// Example 2: Members ordered efficiently (largest to smallest)
// long (8 bytes) + int (4 bytes) + char (1 byte) + char (1 byte) + padding (2
// bytes) Expected size: 16 bytes (on 64-bit systems)
struct Efficient {
  long d; // Offset: 0
  int b;  // Offset: 8
  char a; // Offset: 12
  char c; // Offset: 13
          // 2 bytes of tail padding to align the struct itself to 8 bytes
};

// Example 3: Small members with mixed padding
struct Mixed {
  char a;  // Offset: 0
  short b; // Offset: 2 (1 byte padding after 'a')
  char c;  // Offset: 4
  int d;   // Offset: 8 (3 bytes padding after 'c')
};

// ─── Packed struct demo ────────────────────────────────────────────────────
// Example 4: Normal layout – the compiler inserts padding so every member
// sits on its natural alignment boundary.
struct Normal {
  char x;
  short y;
  int z;
  double w;
};

// Example 5: Packed layout – __attribute__((packed)) tells GCC/Clang to
// remove ALL padding. Members are tightly packed one after another, even
// when that means unaligned accesses.
struct __attribute__((packed)) Packed {
  char x;
  short y;
  int z;
  double w;
};

// ─── tests ────────────────────────────────────────────────────────────────
void test_inefficient(void) {
  assert(sizeof(struct Inefficient) == 24);
  assert(offsetof(struct Inefficient, a) == 0);
  assert(offsetof(struct Inefficient, b) == 4); // 3 bytes padding after 'a'
  assert(offsetof(struct Inefficient, c) == 8);
  assert(offsetof(struct Inefficient, d) == 16); // 7 bytes padding after 'c'

  // print offsets for visual inspection
  printf("--- struct Inefficient ---\n");
  printf("Total Size: %zu bytes\n", sizeof(struct Inefficient));
  printf("  offset of 'char a': %zu\n", offsetof(struct Inefficient, a));
  printf("  offset of 'int  b': %zu\n", offsetof(struct Inefficient, b));
  printf("  offset of 'char c': %zu\n", offsetof(struct Inefficient, c));
  printf("  offset of 'long d': %zu\n\n", offsetof(struct Inefficient, d));

  printf("Inefficient: ok\n");
}

void test_efficient(void) {
  assert(sizeof(struct Efficient) == 16);
  assert(offsetof(struct Efficient, d) == 0);
  assert(offsetof(struct Efficient, b) == 8);
  assert(offsetof(struct Efficient, a) == 12);
  assert(offsetof(struct Efficient, c) == 13);

  printf("--- struct Efficient ---\n");
  printf("Total Size: %zu bytes\n", sizeof(struct Efficient));
  printf("  offset of 'long d': %zu\n", offsetof(struct Efficient, d));
  printf("  offset of 'int  b': %zu\n", offsetof(struct Efficient, b));
  printf("  offset of 'char a': %zu\n", offsetof(struct Efficient, a));
  printf("  offset of 'char c': %zu\n\n", offsetof(struct Efficient, c));

  printf("Efficient:   ok\n");
}

void test_mixed(void) {
  assert(sizeof(struct Mixed) == 12);
  assert(offsetof(struct Mixed, a) == 0);
  assert(offsetof(struct Mixed, b) == 2); // 1 byte padding after 'a'
  assert(offsetof(struct Mixed, c) == 4);
  assert(offsetof(struct Mixed, d) == 8); // 3 bytes padding after 'c'

  printf("--- struct Mixed ---\n");
  printf("Total Size: %zu bytes\n", sizeof(struct Mixed));
  printf("  offset of 'char  a': %zu\n", offsetof(struct Mixed, a));
  printf("  offset of 'short b': %zu\n", offsetof(struct Mixed, b));
  printf("  offset of 'char  c': %zu\n", offsetof(struct Mixed, c));
  printf("  offset of 'int   d': %zu\n\n", offsetof(struct Mixed, d));

  printf("Mixed:       ok\n");
}

void test_packed(void) {
  // Packed removes all padding, so size == sum of member sizes
  assert(sizeof(struct Packed) == 1 + 2 + 4 + 8);
  assert(offsetof(struct Packed, x) == 0);
  assert(offsetof(struct Packed, y) == 1); // no padding after char
  assert(offsetof(struct Packed, z) == 3); // no padding after short
  assert(offsetof(struct Packed, w) == 7); // no padding after int

  // Normal has padding; must be strictly larger than Packed
  assert(sizeof(struct Normal) > sizeof(struct Packed));

  printf("--- struct Normal (with compiler padding) ---\n");
  printf("Total Size: %zu bytes\n", sizeof(struct Normal));
  printf("  offset of 'char   x': %zu\n", offsetof(struct Normal, x));
  printf("  offset of 'short  y': %zu\n", offsetof(struct Normal, y));
  printf("  offset of 'int    z': %zu\n", offsetof(struct Normal, z));
  printf("  offset of 'double w': %zu\n\n", offsetof(struct Normal, w));

  printf("--- struct Packed (__attribute__((packed)), no padding) ---\n");
  printf("Total Size: %zu bytes\n", sizeof(struct Packed));
  printf("  offset of 'char   x': %zu\n", offsetof(struct Packed, x));
  printf("  offset of 'short  y': %zu\n", offsetof(struct Packed, y));
  printf("  offset of 'int    z': %zu\n", offsetof(struct Packed, z));
  printf("  offset of 'double w': %zu\n\n", offsetof(struct Packed, w));

  printf("Bytes saved by packing: %zu\n\n",
         sizeof(struct Normal) - sizeof(struct Packed));

  printf("Packed:      ok\n");
}

int main(void) {
  test_inefficient();
  test_efficient();
  test_mixed();
  test_packed();
  printf("all tests passed\n");
  return 0;
}
