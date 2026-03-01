#include <stdio.h>
#include "math_utils.h"

// Preprocessor macro
#define RADIUS 10

int main() {
    int sum = add(5, 7);
    float area = PI * RADIUS * RADIUS;

    printf("Sum of 5 + 7: %d\n", sum);
    printf("Area of circle (radius 10): %f\n", area);

    return 0;
}
