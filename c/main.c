#include <stdio.h>
#include <stdlib.h>

int main() {
  struct MyStruct {
    int number;
  };
  struct MyStruct struct1 = {1};
  printf("%p\n", &struct1);
  printf("%d\n", struct1.number);

  struct MyStruct *ptr_to_struct = &struct1;
  printf("%p\n", ptr_to_struct);
  printf("%d\n", (*ptr_to_struct).number);
  printf("%d\n", ptr_to_struct->number);

  return 0;
}
