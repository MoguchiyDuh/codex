#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

static volatile sig_atomic_t keep_running = 1;

void handle_sigint(int sig) {
  (void)sig;
  keep_running = 0;
}

int main(void) {
  struct sigaction sa;
  sa.sa_handler = handle_sigint;
  sigemptyset(&sa.sa_mask);
  sa.sa_flags = 0;

  if (sigaction(SIGINT, &sa, NULL) == -1) {
    perror("sigaction");
    return 1;
  }

  while (keep_running) {
    printf("running...\n");
    fflush(stdout);
    sleep(1);
  }

  printf("shutdown cleanly\n");
  return 0;
}
