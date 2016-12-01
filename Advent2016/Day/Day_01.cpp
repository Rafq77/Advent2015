#include "stdafx.h"
#include "Day_01.h"


Day_01::Day_01::Day_01() {
};

Day_01::Day_01::~Day_01() {
};

void Day_01::Day_01::ReadFile(std::string fileName) {
	std::ifstream input;
	std::string word;

	input.open("Resources/Day_01.txt", std::ifstream::in);
	if (false == input.is_open()) {
		std::cout << "Can't open file: " << fileName << std::endl;
		return;
	}

	while (true != input.eof()) {
		input >> word;
		instructions.push_back(Instruction::Parse(word));
	}
	input.close();

	std::cout << instructions.size() << " instructinos in total\n";
}

void Day_01::Day_01::MoveToPosition() {
	for each (Instruction instruction in instructions) {
		position.Move(instruction);
	}
}

void Day_01::Day_01::WhereAmI() {
	position.Print();
}

void Day_01::Position::Print() {
	std::cout << "I'm at x:" << x << "\ty:" << y << "\tfacing " << orientation << " dist is:" << std::abs(x) + std::abs(y) << std::endl;
	std::cout << hqAddress << std::endl;
}

void Day_01::Position::Move(Instruction instruction) {

	// first rotate
	switch (instruction.rotation) {
	case Right:
		RotateRight();
		break;
	case Left:
		RotateLeft();
		break;
	default:
		std::cout << "could not determine rotation" << std::endl;
	}

	// then move
	MoveForward(instruction.distance);
};

void Day_01::Position::RotateLeft() {
	switch (orientation) {
	case North:
		orientation = West;
		break;
	case East:
		orientation = North;
		break;
	case South:
		orientation = East;
		break;
	case West:
		orientation = South;
		break;
	default:
		std::cout << "Could not rotate!" << std::endl;
		break;
	}
}

void Day_01::Position::RotateRight() {
	switch (orientation) {
	case North:
		orientation = East;
		break;
	case East:
		orientation = South;
		break;
	case South:
		orientation = West;
		break;
	case West:
		orientation = North;
		break;
	default:
		std::cout << "Could not rotate!" << std::endl;
		break;
	}
}

void Day_01::Position::MoveForward(int steps) {
	
	int tx = x;
	int ty = y;

	for (int i = 0; i < steps; ++i) {
		std::stringstream ss;
		ss.str("");

		switch (orientation) {
		case North:
			ty++;
			break;
		case East:
			tx++;
			break;
		case South:
			ty--;
			break;
		case West:
			tx--;
			break;
		default:
			std::cout << "Could not rotate!" << std::endl;
			break;
		}

		ss << tx << ty;
		auto result = visitedCoords.insert(ss.str());
		if (false == result.second) {
			//std::cout << "Intersection at x:" << tx << "\ty:" << ty << "\tdist:" << std::abs(tx) + std::abs(ty) << std::endl;
			if (false == hqFound) {
				hqFound = true;
				ss.str("");
				ss << "HQ at x:" << tx << "\ty:" << ty << "\tdist:" << std::abs(tx) + std::abs(ty);
				hqAddress = ss.str();
			}
		}
	}

	switch (orientation) {
	case North:
		y += steps;
		break;
	case East:
		x += steps;
		break;
	case South:
		y -= steps;
		break;
	case West:
		x -= steps;
		break;
	default:
		std::cout << "Could not rotate!" << std::endl;
		break;
	}
}

Day_01::Instruction Day_01::Instruction::Parse(std::string instruction) {
	Instruction inst;
	if (instruction[0] == 'R') {
		inst.rotation = Right;
	} else if (instruction[0] == 'L') {
		inst.rotation = Left;
	} 
	instruction.erase(0, 1);

	if (instruction.back() == ',') {
		instruction.pop_back();
	}

	inst.distance = std::stoi(instruction);
	return inst;
}
