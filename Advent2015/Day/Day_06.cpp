#include "stdafx.h"
#include "Day_06.h"
#include <sstream>

namespace Day_06 {

	Day_06::Day_06() :
		lightsCount(0),
		totalBrightness(0),
		map()
		{
			InitializeMap();
	}

	Day_06::~Day_06() {
		for (int x = 0; x < RANGE_X; ++x) {
			try {
				delete[] map[x];
			} catch (const std::exception&) {
				// well, shit
			}
		}
		delete map;
	}

	void Day_06::DoMagic() {

		input.open("Resources/Day_06.txt", std::ifstream::in);

		if (input.is_open()) {
			std::string word;
			while (true != input.eof()) {
				std::getline(input, word);
				Instruction instruction(word);
				instruction.Parse();
				instructions.push_back(instruction);
			}
			input.close();
		}

		// lol the names
		DoTheMagic();
		CountTheStars();
		Save();
	}

	void Day_06::PrintOutput() {
		std::cout << "06. Lit lights " << lightsCount << " birghtness " << totalBrightness << std::endl;
	}

	void Day_06::InitializeMap() {
		map = new int*[RANGE_X];
		for (int x = 0; x < RANGE_X; ++x) {
			map[x] = new int[RANGE_Y];
			for (int y = 0; y < RANGE_Y; ++y) {
				map[x][y] = 0;
			}
		}
	}

	void Day_06::DoTheMagic() {
		for each (auto instruction in instructions) {
			int x = instruction.start.first;
			int y = instruction.start.second;

			for (x; x <= instruction.end.first; ++x) {
				for (y = instruction.start.second; y <= instruction.end.second; ++y) {
					switch (instruction.instructionType) {
						// part 1
					//case turnOn: 
					//	map[x][y] = 1;
					//	break;
					//case turnOff: 
					//	map[x][y] = 0;
					//	break;
					//case toggle: 
					//	map[x][y] = (map[x][y] == 1) ? 0 : 1;
					//	break;
						//part 2
					case turnOn: 
						++map[x][y];
						break;
					case turnOff: 
						if (map[x][y] > 0)
							--map[x][y];
						break;
					case toggle: 
						++++map[x][y];
						break;
					}
				}
			}
		}
	}

	void Day_06::CountTheStars() {
		lightsCount = 0;
		totalBrightness = 0;
		//for (auto& x : map) {
			//for (auto& y : x) {
		for (int x = 0; x < RANGE_X; ++x) {
			for (int y = 0; y < RANGE_Y; ++y) {
				if (0 != map[x][y]) {
					++lightsCount;
					totalBrightness += map[x][y];
				}
			}
		}
	}

	void Day_06::Save() {
		std::fstream out;
		std::stringstream row("");
		out.open("./Out.txt", std::fstream::out);

		//for (auto& x : map) {
			//for (auto& y : x) {
		for (int x = 0; x < RANGE_X; ++x) {
			row.str("");
			for (int y = 0; y < RANGE_Y; ++y) {
				if (true == map[x][y]) {
					row << "X";
				}
				else {
					row << " ";
				}
			}
			out << row.str() << std::endl;
		}
		out.close();
	}

	void Instruction::Parse() {
		if (this->word.size() <= 1) {
			instructionType = undefined;
			return;
		}

		//type 
		bool offset = ((word[1] == 'o') ? false : true);
		int pos = word.find(" ", 0);
		if (offset) {
			pos = word.find(" ", pos + 1);
		}
		int oldPos = pos;

		std::string type = word.substr(0, pos);
		 
		if (type == "toggle") {
			instructionType = toggle;
		} else if (type == "turn on") {
			instructionType = turnOn;
		} else if (type == "turn off") {
			instructionType = turnOff;
		} else {
			instructionType = undefined;
			return;
		}

		// startCoords
		int yEnd = word.find(" ", oldPos + 1);
		int xEnd = word.find(",", oldPos);

		int x = atoi(word.substr(pos, xEnd).c_str());
		int y = atoi(word.substr(xEnd + 1, yEnd).c_str());

		start = std::pair<int, int>(x, y);

		// through keyword

		//range
		yEnd = word.size();
		pos = word.rfind(" ", yEnd);
		xEnd = word.rfind(",", yEnd);

		x = atoi(word.substr(pos, xEnd).c_str());
		y = atoi(word.substr(xEnd + 1, yEnd).c_str());

		end = std::pair<int, int>(x, y);
	}
}
