#pragma once
#include <algorithm>
#include <vector>
#include <string>
#include <fstream>
#include <iostream>
#include <sstream>
#include <regex>
#include "Day.h"

namespace Day_08 {


	class Day_08 : public Day::Day {
	private:
		static const size_t WIDTH = 50;
		static const size_t HEIGHT = 6;

		char screen[WIDTH][HEIGHT];

		unsigned short task1;
		unsigned short Count();
		void ExecuteInstruction(std::vector<std::string> instr);
		void SwitchOn(size_t X, size_t Y);
		void RotateColumn(size_t X, size_t by);
		void RotateRow(size_t Y, size_t by);

	public:
		void Evaluate();
		void Print();
		Day_08();
		~Day_08();
	};

}
