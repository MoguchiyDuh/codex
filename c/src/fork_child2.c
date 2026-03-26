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
    printf("child ls:\n");
    fflush(stdout);
    execvp("ls", (char *[]){"ls", "-la", NULL});
    perror("execvp");
    exit(1);
  } else {
    int status;
    waitpid(pid, &status, 0);
    if (WIFEXITED(status)) {
      printf("\nchild exited\n");
    }
  }

  return 0;
}
