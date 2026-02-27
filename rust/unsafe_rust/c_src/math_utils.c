#include <math.h>

/* --- Basic arithmetic --- */

int c_add(int a, int b) {
    return a + b;
}

int c_multiply(int a, int b) {
    return a * b;
}

/* --- Factorial (iterative) --- */

long long c_factorial(int n) {
    long long result = 1;
    for (int i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}

/* --- Struct passing by value --- */
/* Must match the #[repr(C)] layout on the Rust side */

typedef struct {
    double x;
    double y;
} CPoint;

double c_point_magnitude(CPoint p) {
    return sqrt(p.x * p.x + p.y * p.y);
}

/* --- Higher-order: function pointer callback --- */

int c_apply(int value, int (*fn)(int)) {
    return fn(value);
}

/* --- Buffer fill: caller allocates, C fills --- */
/* Returns number of chars written (excluding null terminator) */

int c_repeat_char(char c, int n, char *buf, int buf_len) {
    if (n >= buf_len) {
        n = buf_len - 1;
    }
    for (int i = 0; i < n; i++) {
        buf[i] = c;
    }
    buf[n] = '\0';
    return n;
}
