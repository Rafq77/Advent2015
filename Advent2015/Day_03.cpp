#include "stdafx.h"
#include "Day_03.h"

namespace Day_03 {

	Day_03::Day_03() :
		santaPos(std::pair<int, int>(0, 0)),
		robotPos(std::pair<int, int>(0, 0)) {
	}


	Day_03::~Day_03() {
		if (input.is_open()) {
			input.close();
		}
	}

	void Day_03::DoMagic() {
		input.open("Day_03.txt", std::ifstream::in);

		if (input.is_open()) {
			input >> steps;
			input.close();
		}
		else {
			//failed
			std::cout << "ERROR: Could not read from file: Day_03.txt" << std::endl;
			return;
		}

		std::pair<int, int> *ptr = &santaPos;

		bool useSantaPos = true;
		visitedHouses[*ptr] = 2;

		for each (auto c in steps) {
			switch (c) {
			case 'v':
				--ptr->second;
				break;
			case '>':
				++ptr->first;
				break;
			case '<':
				--ptr->first;
				break;
			case '^':
				++ptr->second;
				break;
			default:
				break;
			}

			if (visitedHouses.find(*ptr) == visitedHouses.end()) {
				visitedHouses[*ptr] = 0;
			}
			visitedHouses[*ptr]++;

			if (true == swapTurnsWithRobot) {
				useSantaPos ^= true;
				ptr = (useSantaPos) ? &santaPos : &robotPos;
			}
		}

	}

	void Day_03::PrintOutput() {
		std::cout << "03. Gifted Kids are= " << visitedHouses.size() << std::endl;
	}
}
