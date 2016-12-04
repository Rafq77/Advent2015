#pragma once
#include <algorithm>
#include <vector>
#include <string>
#include <fstream>
#include <iostream>
#include <sstream>
#include <tuple>
#include "Day.h"

namespace Day_04 {

	class Doorname {
	public:
		Doorname(std::string fullname);
		bool isReal();
		std::string Decipher();
		const unsigned long int& GetSectorId() const { return sectorId; }

	private:
		static const size_t CHECKSUM_SIZE = 5;
		std::string checksum;
		std::string letters;
		std::string originalName;
		unsigned long int sectorId;

		std::vector<std::tuple<char, unsigned int>> commonElements;
	};



	class Day_04 : public Day::Day {
	private:
		std::vector<Doorname> names;
		static const char* key; 

		int sectorSum;
		int secretRoomId;

	public:
		void Evaluate();
		void Print();
		Day_04();
		~Day_04();
	};

}
