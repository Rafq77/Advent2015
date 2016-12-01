#pragma once
#include <vector>
#include <set>
#include <string>
#include <fstream>
#include <iostream>
#include <sstream>
#include <map>

namespace Day_01 {
	enum Orientation {
		North,
		West,
		South,
		East
	};

	enum Rotation {
		Left,
		Right
	};

	class Instruction;

	class Position {
	public:
		Position() : 
			x(0), 
			y(0),
			orientation(North),
			hqFound(false)
		{};

		void Move(Instruction instruction);
		void Print();

	private:
		void RotateLeft();
		void RotateRight();
		void MoveForward(int steps);

		std::set<std::string> visitedCoords;
		std::string hqAddress;
		bool hqFound; // aka first Intersection
		Orientation orientation;
		int x;
		int y;
	};

	class Instruction {
		friend Position;
		Rotation rotation;
		int distance;

	public:
		static Instruction Parse(std::string instruction);
	};

	class Day_01  {
	private:

		Position position;
		std::string input;
		std::vector<Instruction> instructions;
		//std::vector<std::string> presentsRaw;

	public:
		void MoveToPosition();
		void ReadFile(std::string fileName);
		void WhereAmI();
		Day_01();
		~Day_01();

	};
}
