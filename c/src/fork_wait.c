#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <unistd.h>

int compute() {
  int sum = 0;
  for (size_t i = 0; i < 100; ++i) {
    sum += i;
  }
  return sum;
}

int main(void) {
  pid_t pid1 = fork();

  if (pid1 < 0) {
    perror("fork");
    return 1;
  }

  if (pid1 == 0) {
    int result = compute();
    exit(result % 256);
  } else {
    int status;
    waitpid(pid1, &status, 0);
    if (WIFEXITED(status)) {
      printf("child1 exited with %d\n", WEXITSTATUS(status));
    }
  }

  pid_t pid2 = fork();

  if (pid2 == 0) {
    abort();
  } else if (pid2 > 0) {
    int status;
    waitpid(pid2, &status, 0);
    if (WIFSIGNALED(status)) {
      printf("Child 2 killed by signal: %d\n", WTERMSIG(status));
    }
  }

  return 0;
}
