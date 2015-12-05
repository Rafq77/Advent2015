#include "stdafx.h"
#include "Day_01.h"

void Day_01::Day_01::CountFloor() {
	int i = 0, j = 0;
	bool dontEnter = false;

	for each (auto var in advent_00_0) {
		(var == '(') ? ++i : --i;
		j++;

		if (!dontEnter && i == -1) {
			this->firstTimeInBasement = j;
			dontEnter = true;
		}

		this->finalFloor = i;
	}
}

Day_01::Day_01::Day_01() {
}


Day_01::Day_01::~Day_01() {
}

void Day_01::Day_01::DoMagic() {
	CountFloor();
}

void Day_01::Day_01::PrintOutput() {
	std::cout << "01. First time in basement at " << this->firstTimeInBasement << "; Final floor: " << this->finalFloor << std::endl;
}
