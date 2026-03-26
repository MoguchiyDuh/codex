#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <unistd.h>

int main(void) {
  pid_t pid = fork();

  if (pid < 0) {
    perror("fork");
    return 1;
  }

  if (pid == 0) {
    printf("child with pid %d\n", getpid());
    exit(7);
  } else {
    int status;
    waitpid(pid, &status, 0);
    if (WIFEXITED(status))
      printf("child exited with %d\n", WEXITSTATUS(status));
  }

  return 0;
}
