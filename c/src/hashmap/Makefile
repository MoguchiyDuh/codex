CC = gcc
CFLAGS = -Wall -Wextra -fsanitize=address,undefined -g
TARGET = hashmap_test
SRCS = hashmap.c hashmap_main.c
OBJS = $(SRCS:.c=.o)

.PHONY: all clean run

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) -o $@ $^

%.o: %.c hashmap.h
	$(CC) $(CFLAGS) -c $< -o $@

run: all
	./$(TARGET)

clean:
	rm -f $(OBJS) $(TARGET)
