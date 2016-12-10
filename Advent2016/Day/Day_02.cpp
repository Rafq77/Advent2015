#include "Day_02.h"


Day_02::Day_02::Day_02() {
};

Day_02::Day_02::~Day_02() {
};

void Day_02::Day_02::ReadFile(std::string fileName) {
	std::ifstream input;
	std::string word;

	input.open(fileName, std::ifstream::in);
	if (false == input.is_open()) {
		std::cout << "Can't open file: " << fileName << std::endl;
		return;
	}

	while (true != input.eof()) {
		// read
		input >> word;
		keys.push_back(word);
	}
	input.close();
}

void Day_02::Day_02::Evaluate() {

	std::cout << "Day2 a: ";

	for each (std::string key in keys) {
		for each (char direction in key) {
			keypad.Move(direction);
		}
		keypad.PrintKey();
	}
	std::cout << std::endl;

	std::cout << "Day2 b: ";

	for each (std::string key in keys) {
		for each (char direction in key) {
			keypadDiamond.Move(direction);
		}
		keypadDiamond.PrintKey();
	}

	std::cout << std::endl;
}

void Day_02::Keypad::Move(char direction) {
	switch (direction) {
	case 'R':
		position.GoRight();
		break;
	case 'L':
		position.GoLeft();
		break;
	case 'U':
		position.GoUp();
		break;
	case 'D':
		position.GoDown();
		break;
	default:
		std::cout << "Problem!" << std::endl;
		break;
	}
}

Day_02::Keypad::Keypad() {
	position.Initialize(1, 1, Square, 2);
}

void Day_02::Keypad::PrintKey() {
	std::cout << keys[position.GetY()][position.GetX()]; 
}

/* 
 * This function is repeated because the ancestor (Keypad) is not aware of the new "key" class member. 
 * The "key" array is pre-defined and thus its size is also fixed. The parent class has no way of knowing that.
 * That is why i need to "overwrite" the old PrintKey function, because without it the child class was calling 
 * the parent's class function which was looking up its "key" (3,3) array, thus reading junk from memory.
 *
 * A proper solution to this would be adding a dynamic array which would set its contents during runtime. 
 * then, the parent class and child class would use the same "key" member. Currently the child class has also the 
 * parent class "key" array in its instance (i.e. it holds both arrays altough they have the same name).
 * 
*/

void Day_02::KeypadDiamond::PrintKey() {
	std::cout << keys[position.GetY()][position.GetX()];
}

void Day_02::KeypadPos::GoLeft() {
	SavePosition();
	--x;
	ValidatePos();
}

void Day_02::KeypadPos::GoRight() {
	SavePosition();
	++x;
	ValidatePos();
}

void Day_02::KeypadPos::GoUp() {
	SavePosition();
	--y;
	ValidatePos();
}

void Day_02::KeypadPos::GoDown() {
	SavePosition();
	++y;
	ValidatePos();
}

void Day_02::KeypadPos::SavePosition() {
	lastValidX = x;
	lastValidY = y;
}

void Day_02::KeypadPos::RestoreLastValidPosition() {
	x = lastValidX;
	y = lastValidY;
}

const int & Day_02::KeypadPos::GetX() const {
	return x + xOffset;
}

const int & Day_02::KeypadPos::GetY() const {
	return y + yOffset;
}

void Day_02::KeypadPos::Initialize(int _x, int _y, ValidationPolicy _policy, int _keypadSize, int _xOffset, int _yOffset) {
	x = _x;
	y = _y;
	policy = _policy;
	keypadSize = _keypadSize;
	xOffset = _xOffset;
	yOffset = _yOffset;
}

void Day_02::KeypadPos::ValidatePos() {
	bool positionValid = true;
	if (policy == Square) {
		positionValid = VerifySquare();
	} else if (policy == Distance) {
		positionValid = VerifyDistance();
	} 

	if (positionValid == false) {
		RestoreLastValidPosition();
	}
}

bool Day_02::KeypadPos::VerifySquare() {
	if (x < 0 || x > keypadSize || y < 0 || y > keypadSize)
		return false;
	else
		return true;
}

bool Day_02::KeypadPos::VerifyDistance() {
	if (std::abs(x) + std::abs(y) > xOffset) 
		return false;
	else
		return true;
}

Day_02::KeypadDiamond::KeypadDiamond() {
	position.Initialize(-2, 0, Distance, 2,2,2);
}
