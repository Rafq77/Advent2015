#include "stdafx.h"
#include "Day_05.h"

	const char* Day_05::Day_05::input = "ugkcyxxp";

Day_05::Day_05::Day_05() 
{
};

Day_05::Day_05::~Day_05() {
};

void Day_05::Day_05::Evaluate() {
	//std::cout << md5("abc5017308") << std::endl;
	//unsigned long int i = 0;
	int idx = 0;
	bool done = false;
	std::string hash;
	std::stringstream ss;

#pragma omp parallel for num_threads(8) private(ss, hash)
	for (long int i = 0; i < 26'000'000; ++i) {
		ss.str(""); // clear
		ss << input << i; // nuthing will happen with "0" ;-)
		//std::cout << ss.str() << std::endl;

		hash = md5(ss.str());
		if (hash.compare(0, 5, "00000") == 0) {
			std::cout << hash << std::endl;
#pragma omp atomic
			++idx;
		}
		if (idx >= 8) {
			break;
		}
	}

	Print();
}


void Day_05::Day_05::Print() {
	//std::cout << "Day 05  Sum: " << sectorSum << " room id: " << secretRoomId << std::endl;
}
