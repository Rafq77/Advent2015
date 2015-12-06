#pragma once
#include "Day.h"
#include <vector>
#include <map>

namespace Day_06 {

	enum InstructionType {
		undefined,
		toggle,
		turnOn,
		turnOff
	};

	class Instruction {
	private:
		std::string word;

	public:
		InstructionType instructionType;
		std::pair<int, int> start;
		std::pair<int, int> end;

		Instruction(std::string _word) :
			word(_word),
			instructionType(undefined),
			start(std::pair<int,int> (0,0)),
			end(std::pair<int,int> (0,0)) {
		}

		void Parse();
	};

	class Day_06 : public Day {
	private:
		const static int RANGE_X = 1000;
		const static int RANGE_Y = 1000;
		
		std::fstream input;
		std::vector<Instruction> instructions;
		int **map;
		int lightsCount;
		long int totalBrightness;

		void InitializeMap();
		void DoTheMagic();
		void CountTheStars();
		void Save();

	public:
		Day_06();
		~Day_06();

		// Inherited via Day
		virtual void DoMagic() override;
		virtual void PrintOutput() override;
	};
}
