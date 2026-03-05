#include <assert.h>
#include <stdio.h>
#include <string.h>

// ─── Tag (discriminant) ────────────────────────────────────────────────────
typedef enum {
  TYPE_INT,
  TYPE_FLOAT,
  TYPE_BOOL,
  TYPE_STRING,
} ValueType;

// ─── Tagged union ──────────────────────────────────────────────────────────
// The struct bundles the tag together with the union.  Only the member
// selected by `type` is valid at any given time; reading any other member
// is undefined behaviour.
typedef struct {
  ValueType type;

  union {
    int i;
    float f;
    int b; // 0 = false, 1 = true
    char s[64];
  } as;
} Value;

// ─── Constructors ─────────────────────────────────────────────────────────
Value value_int(int i) { return (Value){.type = TYPE_INT, .as.i = i}; }
Value value_float(float f) { return (Value){.type = TYPE_FLOAT, .as.f = f}; }
Value value_bool(int b) { return (Value){.type = TYPE_BOOL, .as.b = b}; }
Value value_string(const char *s) {
  Value v = {.type = TYPE_STRING};
  strncpy(v.as.s, s, sizeof(v.as.s) - 1);
  return v;
}

// ─── Helpers ──────────────────────────────────────────────────────────────
// Returns 1 on success, 0 on type mismatch.
int add_values(const Value *a, const Value *b, Value *out) {
  if (a->type == TYPE_INT && b->type == TYPE_INT) {
    *out = value_int(a->as.i + b->as.i);
    return 1;
  }
  if (a->type == TYPE_FLOAT && b->type == TYPE_FLOAT) {
    *out = value_float(a->as.f + b->as.f);
    return 1;
  }
  return 0;
}

void print_value(const Value *v) {
  switch (v->type) {
  case TYPE_INT:
    printf("int(%d)", v->as.i);
    break;
  case TYPE_FLOAT:
    printf("float(%.2f)", v->as.f);
    break;
  case TYPE_BOOL:
    printf("bool(%s)", v->as.b ? "true" : "false");
    break;
  case TYPE_STRING:
    printf("string(\"%s\")", v->as.s);
    break;
  }
}

// ─── tests ────────────────────────────────────────────────────────────────
void test_constructors(void) {
  Value i = value_int(42);
  assert(i.type == TYPE_INT);
  assert(i.as.i == 42);

  Value f = value_float(1.5f);
  assert(f.type == TYPE_FLOAT);
  assert(f.as.f == 1.5f);

  Value bt = value_bool(1);
  assert(bt.type == TYPE_BOOL);
  assert(bt.as.b == 1);

  Value bf = value_bool(0);
  assert(bf.type == TYPE_BOOL);
  assert(bf.as.b == 0);

  Value s = value_string("hello");
  assert(s.type == TYPE_STRING);
  assert(strcmp(s.as.s, "hello") == 0);

  printf("constructors: ok\n");
}

void test_add_int(void) {
  Value a = value_int(10);
  Value b = value_int(32);
  Value result;

  assert(add_values(&a, &b, &result) == 1);
  assert(result.type == TYPE_INT);
  assert(result.as.i == 42);

  // print for visual inspection
  printf("  ");
  print_value(&a);
  printf(" + ");
  print_value(&b);
  printf(" = ");
  print_value(&result);
  printf("\n");

  printf("add int:      ok\n");
}

void test_add_float(void) {
  Value x = value_float(1.5f);
  Value y = value_float(2.5f);
  Value result;

  assert(add_values(&x, &y, &result) == 1);
  assert(result.type == TYPE_FLOAT);
  assert(result.as.f == 4.0f);

  printf("  ");
  print_value(&x);
  printf(" + ");
  print_value(&y);
  printf(" = ");
  print_value(&result);
  printf("\n");

  printf("add float:    ok\n");
}

void test_type_mismatch(void) {
  Value i = value_int(10);
  Value f = value_float(1.5f);
  Value result;

  // mismatched types must be rejected
  assert(add_values(&i, &f, &result) == 0);
  assert(add_values(&f, &i, &result) == 0);

  // non-numeric types must also be rejected
  Value s = value_string("hi");
  Value b = value_bool(1);
  assert(add_values(&s, &b, &result) == 0);

  printf("type mismatch: ok\n");
}

void test_sizes(void) {
  // union is as large as its biggest member (char s[64])
  assert(sizeof(((Value *)0)->as) == 64);
  // tag adds 4 bytes (enum), so the full Value must be at least 68
  assert(sizeof(Value) >= 68);

  printf("sizes: ok\n");
}

int main(void) {
  test_constructors();
  test_add_int();
  test_add_float();
  test_type_mismatch();
  test_sizes();
  printf("all tests passed\n");
  return 0;
}
