#pragma once
#include <vector>
#include <set>
#include <string>
#include <fstream>
#include <iostream>
#include <sstream>

namespace Day_02 {

	class Day_02  {
	private:

		int triangleCount;
		std::string input;
		std::vector<std::string> keys;

	public:
		void ReadFile(std::string fileName);
		void Evaluate();
		void PrepareTask2();
		void Print();
		Day_02();
		~Day_02();

	};
}
