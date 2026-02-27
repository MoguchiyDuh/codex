#include <assert.h>
#include <stdio.h>
#include <string.h>

// ── helpers ───────────────────────────────────────────────────────────────────

// Reinterpret the bytes of a float as an unsigned int (via memcpy — no UB).
static unsigned int float_bits(float f) {
    unsigned int bits;
    memcpy(&bits, &f, sizeof(float));
    return bits;
}

// Print float value, hex representation, and binary layout (sign|exp|mantissa).
void view(float *f) {
    unsigned int bits = float_bits(*f);
    printf("float: %.6g\n", *f);
    printf("hex:   0x%08X\n", bits);
    printf("bits:  ");
    for (int i = 31; i >= 0; i--) {
        printf("%d", (bits >> i) & 1);
        if (i == 31 || i == 23) printf(" ");
    }
    printf("\n");
}

// ── tests ─────────────────────────────────────────────────────────────────────

void test_known_bit_patterns(void) {
    // 1.0f: sign=0, exponent=127 (0x7F), mantissa=0
    // 0 01111111 00000000000000000000000 = 0x3F800000
    assert(float_bits(1.0f) == 0x3F800000);

    // -1.0f: same as 1.0f but sign bit set
    assert(float_bits(-1.0f) == 0xBF800000);

    // 0.5f: exponent=126 (127-1), mantissa=0
    // 0 01111110 00000000000000000000000 = 0x3F000000
    assert(float_bits(0.5f) == 0x3F000000);

    // 0.0f: all bits zero
    assert(float_bits(0.0f) == 0x00000000);

    // 2.0f: exponent=128 (127+1), mantissa=0
    assert(float_bits(2.0f) == 0x40000000);

    printf("known bit patterns: ok\n");
}

void test_special_values(void) {
    float inf  =  1.0f / 0.0f;
    float ninf = -1.0f / 0.0f;
    float nan  =  0.0f / 0.0f;

    // +infinity: exponent all 1s, mantissa all 0s, sign=0
    assert(float_bits(inf) == 0x7F800000);

    // -infinity: same with sign=1
    assert(float_bits(ninf) == 0xFF800000);

    // NaN: exponent all 1s, mantissa non-zero (exact bits are implementation-defined)
    unsigned int nan_bits = float_bits(nan);
    unsigned int exp_mask = 0x7F800000;
    unsigned int man_mask = 0x007FFFFF;
    assert((nan_bits & exp_mask) == exp_mask);  // exponent all 1s
    assert((nan_bits & man_mask) != 0);         // mantissa non-zero

    // NaN != NaN is always true (IEEE 754 rule)
    assert(nan != nan);

    printf("special values:     ok\n");
}

void test_sign_bit(void) {
    // Only the sign bit differs between +x and -x
    float pos = 3.14f;
    float neg = -3.14f;
    unsigned int diff = float_bits(pos) ^ float_bits(neg);
    assert(diff == 0x80000000);  // only bit 31 differs

    printf("sign bit:           ok\n");
}

int main(void) {
    test_known_bit_patterns();
    test_special_values();
    test_sign_bit();
    printf("all tests passed\n\n");

    // visual output for reference
    float values[] = {1.0f, -1.0f, 0.5f, 2.0f, 0.0f, 1.0f / 0.0f, 0.0f / 0.0f};
    int n = sizeof(values) / sizeof(values[0]);
    for (int i = 0; i < n; i++) {
        view(&values[i]);
        printf("\n");
    }

    return 0;
}
