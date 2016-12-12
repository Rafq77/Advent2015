#include "Day_12.h"

Day_12::Day_12::Day_12() {
};

Day_12::Day_12::~Day_12() {
};


int Day_12::Day_12::DoAsm(int a, int b, int c, int d) {

	__asm {
		mov a, 1
		mov b, 1
		mov d, 26
		cmp c, 0//mov eax, c
		jne jmp1 //jnz 2 
		jmp jmp2 //jmp 5  // jnz 1 5, extra instr
	jmp1:
		mov c, 7
	jmp3:
		inc d
		dec c
		cmp c, 0//mov eax, c
		jne jmp3 //jnz -2 extra instr
	jmp2:
		mov eax, a
		mov c, eax
	jmp4:
		inc a
		dec b
		cmp b, 0 //mov eax, b			// extra instr
		jne jmp4 //jnz -2 
		mov eax, c
		mov b, eax
		dec d
		cmp d, 0 //mov eax, d			// extra instr
		jne jmp2 //jnz-6 // 2 extra instr
		mov c, 18
	jmp6:
		mov d, 11
	jmp5:
		inc a
		dec d
		cmp d, 0//mov eax, d			// extra instr
		jne jmp5 //jnz -2 //extra instr
		dec c
		cmp c, 0//mov eax, c			// extra instr
		jne jmp6 // jnz -5 

			// original:
			//cpy 1 b
			//cpy 1 a
			//cpy 26 d
			//jnz c 2
			//jnz 1 5
			//cpy 7 c
			//inc d
			//dec c
			//jnz c - 2
			//cpy a c
			//inc a
			//dec b
			//jnz b - 2
			//cpy c b
			//dec d
			//jnz d - 6
			//cpy 18 c
			//cpy 11 d
			//inc a
			//dec d
			//jnz d - 2
			//dec c
			//jnz c - 5
	}
	return a;
}

void Day_12::Day_12::Evaluate() {

	int a = 0;
	int b = 0;
	int c = 0;
	int d = 0;
	task1 = DoAsm(a, b, c, d);

	a = 0;
	b = 0;
	c = 1;
	d = 0;
	task2 = DoAsm(a, b, c, d);
}

void Day_12::Day_12::Print() {
	std::cout << "Day12: Task1:" << task1 << " Task2:" << task2 << std::endl;
}

