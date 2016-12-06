#pragma once
#include <algorithm>
#include <vector>
#include <string>
#include <fstream>
#include <iostream>
#include <sstream>
#include <tuple>
#include "Day.h"

namespace Day_06 {

	class Day_06 : public Day::Day {
	private:
		std::vector<std::tuple<char, unsigned int>> commonElements;
		std::string task1;
		std::string task2;

		void SortCommonElements();
		void InitializeCommonElements();

	public:
		void Evaluate();
		void Print();
		Day_06();
		~Day_06();
	};

}
