#include <iostream>

int main() {
	int32_t a = 0, b = 0, c = 0, d = 0;
	bool jump = false;

	a = 12;
	b = a;
	b--;
lbl2:
	a *= b;
	b--;
	c = 2 * b;

	if (c == 2)
		jump = true;

	if (!jump)
		goto lbl2;

	//tgl c
	//cpy - 16 c
	//jnz 1 c

	a += 76 * 85;
	std::cout << std::dec << "\nSecret Number in a:" << a << std::endl;
}
