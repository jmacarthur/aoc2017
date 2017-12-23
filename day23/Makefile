all: run23

code_fragment.c: input23.txt
	./transpiler.pl <input23.txt >code_fragment.c
run23: wrapper.c code_fragment.c
	gcc -O3 -o run23 wrapper.c
clean:
	rm -f code_fragment.c run23
