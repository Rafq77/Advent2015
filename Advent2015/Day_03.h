#pragma once
#include "Day.h"
#include <string>
#include <iostream>
#include <fstream>
#include <map>

namespace Day_03 {

	class Day_03 :
		public Day {

		bool swapTurnsWithRobot = false;
		bool useSantaPos;
		std::string filename;
		std::string steps;
		std::ifstream input;

		std::pair<int, int> santaPos;
		std::pair<int, int> robotPos;

		std::map<std::pair<int, int>, int> visitedHouses;

	private:
		//std::pair<int, int> 
	public:
		Day_03();
		~Day_03();

		// Inherited via Day
		virtual void DoMagic() override;
		virtual void PrintOutput() override;
	};
}
