#pragma once
#include <vector>
#include <set>
#include <string>
#include <fstream>
#include <iostream>
#include <sstream>

namespace Day {

	class Day  {
	protected:
		std::string input;
		std::vector<std::string> keys;

	public:
		void ReadFile(std::string fileName) {
			std::ifstream input;
			std::string word;
			input.open(fileName, std::ifstream::in);

			if (false == input.is_open()) {
				std::cout << "Can't open file: " << fileName << std::endl;
				return;
			}

			while (true != input.eof()) {
				input >> word;
				keys.push_back(word);
			}
			input.close();
		}
	};
}
