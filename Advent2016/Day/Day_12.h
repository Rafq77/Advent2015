#pragma once
#include <algorithm>
#include <vector>
#include <string>
#include <fstream>
#include <iostream>
#include <sstream>
#include <regex>
#include "Day.h"

namespace Day_12 {

	static unsigned int task1 = 1;
	static unsigned int task2 = 1;
		
	class Day_12 : public Day::Day {
	private:
		int DoAsm(int a, int b, int c, int d);

	public:
		void Evaluate();
		void Print();
		Day_12();
		~Day_12();
	};

}
