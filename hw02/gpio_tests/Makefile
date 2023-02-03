#
# Programs
#
all:	togglegpio toggle0 toggle1

togglegpio:	togglegpio.o gpio-utils.o
	$(CC) $(LDFLAGS) -o $@ $^

toggle0: toggle0.c
	$(CC) $(LDFLAGS) -o $@ $^ -lgpiod

toggle1: toggle1.c
	$(CC) $(LDFLAGS) -o $@ $^ -lgpiod

#
# Objects
#

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm toggle0 toggle1