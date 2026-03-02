CC = gcc
CFLAGS = -Wall -Wextra -fsanitize=address,undefined -g
TARGET = vec_test
SRCS = vec.c vec_main.c
OBJS = $(SRCS:.c=.o)

.PHONY: all clean run

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) -o $@ $^

%.o: %.c vec.h
	$(CC) $(CFLAGS) -c $< -o $@

run: all
	./$(TARGET)

clean:
	rm -f $(OBJS) $(TARGET)
