#include "stdafx.h"
#include "Day_08.h"

Day_08::Day_08::Day_08() 
: task1(0)
{
	for (size_t x = 0; x < WIDTH; ++x) {
		for (size_t y = 0; y < HEIGHT; ++y) {
			screen[x][y] = '.'; // off
		}
	}
};

Day_08::Day_08::~Day_08() {
};

unsigned short Day_08::Day_08::Count() {
	unsigned short cnt = 0;
	for (size_t x = 0; x < WIDTH; ++x) {
		for (size_t y = 0; y < HEIGHT; ++y) {
			cnt += (screen[x][y] == '#') ? 1 : 0; 
		}
	}
	return cnt;
}

void Day_08::Day_08::ExecuteInstruction(std::vector<std::string> instr) {
	if (instr.size() < 1)
		return;
	if (instr[0] == "rect") {
		size_t xPos = instr[1].find('x');
		size_t x = atoi(instr[1].substr(0, xPos).c_str());
		size_t y = atoi(instr[1].substr(xPos+1).c_str());
		SwitchOn(x, y);

	} else if (instr[1] == "column") {
		size_t pos = instr[2].find('=');
		size_t x = atoi(instr[2].substr(pos+1).c_str());
		RotateColumn(x, atoi(instr[4].c_str()));

	} else if (instr[1] == "row") {
		size_t pos = instr[2].find('=');
		size_t y = atoi(instr[2].substr(pos+1).c_str());
		RotateRow(y, atoi(instr[4].c_str()));
	}
}

void Day_08::Day_08::SwitchOn(size_t X, size_t Y) {
	for (size_t x = 0; x < X; ++x) {
		for (size_t y = 0; y < Y; ++y) {
			screen[x][y] = '#';
		}
	}
}

void Day_08::Day_08::RotateColumn(size_t X, size_t by) {
	char tmp[HEIGHT];

	for (int y = 0; y < HEIGHT; ++y) {
		tmp[y] = screen[X][y];
	}

	for (int y = 0; y < HEIGHT; ++y) {
		screen[X][(y + by)%HEIGHT] = tmp[y];
	}
};

void Day_08::Day_08::RotateRow(size_t Y, size_t by) {
	char tmp[WIDTH];

	for (int x = 0; x < WIDTH; ++x) {
		tmp[x] = screen[x][Y];
	}

	for (int x = 0; x < WIDTH; ++x) {
		screen[(x + by)%WIDTH][Y] = tmp[x];
	}
};

void Day_08::Day_08::Evaluate() {
	std::string wordPart;
	std::vector<std::string> instruction;
	
	size_t idx = 0;

	for (auto& word : words) {
		if (word.compare("rect") == 0
			|| word.compare("rotate") == 0) {
			//new instruction execute last one
			ExecuteInstruction(instruction);
			instruction.clear();

		} 
		instruction.push_back(word);
	}
}

void Day_08::Day_08::Print() {
	std::cout << "Day 08 task1: " << Count() << std::endl;
	for (int y = 0; y < HEIGHT; ++y) {
		for (int x = 0; x < WIDTH; ++x) {
			std::cout << (screen[x][y] == '#' ? '#' : ' ');
		}
		std::cout << std::endl;
	}
}