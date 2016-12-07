#pragma once
#include <algorithm>
#include <vector>
#include <string>
#include <fstream>
#include <iostream>
#include <sstream>
#include <regex>
#include "Day.h"

namespace Day_07 {

	class Day_07 : public Day::Day {
	private:

		std::regex expr; 
		std::smatch match;

		std::stringstream ss;


		bool IsAbba(std::string& str);
		bool IsKek(std::string& kek, std::string& eke);
		unsigned short task1, task2;


	public:
		void Evaluate();
		void Print();
		Day_07();
		~Day_07();
	};

}
