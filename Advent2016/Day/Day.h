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
		std::vector<std::string> words;

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
				words.push_back(word);
			}
			input.close();
		}

		std::vector<std::string> SplitString(std::string& string) {

			std::istringstream buf(string);
			std::istream_iterator<std::string> beg(buf), end;
			std::vector<std::string> tokens(beg, end); // done!;


			return tokens;
		};
	};
}
