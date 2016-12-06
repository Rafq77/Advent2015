#pragma once
#include <algorithm>
#include <vector>
#include <string>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <tuple>
#include "../Libs/md5.h"
#include <omp.h>

namespace Day_05 {

	class Day_05 {
	private:
		static const char* input; 
		std::stringstream t1;
		std::stringstream t2;

	public:
		void Evaluate();
		void Print();
		Day_05();
		~Day_05();
	};

}
