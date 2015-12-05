#include "stdafx.h"
#include "Day_02.h"


Day_02::Day_02::Day_02() :
	presents(),
	presentsRaw() {
}

Day_02::Day_02::~Day_02() {
}

/// parse input data here (txt file)
void Day_02::Day_02::DoMagic() {

	ReadFile();

	for each (auto string in presentsRaw) {
		presents.push_back(ParseString(string));
	}

	totalRibbon = 0;
	totalWrapping = 0;

	for each (auto box in presents) {
		totalWrapping += box.Area() + box.SmallestArea();
		totalRibbon += box.Ribbon();
	}
}

void Day_02::Day_02::PrintOutput() {
	std::cout << "02. Total is total = " << totalWrapping << " Ribbon= " << totalRibbon << std::endl;
}

void Day_02::Day_02::ReadFile() {
	std::ifstream input;
	std::string word;

	input.open("Day_02.txt", std::ifstream::in);
	if (false == input.is_open()) {
		std::cout << "Can't open file: " << filename << std::endl;
		return;
	}

	while (true != input.eof()) {
		input >> word;
		presentsRaw.push_back(word);
	}
	input.close();
}

// bruteforce
Day_02::Box Day_02::Day_02::ParseString(std::string _word) {
	int w, l, h;
	sscanf_s(_word.c_str(), "%dx%dx%d", &w, &l, &h);
	return Box(w, h, l);
}
