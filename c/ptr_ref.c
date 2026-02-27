#include <assert.h>
#include <stdio.h>

// ── functions ─────────────────────────────────────────────────────────────────

void swap(int *a, int *b) {
    int temp = *b;
    *b = *a;
    *a = temp;
}

int sum(int *arr, int len) {
    int total = 0;
    for (int i = 0; i < len; ++i) total += arr[i];
    return total;
}

// ── tests ─────────────────────────────────────────────────────────────────────

void test_swap(void) {
    int a = 1, b = 2;
    swap(&a, &b);
    assert(a == 2 && b == 1);

    // swap same variable — should be a no-op
    int x = 5;
    swap(&x, &x);
    assert(x == 5);

    // negative values
    int neg = -3, pos = 7;
    swap(&neg, &pos);
    assert(neg == 7 && pos == -3);

    printf("swap: ok\n");
}

void test_sum(void) {
    int arr[] = {1, 2, 3, 4, 5};
    assert(sum(arr, 5) == 15);

    int single[] = {42};
    assert(sum(single, 1) == 42);

    int zeros[] = {0, 0, 0};
    assert(sum(zeros, 3) == 0);

    int negatives[] = {-1, -2, -3};
    assert(sum(negatives, 3) == -6);

    int mixed[] = {-5, 5};
    assert(sum(mixed, 2) == 0);

    // len == 0 — empty range
    assert(sum(arr, 0) == 0);

    printf("sum:  ok\n");
}

void test_pointer_arithmetic(void) {
    int arr[] = {10, 20, 30, 40, 50};
    int *p = arr;

    // arr[i] == *(p + i)
    for (int i = 0; i < 5; i++)
        assert(arr[i] == *(p + i));

    // pointer difference
    int *first = &arr[0];
    int *last  = &arr[4];
    assert(last - first == 4);

    printf("ptr arithmetic: ok\n");
}

void test_sizeof(void) {
    int arr[] = {1, 2, 3, 4, 5};
    int len = sizeof(arr) / sizeof(arr[0]);
    assert(len == 5);

    // sizeof pointer vs array — pointer is 8 on 64-bit
    int *p = arr;
    assert(sizeof(p) == 8);
    assert(sizeof(arr) == 5 * sizeof(int));

    printf("sizeof: ok\n");
}

int main(void) {
    test_swap();
    test_sum();
    test_pointer_arithmetic();
    test_sizeof();
    printf("all tests passed\n");
    return 0;
}
